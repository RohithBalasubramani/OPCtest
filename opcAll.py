from opcua import Client

# Define the server URL
server_url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your server URL

# Create a client instance
client = Client(server_url)

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

    # Browse children of the objects node to find all data sources
    data_sources = objects.get_children()

    # Iterate over all data sources to find their global variables
    for data_source in data_sources:
        data_source_name = data_source.get_browse_name().Name
        print(f"\nData source: {data_source_name}")

        # Check if the data source has a GlobalVars node
        try:
            global_vars_node = data_source.get_child("2:GlobalVars")  # Adjust namespace index if needed
            print(f"  Found GlobalVars node: {global_vars_node}")

            # Get all child nodes under GlobalVars
            global_vars = global_vars_node.get_children()
            xlen=len(global_vars)
            print(xlen)

            # Print the details of each global variable
            # for var in global_vars:
            #     print(f"    Tag: {var}, Node ID: {var.nodeid}, Value: {var.get_value()}")
        except Exception as e:
            print(f"  GlobalVars node not found for data source '{data_source_name}'")

finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the OPC UA server")
