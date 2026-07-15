print("*** Program 1: ***\n")
### *** Store the variables and print them:

name = "Amn Devv"
age = 22
salary = 25000
role = "AI Developer"

print("Name: " + name) # using concatination
print(f"Age: {age}") # use the value inside inverted commas
print(f"Salary: {salary}")
print("Role: " + role)

print("\nUsing single line print: ")

print(f"Name: {name} \nAge: {age} \nSalary: {salary} \nRole: {role}") # single line print



print("\n\n*** Program 2: ***\n")
### *** User Input

name = input("Enter your name: ")
print(f"Hello, {name} \nWelcome here, have a good day!")


print("\n\n*** Program 3: ***\n")
## calculations

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

action = input("Enter the action (eg: +, -, * , /, %): ")

res = ''

if action == '+':
    res = f"Addition: {num1+num2}"
elif action == '-':
    res = f"Subtration: {num1-num2}"    
elif action == '*':
    res = f"Multiplication: {num1*num2}"    
elif action == '/':
    res = f"Division: {num1/num2}"    
elif action == '%':
    res = f"Modulus: {num1%num2}"    
else: 
    res = 'Invalid action'

print(res);


print("\n\n*** Program 4: ***\n")
##
flang = input("What is you favorite programming language? ")
print(f"Your favorite programming language is '{flang}'")

role = input("What AI role do you want? ")
print(f"Answer: {role}")



### *** 