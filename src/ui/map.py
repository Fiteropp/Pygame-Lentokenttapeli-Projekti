import pygame

import events
import game_events
from ui import UIElement


class Map(UIElement):

    def __init__(self, rect, z_index, ev_manager, color):
        super().__init__(rect, z_index)
        self.ev_manager = ev_manager
        ev_manager.register_listener(self)

        self.color = color
        self.pos_dx = 0.0
        self.pos_dy = 0.0
        self.origin_x = rect.x
        self.origin_y = rect.y
        self.map_surface = rect

    def notify(self, event):
        """
        :param event: Called by an event in the message queue
        """

        match event:
            case game_events.MapMoveEvent():
                self.pos_dx += event.dx
                self.pos_dy += event.dy

                self.map_surface.x = round(self.pos_dx) + self.origin_x
                self.map_surface.y = round(self.pos_dy) + self.origin_y

            case game_events.MapScaleEvent():
                factor = event.zoom

                self.map_surface.scale_by_ip(factor, factor)

            case events.MouseScrollEvent():
                factor = (event.scroll_y + 10) / 10
                print(factor)
                self.map_surface.scale_by_ip(factor, factor)
                print(self.map_surface)

            case game_events.ChangeSceneEvent("game"):
                self.pos_dx = 0.0
                self.pos_dy = 0.0

    def draw(self, screen):
        color = self.color
        pygame.draw.rect(screen, color, self.map_surface)
