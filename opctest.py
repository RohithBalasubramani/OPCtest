from opcua import Client
from opcua import ua

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

    # Browse children of the objects node to find the namespaces
    children = objects.get_children()
    for child in children:
        print(f"Child: {child}")

    # Get the specific namespace node, replace with your node id or path
    # For example, using the namespace identifiers from the image
    namespace_url = "http://phoenixcontact.com/OpcUA/DataSource/IEC61131-3"
    namespace_index = client.get_namespace_index(namespace_url)

    # Replace 'your_node_id' with the actual node id you want to read
    # Example node id format: f"ns={namespace_index};s=3-MCR"
    node_id = f"ns={namespace_index};s=3-MCR"  # Replace with the actual node id
    node = client.get_node(node_id)

    # Read the value of the node
    value = node.get_value()
    print(f"Value of node {node_id}: {value}")

    # Optionally, read multiple nodes
    node_ids = [
        f"ns={namespace_index};s=3-MCR",
        f"ns={namespace_index};s=3-PHASE-2",
        f"ns={namespace_index};s=3-CELL_LINE_1",
        f"ns={namespace_index};s=3-CELL_LINE_1_2",
        f"ns={namespace_index};s=3-CELL_LINE_3",
        f"ns={namespace_index};s=3-MODULEUPS",
        f"ns={namespace_index};s=3-AMFM",
        f"ns={namespace_index};s=3-VMS_1",
        f"ns={namespace_index};s=3-VMS_2"
    ]

    for node_id in node_ids:
        node = client.get_node(node_id)
        value = node.get_value()
        print(f"Value of node {node_id}: {value}")

finally:
    # Disconnect from the server
    client.disconnect()
    print("Disconnected from the OPC UA server")
