import random as r

while True:
    a = int(input("Enter any random number between (1-10): "))
    correct = print("This is the correct number:", r.randint(1, 11))

    if a == r.randint(1, 11):
        print("Congurlation ")
    else:
        print(correct)
        print("Sorry wrong number pls try again.")

    # b = int(input("Enter any random number between (10-20): "))
    # print(r.randint(10,21))
