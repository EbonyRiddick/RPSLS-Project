from human import Human
from ai import AI

human_1 = Human()
# human_1.gestures_list
# for gesture in human_1.gestures_list:
#     print(gesture)

# human_1.choose_gesture()



computer_1 = AI()
# computer_1.choose_gesture()


# Display welcome
def display_welcome():
    print("Welcome to RPSLS!!!")

# Choose your game mode
def game_mode():
    input("Press 1 for Human vs Human, press 2 for Human vs AI, press 3 for AI vs AI")
    if input == "1":
        print("You have chosen Human vs Human!")
    elif input == "2":
        print("You have chosen Human vs AI!")
    elif input == "3":
        print("You have chosen AI vs AI!")

# Choose your name
human_1.set_name()


