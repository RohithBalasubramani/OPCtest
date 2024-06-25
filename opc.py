from opcua import Client

# Define the server URL
server_url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your server URL

# Create a client instance
client = Client(server_url)

# Specify the name of the data source you want to browse
target_data_source_name = "MODULEUPS"

try:
    # Connect to the server
    client.connect()
    print("Connected to the OPC UA server")

    # Get the root node
    root = client.get_root_node()
    print("Root node is: ", root)

    # Browse the objects node
    objects = client.get_objects_node()
    print("Objects node is: ", objects)

    # Browse children of the objects node to find the specific data source
    data_sources = objects.get_children()
    target_data_source = None
    for data_source in data_sources:
        if data_source.get_browse_name().Name == target_data_source_name:
            target_data_source = data_source
            break

    if target_data_source is not None:
        print(f"Found target data source: {target_data_source}")

        # Browse the tags under the specific data source
        tags = target_data_source.get_children()
        for tag in tags:
            print(f"  Tag: {tag} (Node ID: {tag.nodeid})")
    else:
        print(f"Data source '{target_data_source_name}' not found")

finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the OPC UA server")
