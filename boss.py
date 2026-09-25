from enemy import Enemy
import random

class Boss(Enemy):
    def __init__(self,name):
        super().__init__(name,200,15)

    #overrides parent attack with a much cooler attack
    def attack(self):
        attackStyle =random.randint(1,2)
        if attackStyle == 1:
            print("FIREBALL")
            return 5 * random.randint(1,4)
        else:
            print("STOMP")
            return self.attack_power() * random.randint(1,2)

    def take_damage(self, damage):
        damage=damage * .75
        super().take_damage(damage)
