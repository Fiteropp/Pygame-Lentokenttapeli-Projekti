import yoyo
from dotenv import load_dotenv
from os import getenv

import events

load_dotenv()

class yoyoConnection:

    def __init__(self, ev_manager):
        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)

    def notify(self, event):
        match event:
            case events.DBConnect(True):
                self.yoyo_connection()


    def yoyo_connection(self):

        try:
            host = getenv("DB_HOST")
            port = getenv("DB_PORT")
            user = getenv("DB_USER")
            password = getenv("DB_PASSWORD")
            database = getenv("DB_NAME")

            database_string = f"mysql://{user}:{password}@{host}:{port}/{database}"

            self.backend = yoyo.get_backend(database_string)
            self.migrations = yoyo.read_migrations("migrations")           

            event = events.yoyoIsConnected(True)
            
        except Exception as error:
            print (f"yoyo database operation failed: {error}")
            event = events.yoyoIsConnected(False)

        self.ev_manager.post(event)
