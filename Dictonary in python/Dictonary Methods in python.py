##Dictionary is like a real dictionary real life whereeach words has it's own meaning in python it's just like same
students = {
    "name": "jeevan",
    "age": 17,
    "class": 11,
}  # here students is a dictionary, name is word or key and jeevan is meaning or value of it
print(students)
print(students["name"])
print(students["age"])
# print(students["jeevan"])#here  it's gives an error because name is like a locker label and jeevan is the thing inside it we can open the locker using the label but jeevan is the thing inside the locker not it's label so thils
print(students["class"])  # method 1
print(students.get("age"))  # method 2 #this also we can use to access dictionary
print(students["class"])
print(students.get("class"))
print(students.keys())  # method 1
for key in students.keys():  # method 2
    print(students[key])
print(students.values())
print(students.items())  # used to access or see all the keys and it's value
# we can do like this also
for keys, value in students.items():
    print(f"The value of {keys} is {value})")  # here we use f-strings
# Way to create a empty dictionary
s = {}
print(s)
##Method used in dictionary
st = {111: 2, 222: 3, 333: 4, 444: 5}
# update()#just like before sets
# students.update(st)
# print(students)
# clear()
# st.clear()
# print(st)
##pop()-used to delete any key
# st.pop(111)
# print(st)
##popitem()-used to remove last key of the dict
# st.popitem()
# print(st)
##del- means delete the dict items
# del st()#can delete the entire dict but this code show error
del st[111]  # using this can only delete 111 key
print(st)
hello 