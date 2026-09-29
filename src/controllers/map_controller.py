import game_events
import pygame
import events


class MapController:

    SPEED = 150

    def __init__(self, ev_manager):

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)

    def notify(self, event):
        match event:
            case events.TickEvent():
                keys = pygame.key.get_pressed()
                vel_dx = (keys[pygame.K_d] - keys[pygame.K_a]) * self.SPEED * event.dt
                vel_dy = (keys[pygame.K_s] - keys[pygame.K_w]) * self.SPEED * event.dt

                if vel_dx or vel_dy:
                    self.ev_manager.post(game_events.MapMoveEvent(vel_dx, vel_dy))
