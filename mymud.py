#######################################################################
# My MUD                                                              #
# I need to create the pseudocode, and then create classes, basically #
# transition my original code into OOP                                #
#                                                                     #
# I will do my best to keep everything well documented.               #
# This is the only project I need to be concerned with at the moment. #
#######################################################################

"""
Include 9 rooms as follows:

    A1==A2==A3      Each room will be its own class interation.
    ||  ||  ||      The player will be a class interation.
    B1==B2==B3      Each item will be a class interation.
    ||  ||  ||
    C1==C2==C3
"""

# Module imports
from sys import exit
from random import randint
import os


# Create Player class here
class Player(object):
    
    health = 30
    gold = 0
    def __init__(self, name):
        self.name = name

    # Shows your inventory        
    def show_inventory(self):
        
        os.system('clear')
        
        print "%s's Inventory:\n" % self.name
        print "You have %i gold.\n" % self.gold
        print "You have %i HP.\n" % self.health
        
        raw_input("<Press Enter to Continue>")
        

# Create DeathSequence class here
class DeathSequence(object):
	
	def enter(self):
	    print "You have died...\n"
	    exit()


# Create CombatSequence class here
class CombatSequence(object):

	hp = 10
	dmg = 1
	
	def random_spawn(self):
	    random_chance = randint(0, 9)
	    if random_chance > 4:
		self.enter()
	    else:
		pass


	def enter(self):
	    os.system('clear')
	    print "An enemy approaches...\n"
	    print "Fight(f) Escape(e):\n"
	    choice = raw_input("> ")
	    if choice == "f":
		self.attack_sequence()
	    elif choice == "e":
		self.run_away()	

	def attack_sequence(self):
	    
	    while hero.health > 0 and self.hp > 0:
		os.system('clear')
		print "%s HP: %i    Enemy HP: %i\n" % (hero.name, hero.health, self.hp)
		print "Attack(a) Escape(e):\n"
		choice = raw_input("> ")
		
		if choice == "a":
		    os.system('clear')
		    attack_dmg = randint(0, 4)
		    print "Attacking enemy for %i damage!\n" % attack_dmg	
	            self.hp -= attack_dmg
		    print "Enemy HP: %i\n" % self.hp
		
		    if self.hp <= 0:
		        print "Enemy Slain!\n"
		        loot = randint(1, 4)
		        print "You get %i gold\n" % loot
		        hero.gold += loot
			raw_input("<Press Enter to Continue>")
	    	
		    else:
		        print "Enemy is attacking you for %i damage!\n" % self.dmg
		        hero.health -= self.dmg
			if hero.health <= 0:
			    dead.enter()
			else:
			    print "%s HP: %i\n" % (hero.name, hero.health)
			    raw_input("<Press Enter to Continue>")

		elif choice == "e":
		    self.run_away()
		    break

	def run_away(self):
	    print "You run away!"

# Create Shop class here
class Shop(object):
    
    def display_wares(self):
	
	os.system('clear')
	
	print "Welcome to the Shop!"
	print "You have %i gold.\n" % hero.gold
	print "You have %i HP.\n" % hero.health
	print "----------Items for Sale---------"
	print "(1) Small health potion...3 gold"
	print "(2) Large health potion...5 gold"
	print "---------------------------------"
	print "(3) Leave the shop"

    def enter(self):

        done = False

	while done == False:  
	    self.display_wares()

            choice = raw_input("> ")

	    if choice == "1" and hero.gold >= 3:

		if hero.health > 25:
		    hero.health = 30
		    hero.gold -= 3
		    print "HP Full!\n"

		    raw_input("<Press Enter to Continue>")

		else:
		    hero.health += 5
		    hero.gold -= 3

		    if hero.health == 30:
			print "HP full!\n"

			raw_input("<Press Enter to Continue>")

		    else:
			print "+5 HP!\nHP: %i\n" % hero.health

			raw_input("<Press Enter to Continue>")

	    elif choice == "2" and hero.gold >= 5:

		if hero.health > 20:
		    hero.health = 30
		    hero.gold -= 5
		    print "HP Full!\n"

		    raw_input("<Press Enter to Continue>")

	    	else:
		    hero.health += 10
		    hero.gold -= 5
		    print "+10 HP!\nHP: %i\n" % hero.health

		    raw_input("<Press Enter to Continue>")

	    elif choice == "1" and hero.gold < 3:
		print "Not enough gold!"

		raw_input("<Press Enter to Continue>")

	    elif choice == "2" and hero.gold < 5:
		print "Not enough gold!"

		raw_input("<Press Enter to Continue>")
           
	    elif choice == "3":
		done = True

	    else:
		print "Invalid option!"

		raw_input("<Press Enter to Continue>")

# Create RoomA1(Room) class here
class RoomA1(object):
 
    def description(self):
        os.system('clear')
        print "This is room A1"
        print "Directions: DOWN(s), RIGHT(d)"
        
    def enter(self):
	combat = CombatSequence()
	combat.random_spawn()
        self.description()

	choice = raw_input("> ")

        if choice == "s":
            room_B1.enter()

        elif choice == "d":
            room_A2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_A1.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_A1.enter()



