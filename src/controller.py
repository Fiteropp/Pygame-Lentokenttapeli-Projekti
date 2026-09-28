import pygame
import events
class Keyboard(object):
    """
    Handles keyboard input.
    """

    def __init__(self, ev_manager, model):
        """
        :param ev_manager (EventManager): Allows posting messages to the event queue.
        :param model (GameEngine): a strong reference to the game Model.
        """
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """

        if isinstance(event, events.TickEvent):
            # Called for each game tick.
            for ev in pygame.event.get():
                # handle window manager closing our window
                if ev.type == pygame.QUIT:
                    self.ev_manager.post(events.QuitEvent())
                    break

                elif ev.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    self.ev_manager.post(events.MouseMoveEvent(pos))

                # Keyboard and Mouse events
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.ev_manager.post(events.QuitEvent())
                        break
                    else:
                        self.ev_manager.post(events.KeyInputEvent(ev.unicode))


                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button in (4, 5):
                        pass
                    elif pygame.mouse.get_focused():
                        mouse_btn = pygame.mouse.get_pressed()
                        mouse_pos = pygame.mouse.get_pos()
                        self.ev_manager.post(events.MouseInputEvent(mouse_pos, mouse_btn))


                elif ev.type == pygame.MOUSEWHEEL:
                    mouse_pos = pygame.mouse.get_pos()
                    self.ev_manager.post(events.MouseScrollEvent(mouse_pos, ev.y))
