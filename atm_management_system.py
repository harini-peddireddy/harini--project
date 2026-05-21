balance = 5000
print("ATM MENU")
print("a. Check Balance")
print("b. Deposit Money")
print("c. Withdraw Money")
choice = input("Enter your choice: ")
if choice == 'a':
    print("Your Balance =", balance)
elif choice == 'b':
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Updated Balance =", balance)
elif choice == 'c':
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")
