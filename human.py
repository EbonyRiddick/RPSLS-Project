from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gestures(self):
        self.gestures = input("Choose your gesture!\n1 for Rock \n2 for Paper \n3 for Scissors \n4 for Lizard \n5 for Spock.\n")
   
       
    

