# Lambda functions in python is very useful to write an anonymous functions means a functions which don't have any name and have expressions, we can write in a single expression without using def e.g
def double(x):
    return x * 2


print(double(5))  # it's will gives 10 as we know but we can write it like this also
double = (
    lambda x: x * 2
)  # here lambda is a functions that takes x and return x*2 and it's same as above code but just style is different and this is about lambda functions.

print(double(5))
# lambda makes a fuctions as a variables and use it's as a functions. It's is a shortway to write a code e.g above def is in 2 line but here only line and this how it's work.
avg = lambda x, y: (x + y) / 2
print(avg(2, 4))  # we can do like this also for multiple arguments.
avg1 = lambda x, y, z: (x + y + z) // 2
print(avg1(1, 2, 3))  # this one also.


# we can pass functions to functions also e.g
# def cube(x):
# return x*x*x#we should do like this first
def appl(fx, value):
    return 1 + fx(value)


# print(appl(cube, 2))#if we don't define cube then it's will give's an error but we already define it. This is a long method so
print(
    appl(lambda x: x * x * x, 2)
)  # here we directly pass functions to functions directly we should need to define a separate def
