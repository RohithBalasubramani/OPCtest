import time
import traceback
from django.core.management.base import BaseCommand
from django.apps import apps
from opcua import Client
from django.utils import timezone
from opc_app.tag_model_mapping import tag_model_mapping
from django.db import models, transaction

class Command(BaseCommand):
    help = 'Continuously fetch data from OPC UA server and store in the database every 15 seconds.'

    def handle(self, *args, **kwargs):
        url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your OPC UA server URL and port
        client = Client(url)

        try:
            # Connect to OPC UA server
            self.connect_to_opcua(client)

            while True:
                try:
                    # Fetch data and prepare model instances
                    model_instances = self.fetch_data(client)
                    
                    # Bulk create all instances for each model within a transaction
                    self.bulk_create_instances(model_instances)

                except Exception as e:
                    self.stderr.write(f"Error during data fetch/store: {e}")
                    traceback.print_exc()
                    # Attempt to reconnect to OPC UA server
                    self.reconnect_to_opcua(client)

                # Sleep for 15 seconds before the next iteration
                time.sleep(15)

        except Exception as e:
            self.stderr.write(f"Error: {e}")
            traceback.print_exc()
        finally:
            self.disconnect_from_opcua(client)

    def connect_to_opcua(self, client):
        try:
            client.connect()
            self.stdout.write(self.style.SUCCESS("Connected to OPC UA server."))
        except Exception as e:
            self.stderr.write(f"Error connecting to OPC UA server: {e}")
            traceback.print_exc()

    def disconnect_from_opcua(self, client):
        try:
            client.disconnect()
            self.stdout.write(self.style.SUCCESS("Disconnected from OPC UA server."))
        except Exception as e:
            self.stderr.write(f"Error during disconnect: {e}")
            traceback.print_exc()

    def reconnect_to_opcua(self, client):
        self.stderr.write("Attempting to reconnect to OPC UA server...")
        self.disconnect_from_opcua(client)
        time.sleep(5)  # Small delay before attempting reconnection
        self.connect_to_opcua(client)

    def fetch_data(self, client):
        node_ids = list(tag_model_mapping.keys())
        nodes = [client.get_node(node_id) for node_id in node_ids]
        model_instances = {}
        batch_size = 100

        for i in range(0, len(nodes), batch_size):
            batch_nodes = nodes[i:i + batch_size]
            batch_tags = node_ids[i:i + batch_size]
            try:
                # Perform batch read
                values = client.get_values(batch_nodes)

                for idx, tag in enumerate(batch_tags):
                    value = values[idx]
                    model_name, field_name = tag_model_mapping[tag]

                    # Dynamically get the model class using apps.get_model
                    model_class = self.get_model_class(model_name)
                    if not model_class:
                        continue

                    # Check if the field_name exists in the model
                    if not self.is_field_in_model(field_name, model_class):
                        continue

                    # Prepare the data
                    model_data = self.prepare_model_data(model_class, field_name, value)

                    # Create the model instance but do not save yet
                    model_instance = self.create_model_instance(model_class, model_data)
                    if model_instance:
                        if model_class not in model_instances:
                            model_instances[model_class] = []
                        model_instances[model_class].append(model_instance)

            except Exception as e:
                self.stderr.write(f"Error during batch read: {e}")
                traceback.print_exc()
                continue

        return model_instances

    def get_model_class(self, model_name):
        try:
            return apps.get_model('opc_app', model_name)
        except LookupError:
            self.stderr.write(f"Model '{model_name}' not found. Skipping tag.")
            return None

    def is_field_in_model(self, field_name, model_class):
        model_fields = [field.name for field in model_class._meta.get_fields() if not field.is_relation]
        if field_name not in model_fields:
            self.stderr.write(f"Field '{field_name}' does not exist in model '{model_class.__name__}'. Skipping tag.")
            return False
        return True

    def prepare_model_data(self, model_class, field_name, value):
        model_data = {
            'timestamp': timezone.now(),
            field_name: value
        }

        # Set defaults for all other required fields
        for field in model_class._meta.fields:
            if field.name not in model_data and not field.null and field.default is models.fields.NOT_PROVIDED:
                # Skip auto fields and relationship fields
                if field.auto_created or field.name in ('id', 'pk'):
                    continue
                if isinstance(field, (models.ForeignKey, models.OneToOneField, models.ManyToManyField)):
                    continue
                # Assign a default value based on field type
                if isinstance(field, models.FloatField):
                    model_data[field.name] = 0.0
                elif isinstance(field, models.IntegerField):
                    model_data[field.name] = 0
                elif isinstance(field, models.CharField):
                    model_data[field.name] = ''
                elif isinstance(field, models.BooleanField):
                    model_data[field.name] = False

        return model_data

    def create_model_instance(self, model_class, model_data):
        try:
            # Create model instance
            return model_class(**model_data)
        except Exception as e:
            self.stderr.write(f"Error creating model instance: {e}")
            traceback.print_exc()
            return None

    def bulk_create_instances(self, model_instances):
        try:
            with transaction.atomic():
                for model_class, instances in model_instances.items():
                    if instances:
                        try:
                            model_class.objects.bulk_create(instances, ignore_conflicts=True)
                            self.stdout.write(
                                self.style.SUCCESS(f"Bulk created {len(instances)} instances for model '{model_class.__name__}'.")
                            )
                        except Exception as e:
                            self.stderr.write(f"Error bulk creating instances for model '{model_class.__name__}': {e}")
                            traceback.print_exc()
        except Exception as e:
            self.stderr.write(f"Transaction Error: {e}")
            traceback.print_exc()
