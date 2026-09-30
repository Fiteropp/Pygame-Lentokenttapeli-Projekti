import mariadb
from dotenv import load_dotenv
from os import getenv

import events

load_dotenv()

class DBConnector:
    def __init__(self, ev_manager):
        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)

        self.is_connected()

    def notify(self, event):
        match event:
            case events.DBConnect(True):
                print("data base is connected: True")
            case events.DBConnect(False):
                print("data base is not connected: False")
            


    def is_connected(self):

        print("Checking database connection...")
        try:
            connection = mariadb.connect(
                host=getenv("HOST"),
                port=int(getenv("PORT")),
                user=getenv("USER"),
                password=getenv("PASSWORD"),
                database=getenv("DATABASE"),
            )

            connection.close()
            event = events.DBConnect(True)
        
        except mariadb.Error:
           event = events.DBConnect(False)

        self.ev_manager.post(event)


