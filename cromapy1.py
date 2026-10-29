"""
a = 100
b = 200
c = a+b
print(c)

name = input("what's your name: ")
print("welcome",name)

a = int(input("number: "))
print(a)

a = int(input("First number:"))
b = int(input("Second number:"))
print(a)
print(b)


name = 'Abhinav'
age = 24
print(f"My name is {name} and age is {age}")


# Exercise 1: WAP to calculate the gross salary of an employee
# where HRA is 20% and DA is 30% of his basic salary....HINT: Gross_salary = Basic_Salary+HRA+DA

bs = float(input("Enter Basic Salary: "))
hra = bs*0.20
da = bs*0.30
gs = bs+hra+da
print("Gross Salary: ",gs)

#Q1: Take a name as input and print --- Welcome <name>
name = input("Name: ")
print(f'Welcome {name}')

#Q2: Take a number as input and print it.
num = input("Enter a number: ")
print(num)

#Q3: Take two number as input and print both number on seperate line
a = input("Enter first number: ")
b = input("Enter second number: ")
print(a)
print(b)

#Q4:Take name and age as input and print: My name is ___ and age is ____
name = input("Your Name: ")
age = int(input("Your Age: "))
print(f"My name is {name} and age is {age}")

===============================================INTEGER==========================================
#Q5: Take an integer as input and print it's square
num = int(input("Enter Number: "))
square = num*num
print(square)

#Q6: Take two integer as input and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"sum of two integer : {sum}")

#Q7: Take two integer as input and print - Addition,Substraction,Multiplication
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
add = num1 + num2
sub = num1 - num2
multi = num1 * num2
print(f"Addition: {add}")
print(f"Substraction: {sub}")
print(f"Multiplication: {multi}")

#Q8: Take a number and print: The number entered is <number>
num = int(input())
print(f"The number entered is {num}")

#Q9: Take an integer and print it's double.
num = int(input("Number: "))
double = num * 2
print(f"Double Number: {double}")

================================================FLOAT===========================================
#Q10: Take a float value as input and print it.
num = float(input("Number: "))
print(num)

#Q11: Take two float number and print there sum.
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
sum = num1 + num2
print(f"Sum of two number: {sum}")

#Q12: Take a float number and print it's half.
num = float(input("Number: "))
half = num/2
print(f"Half Number: {half}")

#Q14: Take length and breadth(float) as input and print Area of Rectangle.
length = float(input("Length of Rectangle: "))
breadth = float(input("Breadth of Rectangle: "))
area = length*breadth
print(f"Area of Rectangle: {area}")

#Q15: Take redius float input and print the area of a circle.
r = float(input("Radius: "))
pi = 3.14
area = pi*r*r
print(f"Area of circle: {area}")

===================================================Mix INT & FLOAT========================================
#Q16: Take one integer and one float as input and print both.
num1 = int(input("Integer: "))
num2 = float(input("Float: "))
print(f"Here is integer number: {num1} and here is float number: {num2}")

#Q17: Take total marks (int) and number of subjects (int) and print the average as float.
subject = int(input("Number is subject: "))
total_marks = int(input("Total Marks: "))
avg = float(total_marks/subject)
print(f"Average: {avg}")

#Q18: Take price (float) and quantity (int) and print the total cost.
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total_cost = price*quantity
print(f"Total Cost: {total_cost}")

#Q19: Take two numbers (one int, one float) and print their sum.
num1 = int(input("Integer Number: "))
num2 = float(input("Float Number: "))
sum = num1+num2
print(f"Sum: {sum}")
"""

#Q20: Take salary (float) and bonus (int) and print the final salary.
salary = float(input("Salary: "))
bonus = int(input("Bonus: "))
final_salary = salary+bonus
print(f"Final Salary: {final_salary}")


