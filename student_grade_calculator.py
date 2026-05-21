name = input("Enter Student Name: ")
marks1 = int(input("Enter Marks in Subject 1: "))
marks2 = int(input("Enter Marks in Subject 2: "))
marks3 = int(input("Enter Marks in Subject 3: "))
total = marks1 + marks2 + marks3
average = total / 3
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
