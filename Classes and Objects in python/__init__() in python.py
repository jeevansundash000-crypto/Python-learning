#we can create multiple objects imagine we have three students. we don't need to create three separate classes we can create three objects using one class e.g
# student2 = Student()
# student3 = Student()
# print(student2.name)
# print(student3.name)#we can do like this but it gives same result name,age,grade is same for all objects so what if we want differnt names and ages for all differnt students so we use __init__().
#__init__() an important parts of python classes and is a special method that python automatically calls when a new objects is created e.g:-
class Student:
    
    def __init__(self,name,age):#here we define __init__ as self(either std1 or std2),name,age
        self.name= name#here self(either std1 or std2).name it's simple like std1.name
        self.age=age
        
student1= Student("jeevan",18)#here when python executes this line then it create a new objects and calls __init__() with that object and the supplied arguments. And the value are assigned like this: self name = "jeevan" ,self age = 18 and same for student2 also and when creating std1 self refers to std1 and when creating std2 self refers to std2 and we don't need to pass self for boths like manually python automatically pass it
student2=Student("Aashish",17)

print(student1.name)
print(student2.age)

print(student2.name)
print(student2.age)
#self refers to the current object e.g in line 9 there is self means self(student1 and student2),name,age

