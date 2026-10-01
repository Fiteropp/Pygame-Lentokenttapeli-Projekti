import pygame
import game_events
from controllers.map_controller import MapController
from scenes import Scene
from ui.elements import Button
from ui.map import Map


class GameScene(Scene):
    def __init__(self, ev_manager, ui_manager, assets):
        super().__init__(ev_manager, ui_manager, assets)
        self.map_controller = None
        self.exit_button = None
        self.game_map = None
        self.map_surface = None
        self.map_container = None

    def enter(self):
        if self.exit_button is None:
            self.exit_button = Button(
                pygame.Rect(0, 0, 100, 40),
                callback=lambda: self.ev_manager.post(
                    game_events.ChangeSceneEvent("menu")
                ),
                text="Exit",
                font=self.assets.font("default"),
                z_index=10
            )
            self.elements.append(self.exit_button)

        if self.map_controller is None:
            self.map_controller = MapController(self.ev_manager)

        if self.map_surface is None:
            self.map_surface = pygame.Rect(50, 50, 800, 800)

        if self.map_container is None:
            self.map_container = pygame.Rect(50, 50, 800, 800)

        if self.game_map is None:
            self.game_map = Map(
                rect=self.map_surface,
                z_index=1,
                ev_manager=self.ev_manager,
                color=(20, 100, 0),
                container=self.map_container,
                texture=self.assets.image("map"),
            )
            self.elements.append(self.game_map)

        super().enter()
