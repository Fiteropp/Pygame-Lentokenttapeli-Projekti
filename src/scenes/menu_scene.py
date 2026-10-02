import events
import game_events
import pygame
import os
from ui.elements import Button, Text
from scenes import Scene


class MenuScene(Scene):
    def __init__(self, ev_manager, ui_manager, assets):
        super().__init__(ev_manager, ui_manager, assets)
        self.start_button = None
        self.exit_game_button = None
        self.rules_button = None 
        self.title = None
        self.mute_button = None
        self.muted = False

    def enter(self):
        if self.title is None:
            self.title = Text(
                pygame.Rect(0, 150, 1200, 100),
                fontname=None,
                fontsize=60,
                fontcolor=(255, 255,255),
                hover_color=(255, 255,255),
                text="AFRIKAN TÄHTI"
            
            )
            self.elements.append(self.title)

        if self.start_button is None:
            self.start_button = Button(
                pygame.Rect(500, 330, 240, 60),
                callback=lambda: self.ev_manager.post(
                    game_events.ChangeSceneEvent("game")
                ),
                text="Start",
                font=self.assets.font("default"),
                color=(0, 150, 0),
                hover_color=(0, 180, 0)
            )
            self.elements.append(self.start_button)
        
        if self.rules_button is None:
            self.rules_button = Button(
                pygame.Rect(500, 410, 240, 60),
                callback=lambda: self.ev_manager.post(
                    game_events.ChangeSceneEvent("rules")
                    ),
                text="Rules",
                font=self.assets.font("default"),
                color=(75, 45, 25),
                hover_color=(170, 125, 45)
                )
            self.elements.append(self.rules_button)


        if self.exit_game_button is None:
            self.exit_game_button = Button(
                pygame.Rect(500, 490, 240, 60),
                callback=lambda: self.ev_manager.post(
                    events.QuitEvent()
                ),
                text="Exit Game",
                font=self.assets.font("default"),
            )
            self.elements.append(self.exit_game_button)

        if self.mute_button is None:
            self.mute_button = Button(
                pygame.Rect(1100, 0, 100, 60),
                callback= self.toggle_mute,
                text="Mute",
                font=self.assets.font("default"),
                color=(80, 20, 10),
                hover_color=(100, 60, 30)
            )
            self.elements.append(self.mute_button)
        
        super().enter()

    def draw(self, screen):
        background = pygame.transform.scale(self.assets.image("menu-bkg-img"), screen.get_size())
        screen.blit(background, (0, 0))
        super().draw(screen)

    def toggle_mute(self):
        self.muted = not self.muted
        self.ev_manager.post(game_events.SetVolume(0 if self.muted else 0.7))