from opcua import Client

# Define the server URL
server_url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your server URL

# Create a client instance
client = Client(server_url)

def find_global_vars(node):
    """
    Recursively search for the GlobalVars node.
    """
    try:
        # Check if the current node is GlobalVars
        if "GlobalVars" in node.get_browse_name().Name:
            return node
        
        # Recursively check all child nodes
        for child in node.get_children():
            result = find_global_vars(child)
            if result:
                return result
    except:
        pass
    return None

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
    x=0

    # Iterate over all data sources to find their global variables
    for data_source in data_sources:
        data_source_name = data_source.get_browse_name().Name
        print(f"\nData source: {data_source_name}")

        # Find the GlobalVars node recursively
        global_vars_node = find_global_vars(data_source)
        if global_vars_node:
            print(f"  Found GlobalVars node: {global_vars_node}")

            # Get all child nodes under GlobalVars
            global_vars = global_vars_node.get_children()
            xlen=len(global_vars)
            print(xlen)
            x=x+xlen

            # # Print the details of each global variable
            # for var in global_vars:
            #     try:
            #         print(f"    Tag: {var}, Node ID: {var.nodeid}, Value: {var.get_value()}")
            #     except Exception as e:
            #         print(f"    Failed to get value for tag {var.nodeid}: {e}")
        else:
            print(f"  GlobalVars node not found for data source '{data_source_name}'")

finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the OPC UA server")
    print("total opc tags ", x)
