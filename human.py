from player import Player

class Human(Player):
    def __init__(self):
        gestures = Player()
        gestures.gestures()
        self.gestures = gestures
        super().__init__()

    def set_name(self):
        self.name = input("Assign player name")
        print(f'You have chosen {self.name}!')

    def choose_gesture(self,gesture):
        self.gestures = input("Choose your gesture!")

