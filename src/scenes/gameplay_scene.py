import pygame
import game_events
from scenes import Scene
from ui.elements import Button


class GameScene(Scene):
    def __init__(self, ev_manager, ui_manager, assets):
        super().__init__(ev_manager, ui_manager, assets)
        self.exit_button = None

    def enter(self):
        if self.exit_button is None:
            self.exit_button = Button(
                pygame.Rect(0, 0, 200, 50),
                callback=lambda: self.ev_manager.post(
                    game_events.ChangeSceneEvent("menu")
                ),
                text="Exit",
                font=self.assets.font("default"),
            )
            self.elements.append(self.exit_button)
        super().enter()