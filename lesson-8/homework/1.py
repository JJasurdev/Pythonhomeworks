class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}."
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        return f"{self.name} laid an egg."

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, "Horse", "Neigh")
    
    def run(self):
        return f"{self.name} is running fast."

# Example usage:
cow = Cow("Bessie")
chicken = Chicken("Clucky")
horse = Horse("Thunder")

animals = [cow, chicken, horse]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat("grass"))
    print(animal.sleep())
    
    if isinstance(animal, Cow):
        print(animal.produce_milk())
    elif isinstance(animal, Chicken):
        print(animal.lay_egg())
    elif isinstance(animal, Horse):
        print(animal.run())
    
    print("-")
