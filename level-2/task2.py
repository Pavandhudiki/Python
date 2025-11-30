# Task 2: Find the Largest of Three Numbers
a = int(input("enter first numbber: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if (a >= b and a >= c):
    print(f" Largest = {a} ")
elif(b >= a and b >= c):
    print(f" Largest = {b}")
else:
    print(f" Largest = {c}")
