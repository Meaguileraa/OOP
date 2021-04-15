

#Make a class of pets with a dog, cat, and bird pet 

class Pets():
    """Making a pet class."""

    def __init__(self, name, age, breed):
        """Initializing a pet."""

        self.name = name
        self.age = age
        self.breed = breed 

    def speak(self):
        """Allow the pet to speak."""

        print("Hello!")

class Dogs(Pets):
    """Dog class inheriting from the Pet class."""

    def speak(self):
        """What a dog says."""

        print(f"Bark, I'm {self.name} the {self.breed}!")

class Cats(Pets):
    """Cat class inhertiing from the Pet class."""


    def speak(self):
        """What a cat says."""

        print(f"Meow, I'm {self.name} the {self.breed}!")

    


class Birds(Pets):
    """Bird class inheriting from the Pet class."""

    def speak(self):
        """What a bird says."""

        print(f"Chirp, I'm {self.name} the {self.breed}!")


d1 = Dogs("Marley", 8, "Jack Russell")
d2 = Dogs("Chloe", 8, "Poodle")
d3 = Dogs("Maya", 13, "Miniature Pekingese")

d1.speak()
d2.speak()
d3.speak()

c1 = Cats("Nala", 11, "meanie")

c1.speak()

b1 = Birds("Blue", 4, "Macaw")
b2 = Birds("Love", 3, "Parrot")

b1.speak()
b2.speak()


