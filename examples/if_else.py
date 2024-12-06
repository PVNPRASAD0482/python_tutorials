```
age = int(input("Enter the age : "))

if(age >= 18):
    print("apply for the vote")
else:
    print("Don't apply for the vote")
```
```
num = int(input("Enter a Number: "))

if(num % 2 == 0):
    print("It is a Even number")
else:
    print("It is a Odd number")
```

**Nested-if**
    
height = int(input("Enter your height: "))

if(height >= 4):
    print("you can ride")
    age = int(input("Enter your age: "))
    if(age < 10):
        print("please pay 150 rupees")
    elif(age <= 18):
        print("please pay 300 rupees")
    else:
        print("please pay 500 rupees")
else:
    print("you can't ride")
    print("Bye")
