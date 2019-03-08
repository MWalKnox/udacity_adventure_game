import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause("Hello and welcome to our newest adventure game!")
    print_pause("You're standing in the center of a large room.")
    print_pause("The door behind you is clearly marked as an exit, but it is locked.")
    print_pause("The goal of this game is to collect all three keys to create the master key and escape through the exit.")

def first_room(items):
    print_pause("You turn right and walk with caution into the first room.")
    print_pause("A silver lockbox on the bookshelf catches your attention.")
    if "silver key" in items:
        print_pause("You already have the silver key. Try another room.")
    else:
        print_pause("You walk back to the large room and find a silver key hanging on the wall.")
        items.append("silver key")
        print_pause("You walk back to the first room to unlock the small silver lockbox.")
    get_key(items)

def second_room(items):
    print_pause("You turn left and walk with caution into the second room.")
    print_pause("You notice a bronze chest in the corner of the room.")
    if "bronze key" in items:
        print_pause("You already have the bronze key. Try another room.")
    else:
        print_pause("You walk back to the large room to find a bronze key lying under the potted plant.")
        items.append("bronze key")
        print_pause("You walk back to the second room to unlock the bronze chest.")
    get_key(items)

def third_room(items):
    print_pause("You walk through the hallway and into the third room.")
    print_pause("A gold treasure chest on the coffee table catches your attention.")
    if "gold key" in items:
        print_pause("You already have the gold key.")
    else:
        print_pause("You walk back to the large room to find a gold key beside the welcome mat.")
        items.append("gold key")
        print_pause("You walk through the hallway and back into the third room to unlock the gold treasure chest.")
    get_key(items)

def leave_building(items):
    print_pause("You may only unlock this door if you have collected all 3 keys and created the master key.")
    if "silver key" in items:
        print_pause("You have the silver key!")
    if "bronze key" in items:
        print_pause("You have the bronze key!")
    if "gold key" in items:
        print_pause("You have the gold key!")

        print_pause("You create the master key, unlock the master lock and successfully escape!")
    else:
        print_pause("I'm sorry you have not collected all three keys!")
        get_key(items)

def get_key(items):
    print_pause("Which way do we need to go? You may go to the right, left, or straight ahead.")
    print_pause("If you've collected all three keys, you may unlock the exit door.")
    room = input("Right?\n"
		 "Left?\n"
		 "Straight?\n"
                 "escape\n")
    if room == 'right':
        first_room(items)
    elif room == 'left':
        second_room(items)
    elif room == 'straight':
        third_room(items)
    elif room == 'escape':
        leave_building(items)
    else:
        print_pause("I'm sorry, that is not an option at this time.")
        get_key(items)

def play_game():
    items = []
    intro()
    get_key(items)

play_game()
