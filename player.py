class Player:
    def __init__(self):
        self.name = ''
        self.gestures_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.player_score = 0

    def choose_gestures(self):
        self.gestures = ''
        pass
   
    def set_name(self):
        self.name = input("Assign player name")
        print(f'You have chosen {self.name}!')