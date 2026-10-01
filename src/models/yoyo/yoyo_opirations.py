import events

class yoyoOperations:

    def __init__(self, ev_manager, yoyo_connection):
        self.ev_manager = ev_manager
        self.ev_manager.register_listener(self)
        self.yoyo = yoyo_connection

    def notify(self, event):
        match event:
            case events.yoyoIsConnected(True):
                self.apply_migrations()


    def check_migrations(self):
        pending = list(
            self.yoyo.backend.to_apply(
                self.yoyo.migrations
            )
        )

        event = events.yoyoCheckMigrations(pending)
        self.ev_manager.post(event)

        return pending

    def apply_migrations(self):
        pending = self.check_migrations()

        if not pending:
            print("No pending migrations.")
            event = events.yoyoApplyingMigrations(False)
            return

        try:

            with self.yoyo.backend.lock():
                self.yoyo.backend.apply_migrations(pending)

            print(f"Applied {len(pending)} migrations")
            event = events.yoyoApplyingMigrations(True)

        except Exception as error:
            print(f"Migrations failed - {error}")
            event = events.yoyoApplyingMigrations(False)
        
        self.ev_manager.post(event)
    