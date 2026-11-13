#At the beginner level, we commonly hear about two types of constructors they are:-
#1)Non-parameterized constructor it's doesn't accept additional arguments(apart from self).
class Car:
    
    def __init__(self):#it's doesn't accept additional arguments like name,age.
        self.brand = "TaTa"
        self.colour = "Black"
        
car1 =Car()

print(car1.brand)
print(car1.colour)
#here the values are already provided inside the constructor.

#2)Parameterized construtor it's accept arguments to initialize an object.
class Cars:
    def __init__(self,brands,colours):#looks it's accepted multiple arguments and this types are simple as we already know.
        self.brands = brands
        self.colours = colours
        
car2 =Cars("Honda","Blue")
print(car2.brands)
print(car2.colours)

##we can't make multiple costructors in one class e.g:-
class Hero:
    def ___init__(self,):
        print("first constructor")
    def __init__(self,name):
        print("second construtor")#this is print cause the sec definition replaces the first one means in place of first, sec came
ab = Hero("jeevan")

        
