def adventure_game():
    print("Welcome to the Treasure Hunt Adventure!")
    print("You find yourself at the entrance of a mysterious cave rumored to hold great treasure.")
    print("Do you want to ENTER the cave, LOOK around the area, or LEAVE?")
    
    # First level choices
    choice1 = input("Your choice: ").strip().lower()
    if choice1 == "enter":
        print("\nYou step into the dark cave and hear the sound of dripping water.")
        print("You see two paths: a narrow TUNNEL to the left and a wide HALLWAY to the right.")
        print("Which path do you take?")
        
        # Second level choices for "enter"
        choice2 = input("Your choice: ").strip().lower()
        
        if choice2 == "tunnel":
            print("\nThe tunnel is tight, but you manage to squeeze through.")
            print("You find a small chest. Do you OPEN it or IGNORE it?")
            
            # Third level choices for "tunnel"
            choice3 = input("Your choice: ").strip().lower()
            
            if choice3 == "open":
                print("\nInside the chest, you find a sparkling gem!")
                print("Congratulations! You found one of the treasures!")
            elif choice3 == "ignore":
                print("\nYou decide not to take any risks and leave the chest untouched.")
                print("You return to the cave entrance safely.")
            else:
                print("\nInvalid choice. The tunnel collapses, and you must retreat.")
        
        elif choice2 == "hallway":
            print("\nThe hallway opens into a large room filled with ancient statues.")
            print("You notice a SHINY object on the floor and a DOOR at the far end.")
            print("Do you pick up the SHINY object or go through the DOOR?")
            
            # Third level choices for "hallway"
            choice3 = input("Your choice: ").strip().lower()
            
            if choice3 == "shiny":
                print("\nYou pick up the object and realize it’s a golden key!")
                print("This might unlock a hidden treasure somewhere!")
            elif choice3 == "door":
                print("\nYou walk through the door and find a large treasure chest.")
                print("Using the courage you’ve gained, you open it to discover immense riches!")
            else:
                print("\nInvalid choice. A trap is triggered, and you must flee the cave.")
        
        else:
            print("\nInvalid choice. You get lost in the cave and must turn back.")

    elif choice1 == "look":
        print("\nYou look around the area and spot a hidden path behind some bushes.")
        print("Do you FOLLOW the hidden path or RETURN to the cave entrance?")
        
        # Second level choices for "look"
        choice2 = input("Your choice: ").strip().lower()
        
        if choice2 == "follow":
            print("\nThe path leads to an old tree with a strange marking.")
            print("Do you INSPECT the marking or CONTINUE past the tree?")
            
            # Third level choices for "follow"
            choice3 = input("Your choice: ").strip().lower()
            
            if choice3 == "inspect":
                print("\nYou discover a hidden compartment in the tree containing ancient coins!")
                print("Congratulations! You found a secret treasure!")
            elif choice3 == "continue":
                print("\nYou continue down the path and find yourself back at the cave entrance.")
                print("It seems this path was a loop.")
            else:
                print("\nInvalid choice. The path ends abruptly, and you must turn back.")
        
        elif choice2 == "return":
            print("\nYou decide to return to the cave entrance and rethink your choices.")
        else:
            print("\nInvalid choice. You lose your way and end up back at the starting point.")

    elif choice1 == "leave":
        print("\nYou decide not to take any risks and leave the mysterious cave behind.")
        print("Perhaps some other adventurer will uncover its secrets.")
    else:
        print("\nInvalid choice. Please restart the game and try again.")

# Start the game
adventure_game()
