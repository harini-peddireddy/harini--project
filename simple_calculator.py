num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select Operation")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice == 'a':
    print("Result =", num1 + num2)
elif choice == 'b':
    print("Result =", num1 - num2)
elif choice == 'c':
    print("Result =", num1 * num2)
elif choice == 'd':
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Invali division")
else:
    print("Invalid Input")
