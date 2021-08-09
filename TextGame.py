print("Make sure to type help if you're confused on how to play")
print("There are two caves, which one do you go in?")
counter = True
left_cave_input = ""
left_left_cave_input = ""
left_right_cave_input = ""
right_cave_input = ""
right_right_cave_input = ""
while counter:
    choice = input("> ")
    if choice != "L" or "R" or "help":
        print("Remember to type help")
    if choice == "help":
        print("The letters in parentheses can be typed to make decisions")
    if choice == "L":
        print(
            "You narrowly escape a dragons fireball and fall into a pit of treasure. You spot a sword, but also see a glimmer of light through the wall. Do you (T)ake the sword, or try to (C)rawl through the cave?")
        left_cave_input = input("> ")
        if left_cave_input == "T":
            print("The dragon steps on you as you try to fight it. Game Over. Run again to restart, or type Q to quit.")
            left_right_cave_input = input("> ")
            if left_right_cave_input == "Q":
                break
    if left_cave_input == "C":
        print(
            "A boulder comes falling down and crushes you while you try to escape. Game Over. Run again to restart, or type Q to quit.")
        left_left_cave_input = input("> ")
    if left_left_cave_input == "Q":
        break
    if choice == "R":
        print(
            "You find a mysterious black ball filled with a purple substance sitting on a table. Do you (T)ouch the ball, or (E)xit the cave?")
        right_cave_input = input("> ")
        if right_cave_input == "E":
            print(
                "As you exit the ball seems to get mad and sucks you in. You become a god for a brief second before being sent to the desert. Quite sad. Game Over. Run again to restart, or type Q to quit.")
            right_left_cave_input = input("> ")
            if right_left_cave_input == "Q":
                break
        if right_cave_input == "T":
            print(
                "Your mind floods with memories from the past until you black out. You find yourself in antartica. Game Over. Run again to restart, or type Q to quit.")
            right_right_cave_input = input("> ")
            if right_right_cave_input == "Q":
                break
