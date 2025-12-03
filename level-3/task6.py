# Task 5: Count Even Numbers in a List
List = [2, 5, 6, 9, 10, 3, 19, 26, 76, 99, 15, 25]
count = 0
for num in List:
    if (num % 2 == 0):
        count += 1
print(f"The Count is : {count} ")
