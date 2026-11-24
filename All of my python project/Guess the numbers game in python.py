import random as r

while True:
    a = int(input("Enter any random number between (1-11): "))
    correct = print("This is the correct number:", r.randint(1, 11))

    if a == correct:
        print("Congurlation ")
    else:
        print("Sorry wrong number pls try again.")

    # b = int(input("Enter any random number between (10-20): "))
    # print(r.randint(10,21))
