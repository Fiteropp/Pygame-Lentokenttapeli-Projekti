import events as ev


class Engine:
    """
    Tracks the game state
    """

    def __init__(self, ev_manager):
        """
        :param ev_manager  Allows posting messages to the event queue.
        """

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.running = False

    def notify(self, event):
        """
        :param event: Called by an event in the message queue
        """

        if isinstance(event, ev.QuitEvent):
            self.running = False

    def run(self):
        """
        Starts the game engine loop.

        This creates a Tick event ino the message queue for each loop.
        The loop ends when this object receives a QuitEvent in notify().
        """

        self.running = True
        self.ev_manager.post(ev.InitializeEvent())
        while self.running:
            new_tick = ev.TickEvent()
            self.ev_manager.post(new_tick)

