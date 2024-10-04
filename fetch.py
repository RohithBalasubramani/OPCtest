from opcua import Client
from tag_model_mapping import tag_model_mapping  # Import the generated mapping

def fetch_opc_data():
    url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your actual OPC UA server URL and port
    client = Client(url)
    
    try:
        # Connect to the OPC UA server
        print("Connecting to OPC UA server...")
        client.connect()
        print("Successfully connected to OPC UA server.")

        # No need to get the GlobalVars node if we're accessing nodes directly

        # Iterate through the tags in the mapping and fetch their values
        for tag, (model_name, field_name) in tag_model_mapping.items():
            try:
                # Access the OPC UA node directly using its NodeId
                node = client.get_node(tag)
                value = node.get_value()
                print(f"Tag: {tag}, Model: {model_name}, Field: {field_name}, Value: {value}")

            except Exception as e:
                print(f"Error fetching tag {tag}: {e}")

    except Exception as e:
        print(f"Error connecting to OPC UA server: {e}")
    finally:
        client.disconnect()
        print("Disconnected from OPC UA server.")

if __name__ == "__main__":
    fetch_opc_data()
