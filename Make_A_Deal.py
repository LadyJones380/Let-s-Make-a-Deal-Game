# Create a Python program called "Let's Make a Deal" that offers a user to
# keep some quick cash or take a chance and play for the "Big Deal" (which
# allows them to pick what is behind Door #1, Door #2, or Door #3).

# Introduce and Explain the game:

print ("\nWelcome to the game Let's Make a Deal!  Let's play!\n")
print("Here's how it works:\n")
print("You will roll two dice to determine how much quick cash you'll earn.")
print("Next, you get to decide to keep the money or risk it and choose")
print("behind one of three doors!  Each door will have a random")
print("cash amount behind it. Each door may have more, the same or")
print("even less than your quick cash amount.")
print("Okay, ready to test your luck???  Let's go!\n")
      
      
# Import all modules:

import time
import random
import sys

# Set up the roll of the dice:

dice1 = [1,2,3,4,5,6]

dice2 = [1,2,3,4,5,6]

roll1 = random.choice(dice1)

roll2 = random.choice(dice2)

# Prompt the user to roll the dice:

user_roll = input("Press the Enter Key to roll the dice!")

# Tell user what numbers they got from the dice and determine the quick cash
# value based on the die roll:

print("\nYou rolled a", roll1, "and", roll2,)

sum_dice = roll1 + roll2

quick_cash = sum_dice * 100
int(quick_cash)

print("Based on your roll, your total quick cash is $",quick_cash,"\n")

# Prompt user to choose either Quick Cash option or pick a door:

print("Do you want to keep your quick cash or take a chance and risk it?")
user_choice = int(input("Press 1 to keep your quick cash & leave or 2 to take your chances: "))


# While loop denotes an error message if user does not choose 1 or 2. Otherwise, continue on to game play:

while user_choice not in (1, 2):
    print("Sorry, invalid selection.  You must enter 1 or 2.")
    user_choice = int(input("Press 1 to keep your quick cash & leave or 2 to take your chances: "))
