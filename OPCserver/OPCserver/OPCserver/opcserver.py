# opc_app/opc_server.py
from opcua import Server
import time

def run_server():
    server = Server()
    server.set_endpoint("")  # Set the endpoint

    # Setup our own namespace, not really necessary but should as spec
    uri = ""
    idx = server.register_namespace(uri)

    # Create a new node directly organized under the root node
    myobj = server.nodes.objects.add_object(idx, "")
    myvar = myobj.add_variable(idx, "", 6.7)

    myvar.set_writable()  # Set MyVariable to be writable by clients

    server.start()
    try:
        while True:
            time.sleep(1)
    finally:
        server.stop()
