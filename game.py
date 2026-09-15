from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Triangle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    goblinTwo= Goblin("Scribble")

    arcane= Hero("Arcane")

    print(f"{arcane.name} enters the arena with {arcane.health} health.")

    heroDamage= arcane.attack()
    goblin.take_damage(heroDamage)

    goblinDamage = goblin.attack()
    arcane.use_healing()
    arcane.take_damage(goblinDamage)

    goblinDamage = goblin.attack()
    arcane.use_healing()
    arcane.take_damage(goblinDamage)

    

    
if __name__ == "__main__":
    main()
