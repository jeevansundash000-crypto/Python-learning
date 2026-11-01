# import time
# timestamp = time.strftime("%H:%M:%S")
# print("Current Time =", timestamp)
##f strings in python
#Srings formatting is a way to inject variables into strings. There are multiple ways to format strings in python.
letter = ("My name is {1}. I am from {0}")
name = "jeevan"
country = "Nepal"
print(letter.format(country,name))
#it counsmed more time to write and gets confused so we use f strings
# print(f"My name is {name}. I am from {country}")#f strings are faster and easier to write and read
# txt = "The price is only {price:.3f} dollars"#it rounds the price to 2 decimal places
# print(txt.format(price = 49.99999))
# print(f"{2 * 30}")
# name = input("Enter yours name:")
# age = int(input("Enter yours age:"))
# print(f"My name is {name}. I am {age} years old")
# num1 = int(input("Enter yours first numbers:"))
# num2 = int(input("Enter yours second number:"))
# print(f"{num1 + num2}")
age2 = 18
print(f"my age is: {age2>=18}")


