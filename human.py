from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gestures(self):
        prompt = 'Choose your gesture!\n'
        for gesture in self.gestures_list:
            prompt += (f'{gesture}\n')
        self.gestures = input(prompt).lower()

        while self.gestures not in self.gestures_list:
            print(f"Invalid gesture, please choose again! ")
            self.choose_gestures()



   

