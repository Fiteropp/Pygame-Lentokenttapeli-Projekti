import pygame
import game_events
import events
from ui import UIElement


import pygame


class Button(UIElement):
           
    """
    A clickable, hoverable rectangular UI element with optional text.
    """

    def __init__(self, rect, callback=None, z_index=0,
                 color=(70, 70, 70), hover_color=(100, 100, 100),
                 text=None, font=None, text_color=(255, 255, 255)):
        super().__init__(rect, z_index)
        self.callback = callback
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.highlighted = False

    def draw(self, screen):
        color = self.hover_color if self.highlighted else self.color
        pygame.draw.rect(screen, color, self.rect)

        if self.text and self.font:
            words = self.font.render(self.text, True, self.text_color)
            text_rect = words.get_rect(center=self.rect.center)
            screen.blit(words, text_rect)

    def on_hover_start(self):
        self.highlighted = True

    def on_hover_end(self):
        self.highlighted = False

    def on_click(self):
        if self.callback is not None:
            self.callback()

class Text(UIElement):

    """
    Defines the text inside Button
    """
    def __init__ (self, rect, z_index=0, fontname = None, fontsize = 40, fontcolor = (255,255,255), hover_color=(100,100,100),text = None ):
        super(). __init__(rect, z_index)
        self.fontname = fontname
        self.fontsize = fontsize 
        self.fontcolor = fontcolor
        self.hover_color = hover_color
        self.text = text
        self.highlighted = False

    def draw(self, screen):
        font = pygame.font.Font(self.fontname, self.fontsize)
        color = self.hover_color if self.highlighted else self.fontcolor
        words = font.render(self.text, True, color)

        text_rect = words.get_rect(center=self.rect.center)
        screen.blit(words, text_rect)

    def on_hover_start(self):
        self.highlighted = True

    def on_hover_end(self):
        self.highlighted = False
    





