# control flow statement is basically devide into 3 parts 

# Control Flow Statements

"""
1. Decision / Conditional Statements
   - if
   - if else
   - if elif else
   - match case (switch alternative)

2. Looping Statements
   - for loop
   - while loop

3. Jump Statements
   - break
   - continue
   - return
"""

# 1 . decision / conditional making statement 
age = 20

if age >= 18:
    print("You can vote")

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# python alternate match case 

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")


# Looping Statements

for i in range(5):
    print(i)

i = 1

while i <= 5:
    print(i)
    i += 1

# Jump Statements


# exit the loop completely

for i in range(10):
    if i == 5:
        break
    print(i)

# skip the current iteration 

for i in range(5):
    if i == 2:
        continue
    print(i)

# return some value from the function

def add(a, b):
    return a + b

print(add(5,3))