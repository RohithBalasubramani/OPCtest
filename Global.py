from opcua import Client
from opcua import ua

def list_opc_tags():
    # OPC UA Server URL
    url = "opc.tcp://DESKTOP-ALRG67P:4840"  # Replace with your actual OPC UA server URL and port

    # Initialize the OPC UA client
    client = Client(url)

    try:
        print("Connecting to OPC UA server...")
        client.connect()
        print("Successfully connected to OPC UA server.\n")

        # Retrieve and print the Namespace Array
        namespaces = client.get_namespace_array()
        print("Available Namespaces:")
        for idx, namespace in enumerate(namespaces):
            print(f"  Namespace {idx}: {namespace}")
        print("\n")

        # Define the NodeId for GlobalVars
        global_vars_nodeid = "ns=14;s=/.GlobalVars"

        # Get the GlobalVars node
        global_vars_node = client.get_node(global_vars_nodeid)

        # Verify if the node exists by reading its DisplayName
        display_name = global_vars_node.get_display_name().Text
        print(f"Accessing Node: {global_vars_nodeid} - DisplayName: {display_name}\n")

        # Browse all child nodes under GlobalVars
        print("Listing all child tags under GlobalVars:\n")
        browse_children(global_vars_node)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Disconnect from the server
        client.disconnect()
        print("\nDisconnected from OPC UA server.")

def browse_children(node, depth=0):
    """
    Recursively browse and print all child nodes under the given node.
    """
    try:
        # Browse the current node's children
        children = node.get_children()
        for child in children:
            # Retrieve NodeId and DisplayName
            nodeid = child.nodeid.to_string()
            display_name = child.get_display_name().Text

            # Indentation based on depth for readability
            indent = "  " * depth
            print(f"{indent}- {display_name} (NodeId: {nodeid})")

            # Recursively browse child nodes
            browse_children(child, depth + 1)
    except Exception as e:
        print(f"Error browsing children: {e}")

if __name__ == "__main__":
    list_opc_tags()
