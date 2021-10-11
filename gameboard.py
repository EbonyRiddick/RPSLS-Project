from human import Human
from ai import AI
from player import Player


class Gameboard:
    def __init__(self):
        self.game_mode = ''
        self.player_1 = Player()
        self.player_2 = Player()

    def run_games(self):
        self.display_welcome()
        self.set_game_mode()
        self.initialize_players()
        while self.player_1.player_score < 2 and self.player_2.player_score < 2:
            self.player_1.choose_gesture()
            self.player_2.choose_gesture()

        
    
    def player_1_turn(self):
        self.player_1.choose_gesture()

    def player_2_turn(self):
        self.player_2.choose_gesture()
    
    
    def initialize_players(self):
        if self.game_mode == 'hvh':
            player_1 = Human()
            player_2 = Human()
            player_1.set_name()
            player_2.set_name()
            self.player_1 = player_1
            self.player_2 = player_2
            print(f"Get ready to rumble {player_1.name} and {player_2.name}!")
        elif self.game_mode == 'hva':
            player_1 = Human()
            player_2 = AI()
            player_1.set_name()
            player_2.set_name()
            print(f"Get ready to rumble {player_1.name} and {player_2.name}!")
        elif self.game_mode == 'ava':
            player_1 = AI()
            player_2 = AI()
            player_1.set_name()
            player_2.set_name()
            print(f"Get ready to rumble {player_1.name} and {player_2.name}!")

        
    def compare_gestures(self):
        while self.player_1.gestures == self.player_2.gestures:
            print("IT'S A TIE \nno point awarded try again")
            if self.player_1.gestures == 'rock' and self.player_2.gestures == 'scissors':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'scissors' and self.player_2.gestures == 'paper':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'paper' and self.player_2.gestures == 'rock':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'rock' and self.player_2.gestures == 'lizard':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'lizard' and self.player_2.gestures == 'spock':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures =='spock' and self.player_2.gestures == 'scissors':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'scissors' and self.player_2.gestures == 'lizard':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'lizard' and self.player_2.gestures == 'paper':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'paper' and self.player_2.gestures == 'spock':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            elif self.player_1.gestures == 'spock' and self.player_2.gestures == 'rock':
                self.player_1.player_score += 1
                print(f'{self.player_1.name} gets the point! \n{self.player_1.player_score}')
            else:
                self.player_2.player_score += 1
                print(f'{self.player_2.name} gets the point! \n{self.player_2.player_score}')



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

    
    

    


