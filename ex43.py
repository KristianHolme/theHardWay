from sys import exit
from random import randint
from textwrap import dedent
from os import system

loop = True

class entity(object):
    def __init__(self, weapon, skill):
        self.weapon = weapon
        self.skill = skill


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        rep = Repeat()                      
        return rep

class CentralCorridor(Scene):

    def enter(self):
        system('cls')
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and
             destroyed your entire crew.  You are the last surviving
             member and your last mission is to get the neutron destruct
             bomb from the Weapons Armory, put it in the bridge, and
             blow the ship up after getting into an escape pod.

             You're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body. ENGAGING FIGHT MODE!
             """))

        fight_result = Fight()
        if "win" in fight_result:
            input()
            return 'laser_weapon_armory'
        else:
            input()
            return 'death'

class LaserWeaponArmory(Scene):

    def enter(self):
        system('cls')
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding.  It's dead
            quiet, too quiet.  You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out.  If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb.  The
            code is 3 digits.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 1

        if guess == "skip": return 'the_bridge'
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    The container clicks open and the seal breaks, letting
                    gas out.  You grab the neutron bomb and run as fast as
                    you can to the bridge where you must place it in the
                    right spot.
                    """))
            input()
            return 'the_bridge'
        else:
            print(dedent("""
                    The lock buzzes one last time and then you hear a
                    sickening melting sound as the mechanism is fused
                    together.  You decide to sit there, and finally the
                    Gothons blow up the ship from their ship and you die.
                    """))
            input()
            return 'death'

class TheBridge(Scene):

    
    def enter(self):
        system('cls')
        print(dedent("""
              You burst onto the Bridge with the netron destruct bomb
              under your arm and surprise 5 Gothons who are trying to
              take control of the ship.  Each of them has an even uglier
              clown costume than the last.  They haven't pulled their
              weapons out yet, as they see the active bomb under your
              arm and don't want to set it off.
              """))
        print("Options: \"throw the bomb\", \"slowly place the bomb\". What do you do?")
        action = input("> ")

        if action == "skip": return 'escape_pod'
        if action == "throw the bomb":
            print(dedent("""
                  In a panic you throw the bomb at the group of Gothons
                  and make a leap for the door.  Right as you drop it a
                  Gothon shoots you right in the back killing you.  As
                  you die you see another Gothon frantically try to
                  disarm the bomb. You die knowing they will probably
                  blow up when it goes off.
                  """))
            input()
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                  You point your blaster at the bomb under your arm and
                  the Gothons put their hands up and start to sweat.
                  You inch backward to the door, open it, and then
                  carefully place the bomb on the floor, pointing your
                  blaster at it.  You then jump back through the door,
                  punch the close button and blast the lock so the
                  Gothons can't get out.  Now that the bomb is placed
                  you run to the escape pod to get off this tin can.
                  """))
            input()
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            input()
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        system('cls')
        print(dedent("""
              You rush through the ship desperately trying to make it to
              the escape pod before the whole ship explodes.  It seems
              like hardly any Gothons are on the ship, so your run is
              clear of interference.  You get to the chamber with the
              escape pods, and now need to pick one to take.  Some of
              them could be damaged but you don't have time to look.
              There's 5 pods, which one do you take?
              """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if guess == 'skip': return 'finished'
        try:
            if int(guess) != good_pod:
                print(dedent("""
                    You jump into a pod and hit the eject button.
                    The pod escapes out into the void of space, then
                    implodes as the hull ruptures, crushing your body into
                    jam jelly.
                    """))
                input()
                return 'death'
            else:                
                print(dedent("""
                    You jump into a pod and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below.  As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time.  You won!
                    """))
                input()
                return 'finished'
        except:
            print("DOES NOT COMPUTE!")
            return 'escape_pod'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        rep = Repeat()
        return rep


class Map(object):

   scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

   def __init__(self, start_scene):
        self.start_scene = start_scene

   def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

   def opening_scene(self):
        return self.next_scene(self.start_scene)

Hero = entity("Fist", "none")
Enemy = entity("Fist", "none")

def Fight():
    weapons = {11:"spoon", 10:"Lightsaber", 9:"Railgun", 
        8:"Super-Ultra-Mega-Blaster", 7:"Blaster",
        6: "AK-47", 5:"Revolver", 4: "Sword", 3: "Dagger",
        2:"Kitchen knife", 1:"Stick"}

    print("You shalt now engage in fight.\nYou pull  out your best weapon from your back pocket.")
    w1index = randint(1, 11)
    w2index = randint(1, 11)

    Hero.weapon = weapons.get(w1index)
    Enemy.weapon = weapons.get(w2index)

    print(f"You got a {Hero.weapon}, your opponent has a {Enemy.weapon}!")
    if w1index - w2index <= 2 and w1index - w2index >= -2:
        print("You have pretty similar weapons. What do do?")
        print("Options: \"shoot\", \"dodge\", \"pray to the almighty flying spaghettimonster\".\nWhat do you do?")
        action = input(">>>")

        if "shoot" in action:
            print("You miss your enemy and it shoots you.")
            return 'death'
        elif "dodge" in action:
            print("You dodge and you get shot.")
            return 'death'
        elif "pray" in action:
            print("Nice move! Through a long series of unlikely events you have won!")
            return 'win'
    elif w1index > w2index:
        print("You have a far superior weapon, you win!")
        return 'win'
    elif w2index > w1index:
        print("You have a far inferior weapon. You lose.")
        return 'death'



def Repeat():
    print("Do you want to play again?")
    answer = input("Yes/No>>>>")
    if 'y' in answer:
        return 'central_corridor'
        
    elif 'n' in answer:
        exit(1)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()