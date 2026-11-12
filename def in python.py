##def is used to create our own function basically a reuseable block of code.
def hello():  # here def means i am creating my own function and hello means the name of my function.
    print(
        "Hello all of you"
    )  # this is the block of code that will be executed when we call the function hello.


hello()  # we are calling the function and that print will executed this is important. If we write hello() many times then print() will be executed many times so we didn't need to write print() many times.This process call code reuse.


def hello(name):  # here name is a parameter used to pass value to the fucction hello.
    print("Hello", name)


hello(
    "jeevan"
)  # here jeevan is an argument that is passed to the function hello and it will be printed in the output.


# multiple parameters
def add(a, b):
    print(a + b)


add(1, 2)


# sometimes we want to give the answer back to our program so we use return statement.
def add(c, d):
    return c + d


result = add(8, 1)
print(
    result
)  # basically first add c and d then return will send that result again to that result variable and print will print that result.
print(result * 2)
print(result + 1)  # like that we can do many operation with singel variable


# function with muliple parameters
def introduction(name, age, place):
    print("Hello my name is", name)
    print("I am", age, "years old")
    print("I am from", place)
    print("my name is", name, ".I am from ", place, ".I am ", age, "years old")


introduction(
    "jeevan", 18, "Nepal"
)  # indexing is important here because first jeevan will goes to name but if we writ age first or any thing instead of name then name will be age or something except name.


# function can contain if also
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


a = int(input("Enter a number: "))
check_even_odd(
    a
)  # basically here we input a then a goes to check_even_odd then after at the top inside num and check the condition.


# function can work with list,tuples,set and dict also.
def show_list(mylist):
    print(mylist)


mylist = [1, 2, 3, 4, 5]
show_list(mylist)  # here is also same process repeated.

# import jeevan #here we make a file named jeevan and we call it from another file using import. We can use import like this way also.
# jeevan.welcome()
