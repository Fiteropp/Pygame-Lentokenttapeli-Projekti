import pygame

import events
import game_events


class Music:
    DEFAULT_VOLUME = 0.7

    def __init__(self, assets, ev_manager):
        self.assets = assets
        self.muted = False
        self.current_track = None

        self.ev_manager = ev_manager
        ev_manager.register_listener(self)

    def notify(self, event):
        """
        Receive events posted to the message queue.
        """

        if isinstance(event, events.AssetsReadyEvent):
            self.play("menu-ost")
        if isinstance(event, game_events.SetVolume):
            self.set_volume(event.volume)

    def play(self, track: str = "menu-ost", loops: int = -1):
        if not pygame.mixer.get_init():
            return

        path = self.assets.music_path(track)
        if path is None:
            print(f"Warning: no music registered under '{track}'")
            return

        try:
            pygame.mixer.music.load(path)
        except pygame.error as e:
            print(f"Warning: could not load music '{track}': {e}")
            return

        pygame.mixer.music.set_volume(0 if self.muted else self.DEFAULT_VOLUME)
        pygame.mixer.music.play(loops)
        self.current_track = track

    def stop(self):
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
        self.current_track = None

    def mute(self):
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(0)
        self.muted = True

    def set_volume(self, volume):
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(volume)

    def unmute(self):
        if pygame.mixer.get_init():
            pygame.mixer.music.set_volume(self.DEFAULT_VOLUME)
        self.muted = False
