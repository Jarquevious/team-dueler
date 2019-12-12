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

class Weapon(Ability):
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
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        
        self.abilities.append(weapon)

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
    def __init__(self, name, ability):
        self.name = name 
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list. If Hero isn't found return 0.'''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
          if hero.name == name:
              self.heroes.remove(hero)
              # set our indicator to True
              foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
          if not foundHero:
              return 0

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # TODO: Add the Hero object that is passed in to the list of heroes in
        # self.heroes
        self.heroes.append(hero)
        
        
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.ability:
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
        if len(self.ability) < 0 and len(opponent.ability) < 0:
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

class Weapon(Ability):   
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
                    hero.append.living_heroes

class Arena:
    def __init__(self):
        '''Instantiate properties
            team1: None
            team2: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        team1: None
        team2: None 

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon_name = input('Create a weapon name: ')

        while True:
            weapon_damage = input('Enter how much damage your item will do: ')
            if weapon_damage.isnumeric():
                break
            elif weapon_damage.isalnum():
                print('Please enter an input with numbers only')

        return Weapon(weapon_name, int(weapon_damage))


    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
    
        armor_name = input('Create an armor name: ')
        while True:
            block_input = input('Enter how much your armor will block: ')
            if block_input.isnumeric():
                break
            elif block_input.isalnum():
                print('Please enter an input with numbers only')

        return Armor(armor_name, int(block_input))

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #TODO add an ability to the hero
               punch = Ability("punch", 20)
               hero.add_ability(punch)
           elif add_item == "2":
               #TODO add a weapon to the hero
               dagger = Weapon("dagger", 25)
               hero.add_weapon(dagger)
           elif add_item == "3":
               #TODO add an armor to the hero
               shield = Armor("shield", 18)
               hero.add_ability(shield)
        return hero

    def build_team1(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        add_hero_team = int(
            input('How many heroes would you like on team one? '))

        for amount in range(add_hero_team):
            self.team1.add_hero(self.create_hero())

        hero_list = [hero.name for hero in self.team1.hero_list]
        print(f'Heroes on Team 1: {", ".join(hero_list)}')

    def build_team2(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # 1) Prompt the user for the name of the team
        # 2) Prompt the user for the number of Heroes on the team
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        add_hero_team = int(
            input('How many heroes would you like on team two? '))

        for amount in range(add_hero_team):
            self.team2.add_hero(self.create_hero())

        hero_list = [hero.name for hero in self.team2.hero_list]
        print(f'Heroes on Team 2: {", ".join(hero_list)}')


    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team1.attack(self.team2)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        print('=' * 24)
        print('TEAM ONE STATISTICS: \n')
        print(f'\nTeam one\'s stats: {self.team1.stats()}\n')

        print('=' * 24)

        print('TEAM TWO STATISTICS: \n')
        print(f'\nTeam two\'s stats: {self.team2.stats()}\n')
        print('=' * 24)

        print('FIGHT OUTCOME: \n')
        if self.team1.team_alive():
            hero_list = [hero.name for hero in self.team1.hero_list]
            print(
                f'Team 1 is victorious!\nChampions: {", ".join(hero_list)}')
        else:
            hero_list = [hero.name for hero in self.team2.hero_list]
            print(
                f'Team 2 is victorious!\nChampions: {", ".join(hero_list)}')
        print('=' * 24)





if __name__ == "__main__":
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 80)
    # ability2 = Ability("Super Eyes", 30)
    # ability3 = Ability("Wizard Wand", 300)
    # ability4 = Ability("Wizard Beard", 120)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # team1 = Team("Team1", ability1)
    # team1.add_hero(hero1)
    # team2 = Team("Team2", ability2)
    # team1.fight(team2)

    # arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team1()
    arena.build_team2()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team1.revive_heroes()
            arena.team2.revive_heroes()

