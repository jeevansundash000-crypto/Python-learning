#A class is a blueprint or template used to create objects e.g a house is an objects and class is an it's blueprint but it's doesnt' said that it's actual house so class described what an objects should contain. let's learn with e.g
class Student:#this is python keyword used to create a class and Student means our name of class. By convention,class names usually start with a capital letter.
    name = "jeevan" #name,age, grade is the attributes(properties)of our class.At this point we have created an class but not an objects yet.
    age = 18
    grade = 11
#An objects is an actual instance of a class e.g an house, class = house blueprint, objects1= first house,ob2= sec house,ob3= thir house all house can be created using the same blueprint e.g
student1 = Student()#created an objects from the class and student1 is our object. now let's access it's attributes(Data or properties) 
print(student1.name)
print(student1.age)
#we use dot(.) operator to access an object's attributes(data or properties)
#continue in file __init__() in python.py
