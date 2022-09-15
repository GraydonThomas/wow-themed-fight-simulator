#!/usr/bin/env python

"""
Simple WoW Themed Object-Oriented Programming Fight Simulator
"""

import random
import math
races = ['Human', 'Orc', 'Blood Elf', 'Tauren', 'Dwarf']
classes = ['Warrior', 'Paladin', 'Death Knight', 'Mage', 'Rogue']
battle_on = True


class Character:

    def __init__(self, chosen_race, chosen_class):

        self.chosen_race = chosen_race
        self.chosen_class = chosen_class
        self.attack = 0
        self.defense = 0
        self.health = 0
        self.max_health = 0
        self.mana = 0
        self.max_mana = 0

        if chosen_class == "Warrior":
            self.special_ability = "Whirlwind - Mana Cost: 20; May hit up to 3 times"
        if chosen_class == "Paladin":
            self.special_ability = "Holy Light - Mana Cost: 20; Heals self and damages opponent"
        if chosen_class == "Death Knight":
            self.special_ability = "Obliterate - Mana Cost: 20; Damages opponent and self"
        if chosen_class == "Mage":
            self.special_ability = "Mana Boost - Mana Cost: 30; Boosts attack and defense and deals small damage"
        if chosen_class == "Rogue":
            self.special_ability = "Assassinate - Mana Cost: 50; Deals massive damage"

    def __str__(self):

        # Determine proper grammar
        if (self.chosen_race[0] == "A" or self.chosen_race[0] == "E" or self.chosen_race[0] == "I" or
                self.chosen_race[0] == "O" or self.chosen_race[0] == "U"):

            strobj = (f"You are an {self.chosen_race} {self.chosen_class}. " 
                      f"You currently have {self.attack} attack, {self.defense} defense, {self.health} health, " 
                      f"and {self.mana} mana. \nYour special ability is {self.special_ability}.")
            return strobj

        else:
            strobj = (f"You are a {self.chosen_race} {self.chosen_class}. " 
                      f"You currently have {self.attack} attack, {self.defense} defense, {self.health} health, " 
                      f"and {self.mana} mana. \nYour special ability is {self.special_ability}.")
            return strobj

    def stat_roll(self):

        # Randomize the generated stats
        self.attack = random.randint(1, 10)
        self.defense = random.randint(1, 10)

        # Ensure health/mana stats are round numbers divisible by 10
        while self.health == 0 or not (self.health % 10 == 0):
            self.health = random.randint(100, 200)
            self.max_health = self.health

        while self.mana == 0 or not (self.mana % 10 == 0):
            self.mana = random.randint(50, 100)
            self.max_mana = self.mana

    def basic_attack(self):

        # Initiate a basic attack
        damage_done = self.attack + random.randint(1, 5)
        return damage_done

    def receive_attack(self, attack):

        # Record a received attack
        self.health = self.health - attack
        if self.health < 0:
            self.health = 0
        print(f"The {self.chosen_race} {self.chosen_class} is hit for {attack} damage and has {self.health} "
              f"health remaining.")

    def special_attack(self):

        # Initiate a special attack, depending on the class

        # Warrior
        if self.chosen_class == "Warrior":

            print(f"The {self.chosen_race} {self.chosen_class} readies Whirlwind for 20 mana!")

            if self.mana >= 20:
                self.mana -= 20

                # Whirlwind may hit multiple times, or miss entirely

                damage_done = 0
                hit_chance = random.randint(1, 1000)

                if hit_chance < 150:
                    print("The Whirlwind MISSES!")
                    damage_done = 0

                elif 150 <= hit_chance < 500:
                    damage_done = self.attack + 5
                    print(f"The Whirlwind hits once for {damage_done} damage!")

                elif 500 <= hit_chance < 750:
                    damage_done = (self.attack + 5) * 2
                    print(f"The Whirlwind hits TWICE for a total of {damage_done} damage!")

                elif hit_chance >= 750:
                    damage_done = (self.attack + 5) * 3
                    print(f"The Whirlwind hits THREE times for a total of {damage_done} damage!")

                print(f"Your remaining mana is {self.mana}.")
                return damage_done

            else:
                damage_done = 0
                print(f"You did not have enough mana, and forfeit your turn. Your remaining mana is {self.mana}.")
                return damage_done

        # Paladin
        if self.chosen_class == "Paladin":

            print(f"The {self.chosen_race} {self.chosen_class} readies Holy Light for 20 mana!")

            if self.mana >= 20:
                self.mana -= 20

                # Holy Light will heal the player and damage the opponent

                damage_done = 0
                hit_chance = random.randint(1, 1000)

                if hit_chance < 150:
                    print("The Holy Light fizzles out!")
                    damage_done = 0

                elif 150 <= hit_chance < 500:
                    damage_done = self.attack + 3

                    if self.health + 10 <= self.max_health:
                        self.health += 10
                        print(f"The Holy Light hits for {damage_done} damage and heals the player for 10!")
                        print(f"The player's health is now {self.health}/{self.max_health}.")
                    else:
                        print(f"The Holy Light hits for {damage_done} damage and heals the player for "
                              f"{self.max_health - self.health}!")
                        self.health = self.max_health
                        print(f"The player's health is now {self.health}/{self.max_health}.")

                elif 500 <= hit_chance < 750:
                    damage_done = self.attack + 5

                    if self.health + 20 <= self.max_health:
                        self.health += 20
                        print(f"The Holy Light CRITS for {damage_done} damage and heals the player for 20!")
                        print(f"The player's health is now {self.health}/{self.max_health}.")
                    else:
                        print(f"The Holy Light hits for {damage_done} damage and heals the player for "
                              f"{self.max_health - self.health}!")
                        self.health = self.max_health
                        print(f"The player's health is now {self.health}/{self.max_health}.")

                elif hit_chance >= 750:
                    damage_done = self.attack + 7

                    if self.health + 30 <= self.max_health:
                        self.health += 30
                        print(f"The Holy Light CRITS!! for {damage_done} damage and heals the player for 30!")
                        print(f"The player's health is now {self.health}/{self.max_health}.")
                    else:
                        print(f"The Holy Light hits for {damage_done} damage and heals the player for "
                              f"{self.max_health - self.health}!")
                        self.health = self.max_health
                        print(f"The player's health is now {self.health}/{self.max_health}.")

                print(f"Your remaining mana is {self.mana}.")
                return damage_done

            else:
                damage_done = 0
                print(f"You did not have enough mana, and forfeit your turn. Your remaining mana is {self.mana}.")
                return damage_done

        # Death Knight
        if self.chosen_class == "Death Knight":

            print(f"The {self.chosen_race} {self.chosen_class} readies Obliterate for 20 mana!")

            if self.mana >= 20:
                self.mana -= 20

                # Obliterate does large damage and damages the caster

                damage_done = 0
                hit_chance = random.randint(1, 1000)

                if hit_chance < 150:
                    print("Obliterate MISSES!")
                    damage_done = 0

                elif 150 <= hit_chance < 500:
                    damage_done = (self.attack * 2) + 5
                    self.health -= int(math.ceil(0.1 * damage_done))
                    self_damage = int(math.ceil(0.1 * damage_done))
                    print(f"Obliterate hits for {damage_done} damage and self-inflicts {self_damage} damage!")
                    print(f"The player's heath is now {self.health}.")

                elif 500 <= hit_chance < 750:
                    damage_done = (self.attack * 2) + 10
                    self.health -= int(math.ceil(0.1 * damage_done))
                    self_damage = int(math.ceil(0.1 * damage_done))
                    print(f"Obliterate CRITS for {damage_done} damage and self-inflicts {self_damage} damage!")
                    print(f"The player's heath is now {self.health}.")

                elif hit_chance >= 750:
                    damage_done = (self.attack * 2) + 15
                    self.health -= int(math.ceil(0.1 * damage_done))
                    self_damage = int(math.ceil(0.1 * damage_done))
                    print(f"Obliterate CRITS!! for {damage_done} damage and self-inflicts {self_damage} damage!")
                    print(f"The player's heath is now {self.health}.")

                print(f"Your remaining mana is {self.mana}.")
                return damage_done

            else:
                damage_done = 0
                print(f"You did not have enough mana, and forfeit your turn. Your remaining mana is {self.mana}.")
                return damage_done

        # Mage
        if self.chosen_class == "Mage":

            print(f"The {self.chosen_race} {self.chosen_class} readies Mana Boost for 30 mana!")

            if self.mana >= 30:
                self.mana -= 30

                # Mana Barrier increases maximum attack and armor

                damage_done = 0
                hit_chance = random.randint(1, 1000)

                if hit_chance < 150:
                    print("The Mana Boost faintly glows.")
                    damage_done = 0
                    self.attack += 1
                    self.defense += 1
                    print(f"The Mana Boost increases your attack and defense by 1, and deals 0 damage to the enemy!")
                    print(f"The player's new attack is {self.attack} and defense is {self.defense}.")

                elif 150 <= hit_chance < 500:
                    damage_done = 3
                    self.attack += 2
                    self.defense += 2
                    print(f"The Mana Boost increases your attack and defense by 2, and deals 3 damage to the enemy!")
                    print(f"The player's new attack is {self.attack} and defense is {self.defense}.")

                elif 500 <= hit_chance < 750:
                    damage_done = 5
                    self.attack += 3
                    self.defense += 3
                    print(f"The Mana Boost increases your attack and defense by 3, and deals 5 damage to the enemy!")
                    print(f"The player's new attack is {self.attack} and defense is {self.defense}.")

                elif hit_chance >= 750:
                    damage_done = 7
                    self.attack += 5
                    self.defense += 5
                    print(f"The Mana Boost increases your attack and defense by 5, and deals 7 damage to the enemy!")
                    print(f"The player's new attack is {self.attack} and defense is {self.defense}.")

                print(f"Your remaining mana is {self.mana}.")
                return damage_done

            else:
                damage_done = 0
                print(f"You did not have enough mana, and forfeit your turn. Your remaining mana is {self.mana}.")
                return damage_done

        # Rogue
        if self.chosen_class == "Rogue":

            print(f"The {self.chosen_race} {self.chosen_class} readies Assassinate for 50 mana!")

            if self.mana >= 50:
                self.mana -= 50

                # Assassinate does heavy damage and costs a large amount of mana

                damage_done = 0
                hit_chance = random.randint(1, 1000)

                if hit_chance < 150:
                    print("Assassinate misses!")
                    damage_done = 0

                elif 150 <= hit_chance < 500:
                    damage_done = (self.attack * 2) + 25
                    print(f"Assassinate hits for a total of {damage_done} damage!")

                elif 500 <= hit_chance < 750:
                    damage_done = (self.attack * 2) + 35
                    print(f"Assassinate CRITS for a total of {damage_done} damage!")

                elif hit_chance >= 750:
                    damage_done = (self.attack * 2) + 50
                    print(f"Assassinate CRITS!! for a total of {damage_done} damage!")

                print(f"Your remaining mana is {self.mana}.")
                return damage_done

            else:
                damage_done = 0
                print(f"You did not have enough mana, and forfeit your turn. Your remaining mana is {self.mana}.")
                return damage_done


