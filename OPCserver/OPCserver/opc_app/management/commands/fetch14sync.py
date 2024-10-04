import time
from django.core.management.base import BaseCommand
from django.apps import apps
from opcua import Client
from django.utils import timezone
from opc_app.tag_model_mapping import tag_model_mapping
from django.db import models

class Command(BaseCommand):
    help = 'Fetch data from OPC UA server and store in the database'

    def handle(self, *args, **kwargs):
        url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your actual OPC UA server URL and port
        client = Client(url)

        try:
            client.connect()
            self.stdout.write(self.style.SUCCESS("Connected to OPC UA server."))

            while True:  # Infinite loop
                # Start the timer
                start_time = time.time()

                for tag, (model_name, field_name) in tag_model_mapping.items():
                    try:
                        # Access the OPC UA node directly using its NodeId
                        node = client.get_node(tag)
                        value = node.get_value()

                        # Dynamically get the model class using apps.get_model
                        try:
                            model_class = apps.get_model('opc_app', model_name)
                        except LookupError:
                            self.stderr.write(f"Model '{model_name}' not found. Skipping tag {tag}.")
                            continue

                        # Check if the field_name exists in the model
                        model_fields = [field.name for field in model_class._meta.get_fields() if not field.is_relation]
                        if field_name not in model_fields:
                            self.stderr.write(f"Field '{field_name}' does not exist in model '{model_name}'. Skipping tag {tag}.")
                            continue

                        # Prepare the data with a fallback for other required fields
                        model_data = {'timestamp': timezone.now(), field_name: value}

                        # Set defaults for all other required fields (if not provided)
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
                                else:
                                    # Handle other field types as needed
                                    pass

                        # Create and save the new instance of the model
                        model_instance = model_class(**model_data)
                        model_instance.save()

                        self.stdout.write(self.style.SUCCESS(
                            f"Saved data for {tag} into {model_name}.{field_name}"
                        ))

                    except Exception as e:
                        self.stderr.write(f"Error processing tag {tag}: {e}")

                # End the timer
                end_time = time.time()
                elapsed_time = end_time - start_time
                self.stdout.write(self.style.SUCCESS(f"Total time taken to log all values: {elapsed_time:.2f} seconds"))

                # Wait for 60 seconds before the next iteration
                time.sleep(60)

        except Exception as e:
            self.stderr.write(f"Error connecting to OPC UA server: {e}")

        finally:
            try:
                if client.uaclient._uasocket:  # Check if the socket was initialized
                    client.disconnect()
                    self.stdout.write(self.style.SUCCESS("Disconnected from OPC UA server."))
            except Exception as e:
                self.stderr.write(f"Error during disconnect: {e}")
