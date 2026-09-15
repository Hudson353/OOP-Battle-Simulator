import random
healingHas_run= False

class Hero:
    def __init__(self,name):
        self.name= name
        self.attack_power= 25
        self.health= 150
        self.armor=10

    def attack(self): 
        return random.randint(1, self.attack_power)

    def take_damage(self,damage):
        if self.armor != 0:
            self.health= max(0, self.health-(int(damage/3)))
            print ((f"{self.name}'s Armor reduced {damage-(int(damage/3))} damage. Damage receiced: "
                  f"{(int(damage/3))}; Health: {self.health}; Armor: {self.armor-1} "))
            self.armor -= 1
            return self.armor
        else:
            self.health= max(0, self.health-damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
    
    def use_healing(self):
        global healingHas_run    
        if healingHas_run:
            print(f"{self.name} has already used their healing!")
            return
                
        healingAmount=random.randint(1,25)
        print(f"{self.name}'s healing grants {healingAmount} amount of Health!")
        self.health += healingAmount
        healingHas_run=True

                