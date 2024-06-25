from opcua import Client

# Define the OPC UA server endpoint
server_url = "opc.tcp://DESKTOP-ALRG67P:4840"

# Create an instance of the OPC UA client
client = Client(server_url)

try:
    # Connect to the server
    client.connect()
    print(f"Client connected to OPC UA Server at {server_url}")

    # Get available endpoints
    endpoints = client.get_endpoints()
    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.EndpointUrl}")
        print(f"Security Mode: {endpoint.SecurityMode}")
        print(f"Security Policy: {endpoint.SecurityPolicyUri}")
        print("")

finally:
    client.disconnect()
    print("Client disconnected")
