
class AquaticMixin:
    def swim(self):
        print("just keep swimming.")

    def encounter_water(self):
        print("I don't mind")
        self.swim()

    def dive(self):
        print("diving into the deep! boom!")


class AbstractAnimal: #this is a superclass
    def __init__(self, name, age):#can also put hungry =True in parameter
        self.name = name
        self.age = age
        self.hungry = True

    def eat(self):
        print("I'm ready to eat")
        self.hungry = False
        print("omomomom")

    def run(self):
        print("I'm running, buring calories.")
        self.hungry = True

    def wants_food(self):
        return self.hungry

    def encounter_water(self):
        print("*drowning sound*")


class Rodent(AbstractAnimal):
    diet = "nuts and berries"
    lives_in_holes = True



#class Hedgehog(AbstractAnimal): 
class Hedgehog(Rodent):
#Subclass, superclass has to be parameter of subclass

    species = "hedgehog"

    def __init__(self, name, spikiness_level, age): 
    #added a def init method here bc of inheritance

        super().__init__(name, age) #use super when you have different instance attributes
        self.spikiness_level = spikiness_level#this is a instance attribute 

    def react_to_berry(self):
        print("I see a berry")
        if self.wants_food():
            self.eat()
        else:
            print("I'm not hungry yet, maybe later.")

    def encounter_water(self):
        super().encounter_water() #super can be used with any other method 
        print("pokey pokey")



class Chipmunk(Rodent): #subclass 
    species = "chipmunk"

    def __init__(self, name, age, hair_style):

        super().__init__(name, age)



#Mixin is saying there are a lot of methods and class attributes 
class Capybara(AquaticMixin, Rodent): #can have two superclasses
    species = "capybara"



#to call a method in a method you need to use self.method name (don't need to use self as parameter)


if __name__ == "__main__":
#always best practice to have this at the bottom(even not with classes) 
#use this when importing a file

    henry = Hedgehog("Henry", 2, 10)
    lacey = Hedgehog("Lacey", 1, 7)#they are instances or objects of hedgehog or chipmonk classes
    alvin = Chipmnk("Alvin", 3)#calling the init function to make the functions happen
    pasta = Capybara("Pasta", 1)



#PYTHON INTERPRETER
#python3 -i classes2.py
#henry.react_to_berry()
#henry.run()
#henry.wants_food()

















