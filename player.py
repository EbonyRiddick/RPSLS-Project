class Player:
    def __init__(self):
        self.gestures_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.player_score = 0

    def choose_gesture(self):
        self.gestures = input("Choose your gesture!\n1 for Rock \n2 for Paper \n3 for Scissors \n4 for Lizard \n5 for Spock.\n")
 
