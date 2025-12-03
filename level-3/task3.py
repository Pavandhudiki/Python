# Task 3: Create a Function to Check if a Number is Even or Odd

n =  int(input("Enter number: "))
def Even_Odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = Even_Odd(n)
print(f"{result} Number")
