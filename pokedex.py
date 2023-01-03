# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Jay Forbes
# Last Modified: 10/17/17 
# ---------------------------------------
# This is a program to access information about the pokemon registered to the pokedex.  You can search by name, the number on catagorized list, or
# just read over the whole pokedex.  In addition we can get infomation about how many pokemon are in the pokedex and the total hitpoints of all the
# registered pokemon.
# ---------------------------------------
import string

def printMenu():
    print("1. Print Pokedex")
    print("2. Lookup Pokemon by Name")
    print("3. Lookup Pokemon by Number")
    print("4. Print Number of Pokemon")
    print("5. Print Total Hit Points of All Pokemon")
    print("6. Quit")
    print()

# List all availble pokemon in pokedex
def printPokedex(pokedex):
    print("The Pokedex")
    for key, value in pokedex.items():
        print("-----------")
        if len(value) == 3: # differentiates the values that have 3 elements compared to 4
            print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]))
        else:
            print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]) + " and " + str(value[3]))
    print("-----------")
    print()
    
# Get info for a pokemon given a name
def lookupByName(pokedex, name):
    i = 0
    for key, value in pokedex.items():
        if name == value[0]:
            if len(value) == 3:
                print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]))
                i += 1
            else:
                print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]) + " and " + str(value[3]))
                i += 1
        else:
            if i == 0:
                print("That is not a valid pokemon.")
                i += 1
    print()

# Get info for a pokemon based on number in list
def lookupByNumber(pokedex, number):
    i = 0
    for key, value in pokedex.items():
        if key == number:
            if len(value) == 3:
                print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]))
                i += 1
            else:
                print("Number:" + str(key) + ", Name: " + str(value[0]) + ", HP: " + str(value[1]) + ", Type: " + str(value[2]) + " and " + str(value[3]))
                i += 1
        else:
            if i == 0:
                print("That is not a valid pokemon.")
                i += 1
    print()

# Figure out how many pokemon there are
def howManyPokemon(pokedex):
    print("There are " + str(len(pokedex)) + " different Pokemon.")
    print()

# Total Hit points for all pokemon
def howManyHitPoints(pokedex):
    r = 0
    for key, value in pokedex.items():
        r += value[1]
    print("The total number of hit points for all the Pokemon is " + str(r))
    print()
        
        

# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        print(pokelist)
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

def getChoice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
