from goblin import Goblin
from hero import Hero
from boss import Boss


ARENA_NAME = "The Iron Triangle"

def battle(hero: Hero, enemy : Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
            hero.use_healing()
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else: 
        print(f"{enemy.name} wins!")
def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblinTwo= Goblin("Scribble")

    hero= Hero("Arcane")

    print(f"{hero.name} enters the arena with {hero.health} health.")
    battle(hero, goblin)

    boss= Boss("GUCCI MORTY")
    print(f"{boss.name} enters the arena with {boss.health} health.")
    battle(hero, boss)
    
     
    

    
if __name__ == "__main__":
    main()
