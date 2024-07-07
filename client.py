class Client:
    def __init__(self, server_ip):
        self.server_ip = server_ip
    
    def connect_to_server(self):
        print(f"Connecting to server at {self.server_ip}")
