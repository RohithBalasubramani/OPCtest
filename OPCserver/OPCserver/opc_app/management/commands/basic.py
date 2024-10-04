import time
from django.core.management.base import BaseCommand
from opcua import Client
from opc_app.models import *  # Import your Django models
from django.db import transaction
from django.apps import apps
from opc_app.tag_model_mapping import tag_model_mapping



class Command(BaseCommand):
    help = 'Logs OPC UA values to Django models every 15 seconds'

    def handle(self, *args, **kwargs):
        # OPC UA server URL
        opcua_url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your OPC UA server URL

        # Connect to the OPC UA server
        client = Client(opcua_url)
        try:
            client.connect()
            self.stdout.write(self.style.SUCCESS('Connected to OPC UA server'))
            
            while True:
                for node_id, (model_name, field_name) in tag_model_mapping.items():
                    try:
                        # Get the model class dynamically
                        ModelClass = apps.get_model('opc_app', model_name)  # Replace 'your_app' with your actual app name
                        if not hasattr(ModelClass, field_name):
                            self.stdout.write(self.style.ERROR(f'Field "{field_name}" not found in model "{model_name}"'))
                            continue

                        # Read the value from OPC UA server
                        node = client.get_node(node_id)
                        value = node.get_value()

                        # Log the value to the database inside a separate transaction
                        with transaction.atomic():
                            ModelClass.objects.create(**{field_name: value})
                            self.stdout.write(self.style.SUCCESS(f'Successfully logged {field_name}: {value} to {model_name}'))

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error logging data for node {node_id}: {str(e)}'))

                # Wait for 15 seconds
                time.sleep(15)
        finally:
            client.disconnect()
            self.stdout.write(self.style.SUCCESS('Disconnected from OPC UA server'))
