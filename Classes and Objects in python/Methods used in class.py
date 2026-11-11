##A method is simply a functions defined inside a class e.g:-
class Student:
    
    def __init__(self,name,age):
        self.name = name#self.name access the current objects name e.g student1 name 
        self.age = age
        
    def introduce(self):#introduce() is a method 
        print("My name is ",self.name)
        print("I am ",self.name,"yrs old")
        
student1 = Student("jeevan",18)#indentation is improvements if we changes this line jeevna and 18 interchanging then it will print my name is 18 like that so we should put correct information.
student1.introduce()#callls the method
##The difference betn function and method is:- function is defined independently,called by it's name e.g hello() while method is defined inside a class,usually called through an object e.g student1.inroduce()
##we can change an objects attributes(properties) whenever we want e.g:-
class Jeevan:
    
    def __init__(self,habits,goal):
        self.habits = habits
        self.goal = goal
        
student2 = Jeevan("learning","machine learning")
print(student2.habits)#here it's will gives learning as our habits
student2.habits = "improvements"
print(student2.habits)#it's will gives improvements as our habits because we change it attributes in lines 24 think of it's like a house(jeevan) and attributes(properties) are it's properties we just change house(jeevan) properties. This way we can add a new attribute to an individual object.
#There are two common types of attributes 
#1)Class attributes this are defined directly inside the class,outside it's methods and all objects can access this attribute e.g:-
class Hero:
    school = 'abc school'
 
#2)Instance attributes theses belong to individual objects every objets can have a different name e.g:-
class I:
    def __init__(self,I,ll):
        self.I = I

#let's combine them two 
class Hero:
    school = "abc school"
    
    def __init__(self,person):
        self.person =person
        
st1 = Hero("jeevan")
st2 = Hero("krishna")
print(st1.school)#this two line gives same output cause school is class attributes that can be access by any objects.
print(st2.school)

print(st1.person)#it's will gives different cause we already know.
print(st2.person)

                                                     