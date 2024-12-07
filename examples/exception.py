# program to print the reciprocal of even numbers

num = int(input("Enter a number: "))
try:
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
