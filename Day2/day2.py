# TYPE IN PYTHON
print(type("Amar"))
print(type('c'))
print(type(5))
print(type(5.5))
print(type(False))

# when a input is taken it is type string by default
number = int(input("Enter a number "))
print(type(number))

# MATHEMATICS IN PYTHON
print(3*3+3/3-3)
print(3**3)

# BMI
print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip = float(input("What percentage do you want to give the tip? "))
no_of_people = int(input("How many people to split the bill? "))
amount = (total*(1+tip/100)/no_of_people)
print("Each person should pay $", round(amount, 2))
