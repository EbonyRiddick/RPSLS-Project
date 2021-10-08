from human import Human
from ai import AI
import random

human_1 = Human()
human_1.gestures_list
for gesture in human_1.gestures_list:
    print(gesture)


human_1.choose_gesture()

computer = AI()
computer.gestures_list


computer.choose_gesture()
print(random.choice(computer.gestures_list))