class Pets:

    def __init__(self, name, species, age, color):

        self.name = name 
        self.species = species
        self.age = age
        self.color = color 

    def baden_pets(self):

        #print(f'Hello, I am {self.name} the {self.species}. I am {self.age} years old and {self.color}')

        p1 = Pets('Maya', 'dog', '13', 'brown/black')
        p2 = Pets('Marley', 'dog', '9', 'brown')
        p3 = Pets('Chloe', 'dog', '7', 'white')
        p4 = Pets('Shrek', 'caterpillar', '4 weeks', 'green/yellow')
        p5 = Pets('Waldo', 'caterpillar', '2 weeks', 'green/yellow')
    p1.baden_pets()
    p2.baden_pets()
    p3.baden_pets()
    p4.baden_pets()
    p5.baden_pets()