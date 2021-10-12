from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        chosen_gesture = random.choice(self.gestures_list)
        self.gestures = chosen_gesture
        print(f'{self.name} has chosen {chosen_gesture}')
       



