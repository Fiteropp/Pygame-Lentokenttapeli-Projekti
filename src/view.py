import pygame

import events


class Graphics:
    """
    Draws the model state onto the screen
    """

    def __init__(self, ev_manager, model, scene_manager):
        """

        :param ev_manager:  Allows posting messages to the event queue.
        :param model: a strong reference to the game Model.

        is_initialized (bool): pygame is ready to draw.
        screen (pygame.Surface): pygame screen object.
        clock (pygame.time.Clock): keeps the fps constant.
        small_font (pygame.font.Font): pygame font object.

        """

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)
        self.model = model
        self.is_initialized = False
        self.screen = None
        self.vsync_fps = 0
        self.clock = None
        self.small_font = None
        self.scene_manager = scene_manager


    def  notify(self, event):
        """
        Recieves events from the event queue.

        :param self:
        :param event:
        :return:
        """
        match event:
            case events.InitializeEvent():
                self.initialize()

            case events.QuitEvent():
                # Shut down graphics
                self.is_initialized = False
                pygame.quit()

            case events.TickEvent():
                if not self.is_initialized:
                    return
                self.renderall()

                assert self.clock is not None
                self.clock.tick(self.vsync_fps)  # Limits fps to 60


    def renderall(self):
        """
        Draw the current game state on the screen.
        Not run if is_initialized == False
        """

        assert self.screen is not None
        self.screen.fill((0, 0, 0))
        if self.scene_manager.current is not None:
            self.scene_manager.current.draw(self.screen)
        pygame.display.flip()


    def initialize(self):
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption("Airport Game")
        self.screen = pygame.display.set_mode((1200, 900))
        self.clock = pygame.time.Clock()
        self.is_initialized = True
        self.ev_manager.post(
            events.PygameReadyEvent()
        )
