from human import Human
from ai import AI

human_1 = Human()
computer_1 = AI()
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




    # Display welcome
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

    # Choose your name
    

    