# Choose a race
def race_choice():
    my_race = ""

    while my_race not in races:
        print("The available races are: ")
        print(races)
        my_race = (str(input("Please choose your race: "))).title()
        if my_race not in races:
            print("That is not one of the available races. Please try again.")
        else:
            return my_race


# Choose a class
def class_choice():
    my_class = ""

    while my_class not in classes:
        print("The available classes are: ")
        print(classes)
        my_class = (str(input("Please choose your class: "))).title()
        if my_class not in classes:
            print("That is not one of the available classes. Please try again.")
        else:
            return my_class


# Check for a winner
def check_winner():

    if player_one.health <= 0:
        print(f"Player One's {player_one.chosen_race} {player_one.chosen_class} has died!")
        print(f"Player Two's {player_two.chosen_race} {player_two.chosen_class} is victorious!")
        return 1

    elif player_two.health <= 0:
        print(f"Player Two's {player_two.chosen_race} {player_two.chosen_class} has died!")
        print(f"Player One's {player_one.chosen_race} {player_one.chosen_class} is victorious!")
        return 2

    else:
        pass


# Determine which player goes first
def first_turn():
    turn_roll = random.randint(0, 1)

    if turn_roll == 0:
        return True
    else:
        return False


# -- Start the Game --


# Character Creation
print("Player One, please create your character.")
chosen_race = race_choice()
chosen_class = class_choice()
player_one = Character(chosen_race, chosen_class)
player_one.stat_roll()

