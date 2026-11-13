#An constructor contain conditions statements also e.g if elif and else e.g:-
class Student:
    def __init__(self,name):
        if name == "jeevan":
            self.names = "Correct name"
        else:
            self.names = "Incorrect name"
std1 = Student("jeevan")
print(std1.names)