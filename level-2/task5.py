attempts = 0
while attempts < 5:
    pwd = input("password: ")
    if pwd == "pavan":
        print("Welcome!")
        break
    attempts +=1
else:
    print("Too many attempts")