# Create RoomA2(Room) class here
class RoomA2(object):
 
    def description(self):
        os.system('clear')
        print "This is room A2"
        print "Directions: DOWN(s), LEFT(a), RIGHT(d)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

        if choice == "s":
            os.system('clear')
            room_B2.enter()

        elif choice == "a":
            os.system('clear')
            room_A1.enter()

        elif choice == "d":
            os.system('clear')
            room_A3.enter()

	elif choice == "i":
            hero.show_inventory()
            room_A2.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_A2.enter()



# Create RoomA3(Room) class here
class RoomA3(object):
    
    def description(self):
        os.system('clear')
        print "This is room A3"
        print "Directions: DOWN(s), LEFT(a)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

        if choice == "s":
            room_B3.enter()

        elif choice == "a":
            room_A2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_A3.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_A3.enter()



# Create RoomB1(Room) class here
class RoomB1(object):

    def description(self):
        os.system('clear')
        print "This is room B1"
        print "Directions: UP(w), DOWN(s), RIGHT(d)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

	if choice == "w":
	    room_A1.enter()
	
	elif choice == "s":
	    room_C1.enter()

	elif choice == "d":
	    room_B2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_B1.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_B1.enter()



# Create RoomB2(Room) class here
class RoomB2(object):
    
    def description(self):
        os.system('clear')
        print "This is room B2"
	print "There is a shop(p) in this room"
        print "Directions: UP(w), DOWN(s), LEFT(a), RIGHT(d)"
    
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

        if choice == "w":
            room_A2.enter()

        elif choice == "s":
            room_C2.enter()

        elif choice == "a":
            room_B1.enter()

        elif choice == "d":
            room_B3.enter()
	
	elif choice == "i":
	    hero.show_inventory()
	    room_B2.enter()

	elif choice == "p":
	    shop.enter()
	    room_B2.enter()

	elif choice == "q":
	    os.system('clear')
	    exit()
	
	else:
	    print "That is an invalid selection"
	    raw_input("<Press enter to continue>")
	    room_B2.enter()



# Create RoomB3(Room) class here
class RoomB3(object):
    
    def description(self):
        os.system('clear')
        print "This is room B3"
        print "Directions: UP(w), DOWN(s), LEFT(a)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

	if choice == "w":
	    room_A3.enter()
	
	elif choice == "s":
	    room_C3.enter()

	elif choice == "a":
	    room_B2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_B3.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_B3.enter()



# Create RoomC1(Room) class here
class RoomC1(object):
    
    def description(self):
        os.system('clear')
        print "This is room C1"
        print "Directions: UP(w), RIGHT(d)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

	if choice == "w":
	    room_B1.enter()

	elif choice == "d":
	    room_C2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_C1.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_C1.enter()



# Create RoomC2(Room) class here
class RoomC2(object):
    
    def description(self):
        os.system('clear')
        print "This is room C2"
        print "Directions: UP(w), LEFT(a), RIGHT(d)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

	if choice == "w":
	    room_B2.enter()

	elif choice == "a":
	    room_C1.enter()

	elif choice == "d":
	    room_C3.enter()

	elif choice == "i":
            hero.show_inventory()
            room_C2.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_C2.enter()



# Create RoomC3(Room) class here
class RoomC3(object):
    
    def description(self):
        os.system('clear')
        print "This is room C3"
        print "Directions: UP(w), LEFT(a)"
        
    def enter(self):
	combat = CombatSequence()
        combat.random_spawn()
        self.description()

	choice = raw_input("> ")

	if choice == "w":
	    room_B3.enter()

	elif choice == "a":
	    room_C2.enter()

	elif choice == "i":
            hero.show_inventory()
            room_C3.enter()

        elif choice == "q":
            os.system('clear')
            exit()
        
        else:
            print "That is an invalid selection"
            raw_input("<Press enter to continue>")
            room_C3.enter()



### Game Starts in 'RoomB2(Room)' instance: The center room ###

# Clear the screen before the game starts
os.system('clear')

# Simple introduction follows
print "Welcome to My Mud Version 0.1"
print "Created by James Buel (james.buel@gmail.com)"
print "Enjoy!\n"

raw_input("<Press Enter to Start!>")
os.system('clear')

# Name your character
print "Please give your character a name:"
char_name = raw_input("> ")
os.system('clear')

# Create instance of Player class named 'hero' with name input
hero = Player(char_name)
shop = Shop()
dead = DeathSequence()

# Create Room class instances
room_A1 = RoomA1()
room_A2 = RoomA2()
room_A3 = RoomA3()

room_B1 = RoomB1()
room_B2 = RoomB2()
room_B3 = RoomB3()

room_C1 = RoomC1()
room_C2 = RoomC2()
room_C3 = RoomC3()

hero.show_inventory()
room_B2.enter()
