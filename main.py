print("Welcome to the Ancient Adventure Game!")
print("As an traveler, you have decided to visit the Catacombs of King Tut.")
print("However, during your exploration, you fell down a trap and got stuck.")
print("You can choose to walk in different directions to find a way out.")
print("Let's start with your name: ")
name = input()
print("Good luck, " +name+ ".")
print("There are 3 paths which one do you go down?")
directions = ["Left","Right","Forward"]
print("Options: Left/Right/Forward")
Choice = input()
if Choice.lower() == "left" or Choice.lower() == "l":
    print("You advance into the Hall of Appios")
if Choice.lower() == "right" or Choice.lower() == "r":
    print("When you walk you see its a dead end but the wall closed behind you and you starve.")
    import sys
    sys.exit()
if Choice.lower() == "forward" or Choice.lower() == "f":
    print("You were attacked by mummies and died.")
    import sys
    sys.exit()
print("What will you do now?")
directions = ["Search","Right","Forward"]
print("Options: Search/Right/Forward")
Choice2 = input()
if Choice2.lower() == "search" or Choice2.lower() == "s":
    print("There is a sword do you take it?")
    Sword =input()
    if Sword.lower() == "yes" or Sword.lower() == "y":
        print("You pick up the God of Wars Montu's Sword")
if Choice2.lower() == "right" or Choice2.lower() == "r":
    print("You walk and you see a box you go inside and the door closes behind you you open the box and Appios's box of chaos kills you..")
    import sys
    sys.exit()
if Choice2.lower() == "forward" or Choice2.lower() == "f":
    print("You were attacked by skeletons and died.")
    import sys
    sys.exit()

print("What will you do now?")
directions = ["Right","Forward"]
print("Options: Right/Forward")
Choice2 = input()
if Choice2.lower() == "right" or Choice2.lower() == "r":
        print("You walk and you see a box you go inside and the door closes behind you you open the box and Appios's box of chaos kills you.")
        import sys
        sys.exit()
if Choice2.lower() == "forward" or Choice2.lower() == "f":
    if Sword.lower() == "no" or Sword.lower() == "n":
        print("You were attacked by skeletons and died")
    else:
        print("You were attacked by skeletons and you fight them off with your sword.")
        print("You walk through a hall and see a canopic jar room")
        print("You see lung on the table and have to put it in one of the jars.Which one do you put it in?")
        jars = ["Hapy", "Imsety", "Duamutef","Qebehsenuef"]
        print("Options: Hapy/Imsety/Duamutef/Qebehsenuef")
        Choice3 = input()

        if Choice3.lower() == "hapy":
            print("The room rumbles and a door opens")
            print("The next room has two signs that says exit and treasure.Which do you go to?")
            directions = ["treasure", " exit"]
            print("Options: Treasure/Exit")
            Choice4 = input()
            if Choice4.lower() == "treasure" or Choice4.lower == "t":
                print(
                    "You walk and you see a stack of gold you go inside and you trip a tripwire and get shot with arrows and die")
                import sys
                sys.exit()
        if Choice4.lower() == "exit" or Choice4.lower() == "e":
            print("you see a few bars of gold collect them and see light and you escape")
            print("congratulations you won")
            print("You walk out and things look different you ask where you are they say ancient egypt in 3100 B.C.E...TO BE CONTINUED.")



        if Choice3.lower() == "imsety" or Choice3.lower() == "i":
            print("The room fills with gas and you suffocate.")
            import sys
            sys.exit()

        if Choice3.lower() == "duamutef" or Choice3.lower() == "d":
            print("The room fills with gas and you suffocate.")
            import sys
            sys.exit()

        if Choice3.lower() == "qebehsenuef" or Choice3.lower() == "q":
            print("The room fills with gas and you suffocate.")
            import sys
            sys.exit()

