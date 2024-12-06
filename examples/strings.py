name = 'Prasad'
age = 22
height = 5.2

print(f"My name is {name}. Iam {age} years old.My height is {height} meters")
print(f"My fathers's age is {age*2}")

--> write a program to find how many Days,Weeks,Months you have to cross 100 years
```
age = int(input("Enter your age: "))

years_left = 100 - age
days_left = years_left * 365       //(365 means in 1 year we have 365 days)
weeks_left = years_left * 52       //(52 means in 1 year we have 52 days)
months_left = years_left * 12      //( 12 means in 1 year we have 12 months)

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months, {years_left} years")

```


