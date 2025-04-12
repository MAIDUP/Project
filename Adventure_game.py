def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest with two paths.")
    print("Do you want to go 'left' or 'right'?")
    choice1 = input("> ").lower()
    if choice1 == "left":
        print("\nYou walk down the left path and encounter a river.")
        print("Do you want to 'swim' across or 'build' a raft?")
        choice2 = input("> ").lower()
        if choice2 == "swim":
            print("\nYou decide to swim, but the current is too strong. You drown.")
            print("Game Over.")
        elif choice2 == "build":
            print("\nYou build a raft and safely cross the river.")
            print("On the other side, you find a treasure chest!")
            print("You win!")
        else:
            print("\nInvalid choice. The forest consumes you.")
            print("Game Over.")
    elif choice1 == "right":
        print("\nYou walk down the right path and encounter a sleeping dragon.")
        print("Do you want to 'sneak' past it or try to 'fight' it?")
        choice3 = input("> ").lower()
        if choice3 == "sneak":
            print("\nYou sneak past the dragon successfully.")
            print("You find a hidden cave filled with gold. You win!")
        elif choice3 == "fight":
            print("\nYou try to fight the dragon, but it\'s too strong. You are defeated.")
            print("Game Over.")
        
        else:
            print("\nInvalid choice. The dragon wakes up and devours you.")
            print("Game Over.")
    else:
        print("\nInvalid choice. You wander aimlessly in the forest and are lost.")
        print("Game Over.")
# Start the game
start_game()
