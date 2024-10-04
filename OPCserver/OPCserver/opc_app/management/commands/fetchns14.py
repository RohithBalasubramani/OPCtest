import time
import traceback
from django.core.management.base import BaseCommand
from django.apps import apps
from opcua import Client
from django.utils import timezone
from opc_app.tag_model_mapping import tag_model_mapping
from django.db import models, transaction

class Command(BaseCommand):
    help = 'Fetch data from OPC UA server and store in the database'

    def handle(self, *args, **kwargs):
        url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your OPC UA server URL and port
        client = Client(url)
        
        # Optionally, set the timeout for OPC UA operations (in milliseconds)
        # Uncomment the next line if `set_timeout` is supported in your `opcua` library version
        # client.set_timeout(60000)  # 60 seconds

        try:
            # Connect to OPC UA server
            conn_start = time.time()
            client.connect()
            conn_end = time.time()
            self.stdout.write(self.style.SUCCESS(
                f"Connected to OPC UA server in {conn_end - conn_start:.2f} seconds."
            ))

            # Start the timer for fetching data
            fetch_start = time.time()

            # Collect all node IDs
            node_ids = list(tag_model_mapping.keys())
            nodes = [client.get_node(node_id) for node_id in node_ids]

            # Define batch size to avoid timeout (adjust as needed)
            batch_size = 100  # Increased batch size for better performance
            model_instances = {}

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
                        try:
                            model_class = apps.get_model('opc_app', model_name)
                        except LookupError:
                            self.stderr.write(
                                f"Model '{model_name}' not found. Skipping tag {tag}."
                            )
                            continue

                        # Check if the field_name exists in the model
                        model_fields = [
                            field.name for field in model_class._meta.get_fields() 
                            if not field.is_relation
                        ]
                        if field_name not in model_fields:
                            self.stderr.write(
                                f"Field '{field_name}' does not exist in model '{model_name}'. Skipping tag {tag}."
                            )
                            continue

                        # Prepare the data with a fallback for other required fields
                        model_data = {
                            'timestamp': timezone.now(),
                            field_name: value
                        }

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

                        # Create the model instance but do not save yet
                        try:
                            model_instance = model_class(**model_data)
                        except Exception as e:
                            self.stderr.write(
                                f"Error creating model instance for tag {tag}: {e}"
                            )
                            traceback.print_exc()
                            continue

                        # Store instances in a dictionary grouped by model class
                        if model_class not in model_instances:
                            model_instances[model_class] = []
                        model_instances[model_class].append(model_instance)

                except Exception as e:
                    self.stderr.write(f"Error during batch read: {e}")
                    traceback.print_exc()
                    continue

            # End fetching data
            fetch_end = time.time()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Time to fetch and prepare data: {fetch_end - fetch_start:.2f} seconds."
                )
            )

            # Start the timer for bulk creation
            bulk_start = time.time()

            # Bulk create all instances for each model within a transaction
            try:
                with transaction.atomic():
                    for model_class, instances in model_instances.items():
                        if instances:
                            try:
                                model_class.objects.bulk_create(instances, ignore_conflicts=True)
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f"Bulk created {len(instances)} instances for model '{model_class.__name__}'."
                                    )
                                )
                            except Exception as e:
                                self.stderr.write(
                                    f"Error bulk creating instances for model '{model_class.__name__}': {e}"
                                )
                                traceback.print_exc()
            except Exception as e:
                self.stderr.write(f"Transaction Error: {e}")
                traceback.print_exc()

            # End bulk creation
            bulk_end = time.time()
            self.stdout.write(
                self.style.SUCCESS(f"Time to bulk create: {bulk_end - bulk_start:.2f} seconds.")
            )

            # Total execution time
            total_time = (fetch_end - fetch_start) + (bulk_end - bulk_start)
            self.stdout.write(
                self.style.SUCCESS(f"Total time taken to log all values: {total_time:.2f} seconds.")
            )

        except Exception as e:
            self.stderr.write(f"Error: {e}")
            traceback.print_exc()
        finally:
            try:
                client.disconnect()
                self.stdout.write(
                    self.style.SUCCESS("Disconnected from OPC UA server.")
                )
            except Exception as e:
                self.stderr.write(f"Error during disconnect: {e}")
                traceback.print_exc()
