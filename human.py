from player import Player

class Human(Player):
    def __init__(self):
        self.name = ''
        super().__init__()

    def set_name(self):
        self.name = input("Assign player name")
        print(f'You have chosen {self.name}!')

    

