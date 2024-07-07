import yaml

class Client:
    def __init__(self):
        with open("../config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
            self.server_ip = config["ServerIPAddress"]
    
    def connect_to_server(self):
        print(f"Connecting to server at {self.server_ip}")
