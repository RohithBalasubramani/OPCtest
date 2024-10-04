from opcua import Client
import pandas as pd
import time

# Replace with your OPC UA server URL
url = "opc.tcp://DESKTOP-ALRG67P:4840"
client = Client(url)

try:
    client.connect()
    
    start_time = time.time()
    # Replace with the actual Node ID for GlobalVars
    global_vars_node = client.get_node("ns=9;s=/.GlobalVars")
    
    # Get all child nodes under GlobalVars
    global_vars = global_vars_node.get_children()
    end_time= time.time()
    deltatime= end_time-start_time
    print("delta", deltatime)
    gl=len(global_vars)
    print(gl)

    node_id=[]
    value=[]
    
    # Print the details of each global variable
    for var in global_vars:
        print(f"Tag: {var}, Node ID: {var.nodeid}, Value: {var.get_value()}")
        # node_id.append(var.nodeid)
        # value.append(var.get_value())

    # data={"Node Id":node_id, "Value":value}
    # df=pd.DataFrame(data)
    # df.to_csv("Outglobal")
    # # print("dataframe:", df)
        
finally:
    client.disconnect()
