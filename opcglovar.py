from opcua import Client

# Replace with your OPC UA server URL
url = "opc.tcp://DESKTOP-ALRG67P:4840"
client = Client(url)

try:
    client.connect()
    
    # Replace with the actual Node ID for GlobalVars
    global_vars_node = client.get_node("ns=14;s=/.GlobalVars")
    
    # Get all child nodes under GlobalVars
    global_vars = global_vars_node.get_children()
    gl=len(global_vars)
    print(gl)
    
    # Print the details of each global variable
    for var in global_vars:
        print(f"Tag: {var}, Node ID: {var.nodeid}, Value: {var.get_value()}")
        
finally:
    client.disconnect()