else:
    if user_choice==1:
        print("\nCongrats! You get to keep your quick cash of $",quick_cash)
        time.sleep(1)

    elif user_choice==2:

        # First, set up lists for quick cash amounts as low, medium and high:
        
        low_amt = [0.00,0.05,0.15,0.25]
        med_amt = [1.25, 1.50, 1.75, 2.00]
        high_amt = [10.00, 15.00, 20.00, 25.00]
    
        # Second, we want to randomize which amount within the low, medium or high lists
        # will be picked:
        
        random_low_amt = random.choice(low_amt)
        random_med_amt = random.choice(med_amt)
        random_high_amt = random.choice(high_amt)
    
        # Third, we want to create a list of all randomized amounts so we can
        #randomize these in the fourth step:
        
        list_randomized_amt = [random_low_amt, random_med_amt, random_high_amt]

        # Fourth, we are going to randomize the amounts of low medium or high dollar value
        # that shows up behind each door and calculate final cash amount:

        door1 = int(random.choice(list_randomized_amt)) * int(quick_cash)
        door2 = int(random.choice(list_randomized_amt)) * int(quick_cash)
        door3 = int(random.choice(list_randomized_amt)) * int(quick_cash)

        # Prompt the user to pick a door number:

        print("\nOkay, let's pick a door!")
        print("Remember! You may get more cash, the same amount of cash")
        print("or even lose some cash!")
        print("\nSo, let's go! Good luck!")
        door_choice = int(input("\nPick a door number: 1,2, or 3: "))
        
        # While loop denotes an error message if user does not choose 1, 2 or 3. Otherwise, continue on to game play:
        
        while door_choice not in (1, 2, 3):
            print("Sorry, invalid selection. You can only choose 1,2 or 3.")
            door_choice = int(input("\nPick a door number: 1,2, or 3: "))
            
        else:
            if door_choice==1: # Prepare user for game play:
                print("\nOkay, let's play for the Big Deal!")
                user_continue = input("\nAre you ready? Hit Enter when ready...")
                print("\nOkay, here we go...")
                time.sleep(3)    

                if door2 < door3: # Show the smallest amount of the 2 doors not picked:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 2 for $",door2)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 1 for $",door1)
                    time.sleep(3)
                    print("\nAnd finally, Door 3 had $",door3)
                    time.sleep(3)
                elif door2 == door3:
                    print("\nBoth Door 2 and Door 3 had the same amount!")
                    time.sleep(3)
                    print("\nDoor 2 was $",door2,"and Door 3 was $",door3)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 1 for $",door1)
                    time.sleep(3)
                else:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 3 for $",door3)
                    time.sleep(3)
                    user = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou Picked Door 1 for $",door1)
                    time.sleep(3)
                    print("\nAnd finally, Door 2 had $",door2)
                    time.sleep(3)
                
                if door1 < quick_cash: # Show user how much they lost or gained from picking Door 2 over quick cash option:
                    losing1_amt = quick_cash - door1
                    print("\nOoh, sorry you lost $",losing1_amt,"to the deal!")
                    print("But thanks for trying!")
                    time.sleep(1)
                elif door1 == quick_cash:
                    print("\nYou made out even with $",door1,"not bad!")
                    time.sleep(1)
                else:
                    winning1_amt = door1 - quick_cash
                    print("\nNice!! You got an extra $",winning1_amt,"from the deal!")
                    print("Congratulations!!")
                    time.sleep(1)
                    
                    
            elif door_choice==2: # Prepare user for game play:
                print("\nOkay, let's do the Big Reveal...")
                user_continue = input("\nAre you ready? Hit Enter when ready...")
                print("\nOkay, here we go...")
                time.sleep(3)    

                if door1 < door3: # Show the smallest amount of the 2 doors not picked:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 1 for $",door1)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 2 for $",door2)
                    time.sleep(3)
                    print("\nAnd finally, Door 3 had $",door3)
                    time.sleep(3)
                elif door1 == door3:
                    print("\nBoth Door 1 and Door 3 had the same amount!")
                    time.sleep(3)
                    print("\nDoor 1 was $",door1,"and Door 3 was $",door3)
                    time.sleep(3)
                    user = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 2 for $",door2)
                    time.sleep(3)
                else:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 3 for $",door3)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou Picked Door 2 for $",door2)
                    time.sleep(3)
                    print("\nAnd finally, Door 1 had $", door1)
                    time.sleep(3)
                
                if door2 < quick_cash: # Show user how much they lost or gained from picking Door 2 over quick cash option:
                    losing2_amt = quick_cash - door2
                    print("\nOoh, sorry you lost $",losing2_amt,"to the deal!")
                    print("But thanks for trying!")
                    time.sleep(1)
                elif door2 == quick_cash:
                    print("\nYou made out even with $", door2,"not bad!")
                    time.sleep(1)
                else:
                    winning2_amt = door2 - quick_cash
                    print("\nNice!! You got an extra $",winning2_amt,"from the deal!")
                    print("Congratulations!!")
                    time.sleep(1)
                    
            elif door_choice==3: # Prepare user for game play:
                print("\nOkay, let's do the Big Reveal...")
                user_continue = input("\nAre you ready? Hit Enter when ready...")
                print("\nOkay, here we go...")
                time.sleep(3)    

                if door2 < door1: # Show the smallest amount of the 2 doors not picked:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 2 for $",door2)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 3 for $",door3)
                    time.sleep(3)
                    print("\nAnd finally, Door 1 had $",door1)
                    time.sleep(3)
                elif door2 == door1:
                    print("\nBoth Door 2 and Door 1 had the same amount!")
                    time.sleep(3)
                    print("\nDoor 2 was $",door2,"and Door 1 was $",door1)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou picked Door 3 for $",door3)
                    time.sleep(3)
                else:
                    print("\nThe door with the smallest amount between the doors not picked is...")
                    time.sleep(3)
                    print("\nDoor 1 for $",door1)
                    time.sleep(3)
                    show = input("\nIf you're ready, hit Enter to see your door...")
                    time.sleep(3)
                    print("\nYou Picked Door 3 for $",door3)
                    time.sleep(3)
                    print("\nAnd finally, Door 2 had $", door2)
                    time.sleep(3)

                if door3 < quick_cash: # Show user how much they lost or gained from picking Door 3 over quick cash option:
                    losing3_amt = quick_cash - door3
                    print("\nOoh sorry! You lost $",losing3_amt,"to the deal!")
                    print("But thanks for trying!")
                    time.sleep(1)
                elif door3 == quick_cash:
                    print("\nYou made out even with $",door3,"not bad!")
                    time.sleep(1)
                else:
                    winning3_amt = door3 - quick_cash
                    print("\nNice!! You got an extra $",winning3_amt,"from the deal!")
                    print("Congratulations!!")
                    time.sleep(1)

# End of game message:

print("\nThank you for playing! Have a great day!")

# Explain how the program could be enhanced:
# 1. Adding graphics to the whole game.
# 2. Adding music (similar to Jeopardy) to play when the user is waiting for their door.
# 3. Adding spinning wheel graphics or some time of waiting icon while the user is waiting.
# 4. Add more chances to win by adding more doors.

# What type of error handling could be incorporated into the program?
# 1. If user doesn't hit enter, let them know they hit the wrong key and to
# just hit enter.
# 2. Incorporating try to test blocks of code and possibly printing out
# exception errors.
# 3. Use logging through logger.exception to log error messages.


            
    
    
    
    
                  









