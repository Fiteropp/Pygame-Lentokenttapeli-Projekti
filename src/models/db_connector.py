import mariadb
from dotenv import load_dotenv
from os import getenv

import events

load_dotenv()

class DBConnector:
    def __init__(self, ev_manager):
        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)


    def notify(self, event):
        match event:
            case events.PygameReadyEvent():
                print("Checking for connection...")
                self.is_connected()
                
            


    def is_connected(self):
        if getenv("DEBUG") == "TRUE":
            return

        try:
            connection = mariadb.connect(
                host=getenv("HOST"),
                port=getenv("PORT"),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
                database=getenv("DATABASE"),
            )

            event = events.DBConnect(True)
        
        except mariadb.Error as error:
            
            print(f"MariaDB error: {error}")
            event = events.DBConnect(False)
            event = events.DatabaseConnectionFailed(True)

        self.ev_manager.post(event)


