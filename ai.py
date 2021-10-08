from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.gestures = random.choice(self.gestures_list)

