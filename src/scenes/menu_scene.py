import events
import game_events
import pygame
from ui.elements import Button
from scenes import Scene


class MenuScene(Scene):
    def __init__(self, ev_manager, ui_manager, assets):
        super().__init__(ev_manager, ui_manager, assets)
        self.start_button = None
        self.exit_game_button = None

    def enter(self):
        if self.start_button is None:
            self.start_button = Button(
                pygame.Rect(500, 300, 200, 50),
                callback=lambda: self.ev_manager.post(
                    game_events.ChangeSceneEvent("game")
                ),
                text="Start",
                font=self.assets.font("default"),
                color=(0, 150, 0),
                hover_color=(0, 180, 0)
            )
            self.elements.append(self.start_button)

        if self.exit_game_button is None:
            self.exit_game_button = Button(
                pygame.Rect(500, 400, 200, 50),
                callback=lambda: self.ev_manager.post(
                    events.QuitEvent()
                ),
                text="Exit Game",
                font=self.assets.font("default"),
            )
            self.elements.append(self.exit_game_button)
        super().enter()
