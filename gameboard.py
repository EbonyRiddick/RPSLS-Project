from human import Human

human_1 = Human()
human_1.gestures_list
for gesture in human_1.gestures_list:
    print(gesture)


human_1.choose_gesture()