print("Player Two, please create your character.")
chosen_race = race_choice()
chosen_class = class_choice()
player_two = Character(chosen_race, chosen_class)
player_two.stat_roll()

print("\nPlayer One: ")
print(player_one)
print("\nPlayer Two: ")
print(player_two)

current_turn = first_turn()

if current_turn:
    print(f"\nBy the flip of a coin, Player One, the {player_one.chosen_race} {player_one.chosen_class} goes first!")

if not current_turn:
    print(f"\nBy the flip of a coin, Player Two, the {player_two.chosen_race} {player_two.chosen_class} goes first!")


# Game loop
while battle_on:

    if not battle_on:
        break

    player_decision = ""

    if current_turn:
        print(f"Player One's {player_one.chosen_race} {player_one.chosen_class}'s turn!")

        while player_decision == "":

            # Player one makes a move
            player_decision = input(f"\nPlayer One, What would you like to do? (Mana: {player_one.mana}) \n"
                                    "[A] = Attack \n"
                                    "[S] = Special \n"
                                    "[P] = Pass: \n"
                                    "-------------- \n"
                                    "[ ] = ").upper()
            if player_decision == "A":
                damage = player_one.basic_attack()
                player_two.receive_attack(damage)
                current_turn = False
                break

            if player_decision == "S":
                damage = player_one.special_attack()
                player_two.receive_attack(damage)
                current_turn = False
                break

            if player_decision == "P":
                print("Player One skips their turn.")
                current_turn = False
                break

            else:
                print("Incorrect input.")
                player_decision = ""

        # Check if someone has won
        check_winner()
        if check_winner == 1:
            battle_on = False
            break
        if check_winner == 2:
            battle_on = False
            break
        else:
            continue

    if not current_turn:
        print(f"Player Two's {player_two.chosen_race} {player_two.chosen_class}'s turn!")

        while player_decision == "":

            # Player two makes a move
            player_decision = input(f"\nPlayer Two, What would you like to do? (Mana: {player_two.mana}) \n"
                                    "[A] = Attack \n"
                                    "[S] = Special \n"
                                    "[P] = Pass: \n"
                                    "-------------- \n"
                                    "[ ] = ").upper()
            if player_decision == "A":
                damage = player_two.basic_attack()
                player_one.receive_attack(damage)
                current_turn = True
                break

            if player_decision == "S":
                damage = player_two.special_attack()
                player_one.receive_attack(damage)
                current_turn = True
                break

            if player_decision == "P":
                print("Player Two skips their turn.")
                current_turn = True
                break

            else:
                print("Incorrect input.")
                player_decision = ""

        # Check if someone has won
        winner = check_winner()
        if winner == 1:
            battle_on = False
            break
        if winner == 2:
            battle_on = False
            break
        else:
            continue

print("The end!")
