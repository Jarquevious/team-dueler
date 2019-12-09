import random

class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      # Pick a random value between 0 and self.max_damage
      random_value = random.randint(0, self.max_damage)
      return random_value
      

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        block = random.randint(0, self.max_block)
        return block

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
            '''Instance properties:
                abilities: List
                armors: List
                name: String
                starting_health: Integer
                current_health: Integer
            '''

            # abilities and armors don't have starting values,
            # and are set to empty lists on initialization
            self.abilities = list()
            self.armors = list()
            # we know the name of our hero, so we assign it here
            self.name = name
            # similarly, our starting health is passed in, just like name
            self.starting_health = starting_health
            # when a hero is created, their current health is
            # always the same as their starting health (no damage taken yet!)
            self.current_health = starting_health  
            self.kills = 0
            self.deaths = 0  

    def add_kill(self, num_kills):
        # adds kills to total stats
        self.kills += num_kills
    
    def add_deaths(self, num_deaths):
        # adds deaths to total stats
        self.deaths += num_deaths

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

class Team:
    def __init__(self, name)
        self.name = name 
        self.heroes = []

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)
    
    def defend(self):
        '''Calculate the total block amount from all armor blocks.
           return: total_block:Int
        '''
        # TODO: This method should run the block method on each armor in self.armors
        defend_total = 0 
        for armor in self.armors: 
             defend_total += armor.block() 
        return defend_total

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        defense = self.defend()    
        self.current_health -= damage - defense

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.'''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health > 0: 
            return True
        else:
            return False

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        if len(self.abilities) < 0 and len(opponent.abilities) < 0:
            print("Its a Draw!")
        while True:
            if self.is_alive():
                outgoing_damage = self.attack()
                opponent.take_damage(outgoing_damage)
            else:
                print(f"{self.name} died!")
                self.add_deaths(1)
                opponent.add_kill(1)
                return
            if opponent.is_alive():
                incoming_damage = opponent.attack()
                self.take_damage(incoming_damage)
            else:
                print(f"{self.name} killed {opponent.name}!")
                opponent.add_deaths(1)
                self.add_kill(1)
                return

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))




    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = 100
            hero.status = "Alive"
   
    def attack(self, opponents):
        ''' Battle each hero against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponents.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            first_random_hero = self.heroes[random.choice(living_heroes)]
            second_random_hero = opponents.heroes[random.choice(living_opponents)]

            first_random_hero.fight(second_random_hero)
            
            for hero in living_heroes:
                if hero == 'Dead':
                    hero.append.





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 80)
    ability2 = Ability("Super Eyes", 30)
    ability3 = Ability("Wizard Wand", 300)
    ability4 = Ability("Wizard Beard", 120)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
