# My first simple calculator
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
op = input("Enter +,-,*,/,//,%,**:")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "//":  # float
    print(a // b)
elif op == "%":  # Remainder
    print(a % b)
elif op == "**":  # power of any numbers
    print(a**b)
else:
    print("invalid operation")
