import numpy as np

class IslandTile:
    
    def __init__(self, name, a, encounters, description):
        self.name = name
        self.items = ["Rock", "Rock", "Palm Tree", "Treasure Chest", "Food", "A Grumpy Parrot", "Bones of the Last Marooned Pirate", "Water", "A Bag of Silver", "Message in a Bottle", "Food", "A Rusty Sword", "Dirty Underwear", "Sand", "More Sand", "Even More Sand", "A Dead Fish", "Palm Tree", "Palm Tree", "Fallen Log", "Crocodile", "Snake", "Rock", "Water", "A Beat Up Practice Dummy"]
        self.encounters = encounters
        self.description = description
        #Now variables that have default values
        self.discovered = False
        self.lootedItems = []     #By keeping track of these, we make
        self.pastEncounters = []  #sure we don't find the same thing twice
        
    def enterTile(self):
        #Your code here
        if self.discovered:
            print("You enter the "+self.name)
        else:
            self.discovered = True
            print(self.description)
    
    def leaveTile(self):
        #Your code here
        print("After a long day of searching "+self.name+", you return to your camp.")
    
    def search(self):
        #your code here
        encounter = None
        loot = None
        try:
            encounter = self.encounters[np.random.randint(len(self.encounters))]
            loot = self.items[np.random.randint(len(self.items))]
        except:
            print("The items you've collected on the island are strewn about your camp")
        else:
            if encounter in self.pastEncounters:
                encounter = None
                loot = None
            else:
                self.pastEncounters.append(encounter)
                if loot in self.lootedItems:
                    loot = None
                else:
                    self.lootedItems.append(loot)
        return loot, encounter