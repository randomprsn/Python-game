#!/usr/bin/python


# IMPORTS
import random
import time
from random import randint

#ENEMY ATTRIBUTES
enemies = ["Skeleton","Zombie","Warrior","Ogre"]
maxEnemyHealth = 75
enemyAttackDamage = 25

#PLAYER
playerHealth = 100
attackDamage = 50
numHealthPotions = 3



#FUNCTIONS

def cls():
    print("\n" * 100)

def start_game():
    start_room_options = ["1","2"]
    user_choice=""
    while user_choice not in start_room_options:
        cls()
        print("You awake and emerge from your tent. After days of searching, you have found the cave the crazy drunk at "
              "the tavern told you about. What do you do?\n"
              "1) Enter the cave\n"
              "2) Nah, let's go home.\n")

        user_choice = str(input("Enter your choice: \n"))
    if user_choice == start_room_options[0]:
        brave()
    elif user_choice == start_room_options[1]:
        chicken()


def brave():
    print("\n\n You enter the cave.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    battle()

def chicken():
    print("\n\n You chicken out and head back home with your head hung low.")

def battle():

    cls()
    enemy = random.choice(enemies)
    print("A " + enemy + " appears!\n")



    global playerHealth
    enemyHealth = random.randint(1,maxEnemyHealth)

    while enemyHealth >= 1:
        print("Your HP: " + str(playerHealth) + "\n"
          "Enemy HP: " + str(enemyHealth) + "\n")
        combatchoice = ["1", "2", "3"]
        user_choice = ""
        print("What do you do?\n"
          "1) Attack!\n"
          "2) Drink health potion.\n"
          "3) Run away!\n")
        user_choice = str(input("Enter your choice: \n"))
        if user_choice == combatchoice[0]:
            print("You swing your sword at the " +enemy)
            print("\n")
            damageDealt = random.randint(0,attackDamage)
            damageTaken = random.randint(0,enemyAttackDamage)
            enemyHealth -= damageDealt
            if enemyHealth > 1:
                playerHealth -= damageTaken
                print("You take " + str(damageTaken) + " damage from the " + enemy)
            print("You slash your foe for " + str(damageDealt) + " damage!\n")
            print("\n")
        if playerHealth < 1:
                print("You have been torn apart by your foe.\n")
                print("----- GAME OVER -----")
                break
        elif enemyHealth < 1:
                print("You have slain the " +enemy)
                presson()
        elif user_choice == combatchoice[1]:
            global numHealthPotions
            if numHealthPotions >= 1:
                numHealthPotions -= 1
                playerHealth += 50
                print ("You drink a potion and heal yourself for 50 HP.\n"
                       "You now have " + str(numHealthPotions) + " left.\n")
            elif numHealthPotions < 1:
                print("You don't have any potions left!")
        elif user_choice == combatchoice[2]:
            print("Running away!")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("You successfully elude the " +str(enemy))
            time.sleep(3)
            ranaway()
            break


def presson():
    pathchoice = ["1","2"]
    print("Do you wish to continue through the cave?\n"
          "1) Yes\n"
          "2) No\n")
    user_choice = str(input("Enter your choice: "))
    if user_choice == pathchoice[0]:
        print("You continue deeper into the cave.\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(3)
        battle()
    elif user_choice == pathchoice[1]:
        print("You exit the cave and prepare to head back to town to tell the old drunk about your journey.")

def ranaway():
    cls()
    pathchoice = ["1","2"]
    print("Out of breath, you check your backpack to check your supplies.\n"
          "You have " + str(numHealthPotions) + " health potions left.\n"
          "Your HP: " + str(playerHealth) + "\n"
          "What would you like to do?\n"
          "1) Continue through the cave.\n"
          "2) Leave the cave.\n")
    user_choice = str(input("Enter your choice: "))
    if user_choice == pathchoice[0]:
        print("You muster up some courage and continue into the cave.\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(3)
        battle()
    elif user_choice == pathchoice[1]:
        print("With a heavy sigh, you put sling you backpack around your shoulder and exit the cave "
              "vowing to never return.\n")




# MAIN
start_game()