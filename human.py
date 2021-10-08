from player import Player

class Human(Player):
    def __init__(self):
        self.name = ''
        super().__init__()

    def set_name(self):
        self.name = input("Assign player name")
        print(f'You have chosen {self.name}!')

    def choose_gesture(self):
        self.gestures = input("Choose your gesture!\n1 for Rock \n2 for Paper \n3 for Scissors \n4 for Lizard \n5 for Spock.\n")

