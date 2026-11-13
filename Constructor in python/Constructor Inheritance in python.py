#Inheritance is an OOP concept in python where one class can use the attributes(properties) and methods of another class imagine a parent has some properties and a child inherits(use) some properties from the parent e.g:-
class Animal: #Parent class
    def eat(self):
        print("Animal is eating")
    
class Dog(Animal): #Child class
    def bark(self):
        print("Dog is barking")

dog1 = Dog()
dog1.eat()#Dog inherits from Animals so the Dog class can use the eat() method defined in Animal.
dog1.bark()
#Constructor inheritance e.g:-
class Pet:
    def __init__(self,name):
        self.name = name

class Bird(Pet):
    pass
bird1 = Bird("Pegion")

print(bird1.name)#this work how we didn't use constructor __init__() inside the class Bird() but python found the parent's __init__() method and used it and this is called inheriting the constructor.
#Now what happens if the child has it's own constructor e.g:-
class Hero:
    def __init__(self,name):
        self.name = name
class Heroni(Hero):
    def __init__(self,caste):
        self.caste = caste
villian1 = Heroni("Kajal")
print(villian1.caste)
print(villian1.name)#this gives an attributesError because when child didn't have it's own method then it use the parent method but when child has it's own method then instead of using the parent method it's used it's own method cause it's has it's own method so villian1.caste is correct and line 32 got Error.
