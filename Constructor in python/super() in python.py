#continue from file constructor inheritance in python
#super() allows a child class to access methods from it's parent class even they have their own methods e.g:-
class Animal:
    def __init__(self,name):
        self.name = name#first parent constructor receives name(Tommy) and stores it.
class Dog(Animal):
    def __init__(self,name,breed):#it's accpept both parameters.
        super().__init__(name)#it's calls the parent constructor and send name to the parent's __init__()method
        self.breed =breed
        
dog1 = Dog("Tommy","German Shepherd")
print(dog1.name)
print(dog1.breed)
#it's simple let's understand clealy first dog("tommy","german shepherd") goes and stores in class dog() so name = tommy and breed = german shepherd then super().__init__(name) it's send name to the parent class constructor and as we know that child used parent(Animal) method also so print(dog1.name) and print(dog1.breed) work.
#parent class = superclass = Base class
#child class = subclass = Derived class.
