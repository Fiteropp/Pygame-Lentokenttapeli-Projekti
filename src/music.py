import pygame


class Music:
    def __init__(self):
        pygame.mixer.music.load("src/assets/music_OST.mp3")
        self.muted = False

    def play(self):
        pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()

    def mute(self):
        pygame.mixer.music.set_volume(0)
        self.muted = True

    def unmute(self):
        pygame.mixer.music.set_volume(0.5)
        self.muted = False