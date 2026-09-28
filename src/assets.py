import pygame

import events as ev


class Assets:
    """
    Central store for loaded pygame resources (fonts, images, sounds).

    Populated once, in response to InitializeEvent, after pygame.font.init()
    and the display have been set up. Scenes and UI elements read from this
    rather than creating their own resources.
    """

    def __init__(self, ev_manager):
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)

        self.fonts: dict[str, pygame.font.Font] = {}
        self.images: dict[str, pygame.Surface] = {}
        self.is_loaded = False

    def notify(self, event):
        if isinstance(event, ev.PygameReadyEvent):
            self.load()
            self.ev_manager.post(ev.AssetsReadyEvent())

    def load(self):
        """
        Load every shared resource once. Safe to call only after
        pygame.font.init() has run.
        """
        self.fonts["default"] = pygame.font.SysFont("Arial", 20)
        self.fonts["heading"] = pygame.font.SysFont("Arial", 36, bold=True)
        self.fonts["small"] = pygame.font.SysFont("Arial", 14)

        # self.images["logo"] = pygame.image.load("assets/logo.png").convert_alpha()

        self.is_loaded = True

    def font(self, name: str) -> pygame.font.Font:
        """
        Look up a loaded font by name, with a clear error if it's missing
        or requested too early.
        """
        if not self.is_loaded:
            raise RuntimeError("Assets.font() called before InitializeEvent was handled")
        try:
            return self.fonts[name]
        except KeyError:
            raise KeyError(f"No font registered under '{name}'. "
                            f"Available: {list(self.fonts)}") from None
