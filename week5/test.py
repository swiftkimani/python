# Superhero base class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name  # Hero's name
        self.power = power  # Hero's superpower
        self.health = health  # Hero's health level

    def fight(self):
        print(f"{self.name} is fighting with their {self.power}!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed by {amount}. Health is now {self.health}.")

# Villain class inherits from Superhero
class Villain(Superhero):
    def __init__(self, name, power, health, evil_plan):
        super().__init__(name, power, health)  # Inherit attributes from Superhero
        self.evil_plan = evil_plan  # Villain specific attribute

    def fight(self):
        print(f"{self.name} is using {self.power} to enact their evil plan: {self.evil_plan}!")

# Create instances of Superhero and Villain
hero = Superhero("Captain Justice", "Laser Vision", 100)
villain = Villain("Doctor Evil", "Mind Control", 80, "Take over the world!")

# Use methods from both classes
hero.fight()
hero.heal(20)

villain.fight()
villain.heal(10)
