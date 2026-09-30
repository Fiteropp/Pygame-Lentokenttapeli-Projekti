import pygame

import events as ev


class Engine:
    """
    Tracks the game state
    """

    def __init__(self, ev_manager):
        """
        :param ev_manager:  Allows posting messages to the event queue.
        """

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.running = False
        self.target_fps = 60

    def notify(self, event):
        """
        :param event: Called by an event in the message queue
        """

        if isinstance(event, ev.QuitEvent):
            self.running = False
        elif isinstance(event, ev.PygameReadyEvent):
            self.target_fps = event.refresh_rate

    def run(self):
        """
        Starts the game engine loop.

        This creates a Tick event ino the message queue for each loop.
        The loop ends when this object receives a QuitEvent in notify().
        """

        self.running = True
        self.ev_manager.post(ev.InitializeEvent())
        clock = pygame.time.Clock()

        while self.running:
            dt =  clock.tick(self.target_fps) / 1000.0
            self.ev_manager.post(ev.TickEvent(dt))

        pygame.quit()
