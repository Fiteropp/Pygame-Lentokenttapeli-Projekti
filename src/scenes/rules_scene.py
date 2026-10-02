import pygame
import game_events
from scenes import Scene
from ui.elements import Button, Text


class RulesScene(Scene):
    def __init__(self, ev_manager, ui_manager, assets):
        super().__init__(ev_manager, ui_manager, assets)

    def enter(self):
        self.title = Text(
            pygame.Rect(0, 60, 1200, 80),
            fontsize=50,
            fontcolor=(230, 180, 70),
            text="AFRIKAN TÄHTI - PELIN SÄÄNNÖT"
        )
        self.elements.append(self.title)

        self.rule1 = Text(
            pygame.Rect(100, 160, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="1. Matkusta lentokenttien välillä ja etsi Afrikan tähti."
        )
        self.elements.append(self.rule1)

        self.rule2 = Text(
            pygame.Rect(100, 200, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="2. Vie Afrikan tähti Kairoon tai Tangeriin voittaaksesi."
        )
        self.elements.append(self.rule2)

        self.rule3 = Text(
            pygame.Rect(100, 240, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="3. Heitä noppaa jokaisella vuorolla ja liiku kartalla."
        )
        self.elements.append(self.rule3)

        self.rule4 = Text(
            pygame.Rect(100, 280, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="4. Lentokentällä voit maksaa kiekon avaamisesta."
        )
        self.elements.append(self.rule4)

        self.rule5 = Text(
            pygame.Rect(100, 320, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="5. Afrikan tähti = 1000 £"
        )
        self.elements.append(self.rule5)

        self.rule6 = Text(
            pygame.Rect(100, 360, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="6. Hopeinen haalari = 500 £"
        )
        self.elements.append(self.rule6)

        self.rule7 = Text(
            pygame.Rect(100, 400, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="7. Puinen haalari = 300 £"
        )
        self.elements.append(self.rule7)

        self.rule8 = Text(
            pygame.Rect(100, 440, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="8. Huijari vie kaikki rahasi."
        )
        self.elements.append(self.rule8)

        self.rule9 = Text(
            pygame.Rect(100, 480, 1000, 40),
            fontsize=24,
            fontcolor=(255, 255, 255),
            text="9. Onnen merkin löytäjä voi voittaa ehtimällä kaupunkiin ensin."
        )
        self.elements.append(self.rule9)

        self.back_button = Button(
            pygame.Rect(500, 600, 240, 60),
            callback=lambda: self.ev_manager.post(
                game_events.ChangeSceneEvent("menu")
            ),
            text="Back",
            font=self.assets.font("default"),
            color=(75, 45, 25),
            hover_color=(170, 125, 45)
        )
        self.elements.append(self.back_button)

        super().enter()