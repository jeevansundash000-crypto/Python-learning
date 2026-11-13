#A  Constructor is a special method of a class that initializes an object's attribute(properites) when an object is created e.g:-
class Student:#Student is our class.
    
    def __init__(self):
        print("Student object created")
        
student1 = Student()#it's created an object.
#When we created the object, python automatically calls the __init__() method. we don't need to call it manually.
#So, A constructor is like a setup process that runs when a new object is created.
#__init__() is a special method in python and it's also called an initializer as we already previous discuss.

##Basically we need constructor to initalizes each objects information when it's created suppose we want to store information in different objects we can do it without using __init__() but it's may takes more time and we have to asssign the attributes(properties or values)separetely for every objects but using __init__() it's much easier so we use constuctor to initilaizes every objects information.
#An constructor can used for storing multiple parameters as we needed e.g:-
#def __init__(self,name,age,place,birth,death,shool): and many more.
#we can also create our own methods inside the class to use those attributes e.g:-
class Student:
    
    def __init__(self,name,age):#this constructos initializes the data,while show_details() displays the data.
        self.name = name
        self.age = age
    def show_details(self):#our own methods and it's also used that same attributes that we put inside the class Student.
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        
std1 = Student("jeevan",18)
std1.show_details()

#Default values in constructors: what happens if we dont' want to provide every value while creating an object? we can use default parameters e.g:-
class Place:
    def __init__(self,famous,my_famous_place = "Belbari"):
        self.famous = famous
        self.my_famous_place = my_famous_place
aa1 = Place("ktm")#as we can see the output aa1 receives the default my_famous_place = Belbari 
aa2 = Place("Radhnagar","Bahuni")#but aa2 receives Bahuni as in place of my_famous_place because we provided it 

print(aa1.famous,aa1.my_famous_place)
print(aa2.famous,aa2.my_famous_place)
#importanat parameters with default value should generally come after parameters without default values e.g:-
# def __init__(self,name = "jeevan",age):
    # pass#this is mistakes because default value come first which gives an syntexError 
# def __init__(self,age,name = "jeevan"):
#   pass #correct one.

