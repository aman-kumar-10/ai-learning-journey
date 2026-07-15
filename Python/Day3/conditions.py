### Data types:

age = 21 # integer
name = "Aman Kumar" # string
marks = 89.71 # float
adult = True # bool


### Operators

5+2 
5-2 
5*2 
5/2 
5%2

### Comparision Operators
10 == 10
99 != 100
78 > 76
54 < 51 
54 <= 54 



print("Program 1: \n")
### Conditional Statements

age = 17

if age >= 18:
    print("You can vote.")
else: 
    print("You can't vote.")


print("\n\nProgram 2: \n")

## multiple conditions

income = int(input("Enter Your Annual Income: "))

if income <= 0:
    print("Please enter the correct income")
elif income > 0 and income <= 50000:
    print("You falls in very lower poor class")
elif income > 50000 and income <= 200000:
    print("You falls in poor class")
elif income > 200000 and income <= 1000000:
    print("You falls in middle class")
elif income > 1000000 and income <= 5000000:
    print("You falls in upper middle class")
elif income > 5000000 and income <= 10000000:
    print("You falls in rich class")
elif income > 10000000 and income <= 100000000:
    print("You falls in very rich class")
elif income > 100000000:
    print("You falls in ultra rich class")
else:
    print("Invalid Input.")



print("\n\nProgram 3: \n")
###
input = str(input("Do you know Python? "))

if input == 'yes':
    print("Let's build AI")
else:
    print("Let's learn Python first.")

