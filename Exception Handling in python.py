##We use Try Except Code to handle error in python
a = input("Enter your number: ")
print(f"Multiplication table of {a} is ")
for i in range(1, 11):
    print(
        f"{int(a)} X {i} = {int(a)*i}"
    )  ##from here every thing and code is fine and perfectly run
##suppose we wrote a long code and suddenly it's show error due to one line code mistakes then other below code also not be excuated so we use try except code which allows users to try any long code inside try: so when errors come any particular code then python show errors only
b = input("Enter your number: ")
print(f"Multiplication table of {b} is ")
try:

    for x in range(1, 11):
        print(f"{int(b)} X {x} = {int(a)*x}")
except Exception as e:  # we can write like this also
    print(e)
# except:  # this also can be used
# print("Invalid Input")


# print(
# "Code is error"
# )  # now if we put character as a input instead intergers then from that try to except it's show except print then down code will countinu run
# print(
# "Code is broken"
# )  # using try if any code line is mistakes then that line shows what we print in except after that down the except or try others code line will run without stops.
##means normally if any line get's wrong then whole results shows error even others code are right but using try only that line shows errors and others lines run without being affected by errors line or code
# try:
#     d = int(input("Enter an integer:"))
#     e = [1, 2]
#     print(e[d])
# except ValueError:
#     print("Number is not an integer")  # if we didn't put integer then this will show.
# except IndexError:
#     print(
#         "Out of range index"
#     )  # if we put wrong or not exist index then this will show.
# else:
#     print(
#         "you are going well"
#     )  # we can use else also if no error came then else will be excuated, other wise no.
# finally:
#     print(
#         "program ended"
#     )  ##finally runs wheather there is an error or not means if error then run if not then also run, but else is written first then finally.
# ##using except we can handle multiple differents types of errors such as ValueError,IndexError
# ##ZeroDivisionError means trying to divide by zero which is not possible
# ##TypeError means combining different data types such as "hello"+5 which is not possible
# ##IndexError means trying to access an index that doesn't exist
# ##KeyError means trying to access a dictionary key that doesn't exist
# ##NameError means using a variable that doesn't exist
# ##except ValueError as error: #as error means store the error object inside the variable error.
# ##Custom error
# # age = 18
# # if age<20:
# # raise ValueError("You must be 20 or older")#here raise means we can also create our own error using it
# b = int(input("Enter the number between 5 and 9:"))
# if b<5 or b>9:
#     raise ValueError("Number should be between 5 and 9")
# class jeevan(Exception):  # we are making our own error of our own name
# pass


# try:
# a = int(input("Enter your number: "))
# if a > 9:
# raise jeevan("Invalid number")
# except ValueError:
# print("Value is wrong")
