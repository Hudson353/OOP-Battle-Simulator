import random
healingHas_run= False
healingNotify=0

class Hero:
    def __init__(self,name):
        self.name= name
        self.attack_power= 25
        self.health= 150
        self.maxHealth = self.health
        self.armor=10

    def attack(self): 
        return random.randint(1, self.attack_power)

    def take_damage(self,damage):
        if self.armor != 0:
            armor_damage= max(0, int(damage-10))
            self.health= max(0, self.health-armor_damage)
            blocked_damage = damage - armor_damage
            print ((f"{self.name}'s Armor reduced {blocked_damage} damage. Damage receiced: "
                  f"{armor_damage}; Health: {self.health}; Armor: {self.armor-1} "))
            self.armor -= 1
            return self.armor
        else:
            self.health= max(0, self.health-damage)
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
    
    def use_healing(self):
        global healingHas_run
        global healingNotify
        if healingNotify == 0:
            healing_Answer=input("Would you like to use your healing?(yes or no)") 
            if healing_Answer.lower()== "yes":     
                if healingHas_run:
                    print(f"{self.name} has already used their healing!")
                    healingNotify += 1
                    return
                    

                healingAmount=random.randint(1,25)
                recordhealth = self.health
                self.health = min(self.maxHealth,self.health+healingAmount)
                print(f"{self.name}'s healing grants {abs(recordhealth-self.health)} amount of Health!")
                healingHas_run=True

            else:
                return

                