from human import Human
from ai import AI

human_1 = Human()
human_2 = Human()
johnny_5 = AI()
robocop = AI()
# human_1.gestures_list
# for gesture in human_1.gestures_list:
#     print(gesture)
# human_1.choose_gesture()
# # computer_1.choose_gesture()

class Gameboard:
    def __init__(self):
        self.game_mode = ''

    def run_games(self):
        self.display_welcome()
        self.set_game_mode()
        if self.game_mode == 'hvh':
            human_1.set_name()
            human_2.set_name()
            print(f"Get ready to rumble {human_1.name} and {human_2.name}!")
        elif self.game_mode == 'hva':
            human_1.set_name()
            print(f"Get ready to rumble {human_1.name} and {johnny_5}!")
        elif self.game_mode == 'ava':
            print(f"Get ready to rumble {johnny_5} and {robocop}!")
    

    
    def human_1_turn(self):
        Human.choose_gesture()

    def human_2_turn(self):
        Human.choose_gesture()
    
    def johnny_5_turn(self):
        AI.choose_gesture()

    def robocop_turn(self):
        AI.choose_gesture()
    
    def compare_gestures(self):
        pass

    def display_welcome(self):
        print("Welcome to RPSLS!!!")

    # Choose your game mode
    def set_game_mode(self):
        user_input = ''
        while user_input != "1" and user_input != "2" and user_input != "3":
            user_input = input("Press 1 for Human vs Human\nPress 2 for Human vs AI\nPress 3 for AI vs AI.")
            if user_input == "1":
                print("You have chosen Human vs Human!")
                self.game_mode = 'hvh'
            elif user_input == "2":
                print("You have chosen Human vs AI!")
                self.game_mode = 'hva'
            elif user_input == "3":
                print("You have chosen AI vs AI!")
                self.game_mode = 'ava'
            else:
                print("Choose Again")

    
    

    


