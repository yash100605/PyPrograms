a = int(input("Enter Number 1:\n"))
b = int(input("Enter Number 2:\n"))
c = input("Enter the Operation:\n")

if c == "+":
    print("The Addition is:", a + b)
elif c == "-":
    print("The Subtraction is:", a - b)
elif c == "*":
    print("The Multiplication is:", a * b)
elif c == "/":
    if b == 0:
        print("Not Divisible")
    else:
        print("The Division is:", a / b)
else:
    print("Invalid Syntax")


