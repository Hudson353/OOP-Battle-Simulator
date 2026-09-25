import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name,health= 100, attackPower=7)
        self.gold =0

    def stealGold(self, hero):
        """GOBBOS TAKIN HEROES GOLD."""
        self.gold=self.gold + hero.gold
        hero.gold=0
        print("GIT REKT NOOB")
       

    

    

        
