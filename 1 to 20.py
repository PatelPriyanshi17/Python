'''Section 1: Python Fundamentals'''

'''Task 01: Employee Salary Calculator
Problem Statement
Create a Python program that accepts an employee's name, basic salary, allowances, and deductions as input.

Calculate and display:

Employee name
Basic salary
Total allowances
Gross salary
Total deductions
Net salary
Calculation Rules
Gross Salary = Basic Salary + Total Allowances
Net Salary = Gross Salary - Total Deductions'''

# Employee_Name=input("Employee Name:")
# Basic_Salary=float(input("Basic Salary:"))
# allowances=float(input("allowances:"))
# deductions=float(input("deductions:"))
# Gross_Salary =Basic_Salary +allowances
# Net_Salary = Gross_Salary - deductions

# print("Employee Name:",Employee_Name)
# print("Basic_Salary:",Basic_Salary)
# print("Total Allowances:",allowances)
# print("Gross Salary:",Gross_Salary)
# print("Total Deductions:",deductions)
# print("Net Salary:",Net_Salary)

'''Task 02: Student Result Management
Problem Statement
Create a program that accepts a student's name and marks in five subjects.

Calculate the total marks, percentage, and final grade.

Grading Criteria
Percentage	Grade
90% and above	A+
75% to below 90%	A
60% to below 75%	B
40% to below 60%	C
Below 40%	Fail
Assume each subject carries a maximum of 100 marks.

Requirements
Accept the student's name.
Accept marks in five subjects.
Calculate total marks out of 500.
Calculate the percentage.
Determine the grade using conditional statements.
Display the student's result.
Concepts Covered
Variables, input/output, arithmetic operators, if-elif-else, comparison operators, logical operators.

'''
# Student_name=input("Enter Student name:")

# sub1=float(input("Enter Subject 1 Marks: "))
# sub2=float(input("Enter Subject 2 Marks: "))
# sub3=float(input("Enter Subject 3 Marks: "))
# sub4=float(input("Enter Subject 4 Marks: "))
# sub5=float(input("Enter Subject 5 Marks: "))
# total_Marks=sub1+sub2+sub3+sub4+sub5
# percentage=(total_Marks/500)*100

# if percentage>=90:
#     grade= "A+"
# elif percentage>=75:
#     grade="A"
# elif percentage>=60:
#     grade="B"
# elif percentage>=40:
#     grade="C"
# else:
#     grade="fail"

# print("\n-------Students Result:--------")
# print("Student Name:",Student_name)
# print("total_marks:",total_Marks)
# print("percentage:",percentage)
# print("grade:",grade)

'''Task 03: Number Analysis Tool
Problem Statement
Create a program that accepts an integer and analyzes the number.

Requirements
Determine whether the number is:

Positive, negative, or zero.
Even or odd.
Divisible by 3.
Divisible by 5.
Divisible by both 3 and 5.'''
# num=int(input("Enter number:"))
# # Positive, negative, or zero
# if num>0:
#     number_type="Positive"

# elif num<0:
#     number_type="Negative"

# else:
#     number_type="zero"

# # Even or odd 
# if num%2 ==0:
#     parity="Even"

# else :
#     parity="Odd"

# # divisible by 3 
# if num%3 ==0:
#     div3="Yes"
# else:
#     div3="No"

# # divisible by 5
# if num%5==0:
#     div5="yes"
# else:
#     div5="No"

# # Divisible by both 3 and 5.'''
# if num%3==0 and num%5==0:
#     both="yes"
# else:
#     both="No"

# print("\nnumber:",num)
# print("Type:",number_type)
# print("partiy:",parity)
# print("divDivisible 3:",div3)
# print("divDivisible 5:",div5)
# print("Divisible by both 3 and 5:",both)

'''Task 04: Electricity Bill Calculator
Problem Statement
Create a program that calculates an electricity bill based on the number of units consumed.

Electricity Tariff
Consumption Slab	Rate
First 100 units	₹5 per unit
Next 100 units	₹7 per unit
Above 200 units	₹10 per unit
Apply the rates progressively.

For example, if a customer consumes 250 units:

First 100 units: 100 × ₹5 = ₹500
Next 100 units: 100 × ₹7 = ₹700
Remaining 50 units: 50 × ₹10 = ₹500
Total Bill = ₹1,700

Requirements
Accept the customer's name.
Accept the total units consumed.
Calculate the bill using the given slabs.
Display the units consumed and the final bill.
Reject negative unit consumption.
Concepts Covered
Input/output, conditional statements, arithmetic operators, comparison operators'''

# Customer_Name=input("Enter Customer Name:")
# Units=float(input("Enter Unit:"))
# if Units<0:
#     print("Invalid Input! Units cannot be negative.")
# elif Units<=100:
#     bill=5*100
   
# elif Units<=200:
#     bill=(5*100)+((Units-100)*7)
   
# elif Units<=200:
#     bill=((100 * 5) + (100 * 7) + ((Units - 200) * 10))
    

# print("Enter Customer Name",Customer_Name)
# print("Enter Unit:",Units)
# print("Total Bill:",bill)

'''Section 2: Loops and Number Problems'''
'''Task 05: Multiplication Table Generator
Problem Statement
Create a program that generates the multiplication table of a number entered by the user.

Requirements
Accept a number.
Print its multiplication table from 1 to 10.
Extend the program to accept a custom ending multiplier.
Display each multiplication in a readable format.
Example Input
Enter a number: 7
Enter ending multiplier: 5
Expected Output
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
Concepts Covered
For loops, range(), input/output, variables, arithmetic operators.'''

# Number=int(input("Enter a Number:"))
# ending=int(input("Enter ending multiplier:"))
# for i in range(1,ending+1):
#     print(Number,"x",i,"=",Number*i)


'''Task 06: Digit Statistics Calculator
Problem Statement
Create a program that accepts a positive integer and calculates statistics about its digits.

Requirements
Calculate:

Sum of all digits.
Number of digits.
Reversed number.
Largest digit.
Smallest digit.

Example Input
Enter a positive integer: 4826
Expected Output
Digit Sum: 20
Digit Count: 4
Reversed Number: 6284
Largest Digit: 8
Smallest Digit: 2
Additional Requirement
Solve the problem using a while loop and arithmetic operators. Do not convert the number into a string for digit processing.

Concepts Covered
While loops, integer division, modulo operator, arithmetic operators, type conversion.

'''

# number = int(input("Enter a positive integer: "))

# temp = number
# digit_sum = 0
# digit_count = 0
# reversed_number = 0
# largest_digit = 0
# smallest_digit = 9

# while temp > 0:
#     digit = temp % 10

#     digit_sum += digit
#     digit_count += 1
#     reversed_number = reversed_number * 10 + digit

#     if digit > largest_digit:
#         largest_digit = digit

#     if digit < smallest_digit:
#         smallest_digit = digit

#     temp = temp // 10

# print("Digit Sum:", digit_sum)
# print("Digit Count:", digit_count)
# print("Reversed Number:", reversed_number)
# print("Largest Digit:", largest_digit)
# print("Smallest Digit:", smallest_digit)

'''Task 07: Prime Number Checker
Problem Statement
Create a program that checks whether a number is prime.

A prime number is a positive integer greater than 1 that has exactly two positive divisors: 1 and itself.

Requirements
Accept an integer.
Check whether it is prime.
Display an appropriate message.
Extend the program to print all prime numbers between 1 and a user-provided limit.
Example Input
Enter a number: 17
Expected Output
17 is a prime number.
Additional Challenge
Accept a limit of 50 and display all prime numbers from 1 to 50.

Concepts Covered
For loops, nested iteration, conditional statements, modulo operator, Boolean logic.

'''
# num=int(input("Enter a number:"))
# if num>1:
#     is_prime=True

#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# else:
#     print(num,"is not a prime numbers")

''' 50 limit and display '''
# limit=int(input("Enter limit number:"))
# for num in range(2,limit+1):
#     is_prime=True

#     for i in range(2,num):
#         if num % i == 0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num, end=" ")

# limit = int(input("Enter the limit: "))

'''Task 08: Pattern Printing
Problem Statement
Create a program that prints different patterns using nested loops.

Pattern 1: Right-Angled Star Triangle
For four rows, the output should be:

*
**
***
****
Pattern 2: Inverted Star Triangle
For four rows, the output should be:

****
***
**
*
Pattern 3: Number Triangle
For four rows, the output should be:

1
12
123
1234
Pattern 4: Repeated Number Triangle
For four rows, the output should be:

1
22
333
4444
Requirements
Accept the number of rows from the user.
Print all four patterns.
Use nested loops instead of directly printing each row.
Concepts Covered
Nested loops, range(), print(), variables, iteration.

'''
# rows=int(input("Enter number of rows:"))
# print("\n Pattern 1: Right-Angled Star Triangle ")
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# print("\n Pattern 2: Inverted Star Triangle ")
# for i in range(rows,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# print("\n Pattern 3: Number Triangle")
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# print("\n Pattern 4: Repeated Number Triangle")
# for i in range(1,rows+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()


'''Section 3: Strings and Collections'''

'''Task 09: Text Analyzer
Problem Statement
Create a program that analyzes a sentence entered by the user.

Requirements
Calculate:

Total characters, including spaces.
Total words.
Total vowels.
Total consonants.
Total digits.
Total spaces.
Total uppercase letters.
Total lowercase letters.
Ignore case when counting vowels and consonants.

For this task, count English alphabetic characters as letters. Ignore punctuation when counting vowels and consonants.

Example Input
Python is Fun 123
Expected Output
Total Characters: 17
Total Words: 4
Total Vowels: 4
Total Consonants: 7
Total Digits: 3
Total Spaces: 3
Concepts Covered
Strings, string methods, indexing, loops, conditions, character checking.'''

# text = input("Enter a sentence: ")

# characters = len(text)
# words = len(text.split())

# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# uppercase = 0
# lowercase = 0

# for ch in text:
#     if ch.lower() in "aeiou":
#         vowels += 1

#     elif ch.isalpha():
#         consonants += 1

#     if ch.isdigit():
#         digits += 1

#     if ch == " ":
#         spaces += 1

#     if ch.isupper():
#         uppercase += 1

#     if ch.islower():
#         lowercase += 1

# print("Total Characters:", characters)
# print("Total Words:", words)
# print("Total Vowels:", vowels)
# print("Total Consonants:", consonants)
# print("Total Digits:", digits)
# print("Total Spaces:", spaces)
# print("Total Uppercase Letters:", uppercase)
# print("Total Lowercase Letters:", lowercase)


'''Task 10: Palindrome and Word Reversal
Problem Statement
Create a program that performs two string operations.

Part A: Palindrome Checker
Accept a word or phrase and determine whether it is a palindrome.

A palindrome reads the same forward and backward when case, spaces, and punctuation are ignored.

Examples:

madam is a palindrome.
racecar is a palindrome.
A man, a plan, a canal: Panama is a palindrome.
python is not a palindrome.
Part B: Reverse Every Word
Accept a sentence and reverse each word while keeping the original word order unchanged.

Example Input
Python is fun
Expected Output
nohtyP si nuf
Requirements
Implement the palindrome check.
Reverse every word in a sentence.
Preserve the original order of words.
Use string slicing, loops, and string methods.
Concepts Covered
Strings, slicing, split(), join(), loops, string methods, conditional statements.'''

# palindrome
# text=input("Enter a Word sentence:")
# clean_text=""
# for char in text:
#     if char.isalnum():
#         clean_text+=char.lower()

# if clean_text==clean_text[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# Reverse Every Word
# sentence = input("Enter a sentence: ")

# words = sentence.split()
# reversed_words = []

# for word in words:
#     reversed_words.append(word[::-1])

# result = " ".join(reversed_words)

# print("Reversed sentence:", result)

'''Task 11: Sales Data List Analysis
Problem Statement
A retail store records its daily sales values in a list.

Analyze the sales data and generate a summary report.

Sample Data
daily_sales = [1200, 1800, 950, 2400, 1600, 2100]
Requirements
Calculate:

Total sales.
Average daily sales.
Highest sale.
Lowest sale.
Number of days with sales above the average.
Number of days with sales below the average.
Number of days with sales equal to the average.
Expected Output
Total Sales: 10050
Average Sales: 1675
Highest Sale: 2400
Lowest Sale: 950
Days Above Average: 3
Days Below Average: 3
Days Equal to Average: 0
Additional Requirement
Allow users to enter their own sales values.

Concepts Covered
Lists, loops, aggregation, sum(), min(), max(), len(), comparison operators'''
# sales=[]
# n=int(input("Enter Number of Days:"))
# for i in range(n):
#     sale=int(input("Enter Sales:"))
#     sales.append(sale)

# total_sales=sum(sales)
# average_sales=total_sales/len(sales)
# highest_sales=max(sales)
# lowest_sales=min(sales)

# above_average=0
# below_average=0
# equal_average=0
# for sale in sales:
#     if sale>average_sales:
#         above_average+=1
#     elif sale<below_average:
#         below_average+=1
#     else:
#         equal_average+=1

# print("Total Sales:", total_sales)
# print("Average Sales:", average_sales)
# print("Highest Sale:", highest_sales)
# print("Lowest Sale:", lowest_sales)
# print("Days Above Average:", above_average)
# print("Days Below Average:", below_average)
# print("Days Equal to Average:", equal_average)

'''Task 12: Remove Duplicates and Find Common Values
Problem Statement
Two classes have lists of student IDs. Analyze the lists to identify unique and common students.

Sample Data
class_a = [101, 102, 103, 104, 105, 102]
class_b = [104, 105, 106, 107, 104]
Requirements
Create a list of unique IDs from both classes.
Find IDs common to both classes.
Find IDs present only in Class A.
Find IDs present only in Class B.
Remove duplicates while preserving the original order in the unique list.
Expected Output
Unique Student IDs: [101, 102, 103, 104, 105, 106, 107]
Common IDs: [104, 105]
IDs Only in Class A: [101, 102, 103]
IDs Only in Class B: [106, 107]
Concepts Covered
Lists, sets, membership operators, loops, set operations, duplicate removal.'''


# class_a = [101, 102, 103, 104, 105, 102]
# class_b = [104, 105, 106, 107, 104]

# 1. Unique IDs, preserving original order
# unique_ids = []

# for student_id in class_a + class_b:
#     if student_id not in unique_ids:
#         unique_ids.append(student_id)

# 2. Common IDs
# common_ids = []

# for student_id in class_a:
#     if student_id in class_b and student_id not in common_ids:
#         common_ids.append(student_id)

# 3. IDs only in Class A
# only_a = []

# for student_id in class_a:
#     if student_id not in class_b and student_id not in only_a:
#         only_a.append(student_id)

# 4. IDs only in Class B
# only_b = []

# for student_id in class_b:
#     if student_id not in class_a and student_id not in only_b:
#         only_b.append(student_id)

# print("Unique Student IDs:", unique_ids)
# print("Common IDs:", common_ids)
# print("IDs Only in Class A:", only_a)
# print("IDs Only in Class B:", only_b)

'''Task 13: Student Marks Management
Problem Statement
Store student names and their marks in a dictionary. Analyze the class performance.

Sample Data
student_marks = {
    "Aarav": 85,
    "Diya": 92,
    "Rahul": 76,
    "Priya": 89,
    "Karan": 67
}
Requirements
Display every student's name and marks.
Calculate the class average.
Find the topper.
Identify all students scoring above the class average.
Identify students scoring below 40 marks.
Display the number of students in the dictionary.
Additional Challenge
If multiple students have the highest marks, display all of them.

Concepts Covered
Dictionaries, keys(), values(), items(), loops, conditional statements, aggregation.'''
# student_marks = {
#     "Aarav": 85,
#     "Diya": 92,
#     "Rahul": 76,
#     "Priya": 89,
#     "Karan": 67
# }
# for name,marks in student_marks.items():
#     print(name,":",marks)

# total_marks=sum(student_marks.values())
# total_students=len(student_marks)
# average=total_marks/total_students

# print("Class Average:",average)

# highest_marks=max(student_marks.values())
# print("Highest_Marks:",highest_marks)

# for name,marks in student_marks.items():
#     if marks== highest_marks:
#         print(name)

# print("Above Average Students:")
# for name,marks in student_marks.items():
#     if marks>average:
#         print(name,":",marks)

# print("Students Below 40 Marks:")
# for name,marks in student_marks.items():
#     if marks>40:
#         print(name,":",marks)

# print("total Students:",total_students)

'''Task 14: Product Inventory System
Problem Statement
Create a product inventory system using a nested dictionary.

Each product should contain its name, price, and available quantity.

Sample Data
inventory = {
    "P101": {
        "name": "Keyboard",
        "price": 800,
        "quantity": 10
    },
    "P102": {
        "name": "Mouse",
        "price": 500,
        "quantity": 3
    },
    "P103": {
        "name": "Monitor",
        "price": 7500,
        "quantity": 6
    },
    "P104": {
        "name": "Headphones",
        "price": 1200,
        "quantity": 4
    }
}
Requirements
Display all product details.
Calculate the stock value of each product.
Calculate the total inventory value.
Identify products with fewer than five units in stock.
Find the product with the highest stock value.
Display the total number of product types.
Stock Value = Product Price × Available Quantity

Concepts Covered
Nested dictionaries, loops, dictionary access, arithmetic operators, conditional statements.'''
# inventory = {
#     "P101": {
#         "name": "Keyboard",
#         "price": 800,
#         "quantity": 10
#     },
#     "P102": {
#         "name": "Mouse",
#         "price": 500,
#         "quantity": 3
#     },
#     "P103": {
#         "name": "Monitor",
#         "price": 7500,
#         "quantity": 6
#     },
#     "P104": {
#         "name": "Headphones",
#         "price": 1200,
#         "quantity": 4
#     }
# }
# for product_id,detils in inventory.items():
#     print(product_id,detils["name"],detils["price"],detils["quantity"])

# total_value=0
# for product_id,detils in inventory.items():
#     stock_value=detils["price"]*detils["quantity"]
#     print(detils["name"],"Stock value",stock_value)
#     total_value+=stock_value

# print("Total inventory value: ",total_value)

# print("Products with Low Stock:")
# for product_id,detils in inventory.items():
#     if detils["quantity"]<5:
#         print(detils["name"])

# highest_value=0
# highest_product=""

# for product_id, details in inventory.items():
#     stock_value = details["price"] * details["quantity"]

#     if stock_value>highest_value:
#         highest_value=stock_value
#         highest_product=details["name"]
# print("Highest Stock Value Product:", highest_product)
# print("Highest Stock Value:", highest_value)

# print("Total Product Types:", len(inventory))

'''Section 4: Functions and Reusable Programs'''
'''Task 15: Reusable Calculator
Problem Statement
Build a calculator using separate functions for each arithmetic operation.

Requirements
Create the following functions:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
The program should:

Accept two numbers.
Ask the user to select an arithmetic operator.
Call the appropriate function.
Return and display the result.
Handle division by zero.
Display an error message for an invalid operator.
Example Input
Enter first number: 20
Enter second number: 5
Enter operator (+, -, *, /): /
Expected Output
Result: 4.0
Concepts Covered
Function definition, parameters, arguments, return statements, function calls, conditional statements.'''
# def add(a,b):
#     return a+b 

# def subtract(a, b):
#     return a-b

# def multiply(a, b):
#     return a*b

# def divide(a,b):
#     if b==0:
#         return "cannot divide by zero"
#     return a/b
# num1=int(input("Enter first Number:"))
# num2=int(input("Enter Secound Number:"))

# operator=input("Enter operator(+,-,*,/):")
# if operator=="+":
#     result=add(num1,num2)
#     print("Result:",result)

# elif operator=="-":
#     result=subtract(num1,num2)
#     print("result:",result)

# elif operator == "*":
#     result = multiply(num1, num2)
#     print("Result:", result)

# elif operator == "/":
#     result = divide(num1, num2)
#     print("Result:", result)
# else:
#     print("Invaild Operator")

'''Task 16: Reusable Statistics Functions
Problem Statement
Create reusable functions to calculate common statistical measures for a list of numbers.

Requirements
Write separate functions to calculate:

Mean.
Median.
Minimum value.
Maximum value.
Range.
Function Expectations
calculate_mean(numbers)
calculate_median(numbers)
find_minimum(numbers)
find_maximum(numbers)
calculate_range(numbers)
Rules
The mean is the sum of values divided by the number of values.
For an odd number of sorted values, the median is the middle value.
For an even number of sorted values, the median is the average of the two middle values.
The range is the maximum value minus the minimum value.
Handle an empty list appropriately.
Example Data
numbers = [10, 20, 30, 40, 50]
Expected Output
Mean: 30
Median: 30
Minimum: 10
Maximum: 50
Range: 40
Additional Requirement
Test all functions with at least three different datasets.

Concepts Covered
Functions, parameters, return values, lists, sorting, arithmetic calculations, edge cases.'''
# def calculate_mean(numbers):
#     if len(numbers) == 0:
#         return None
#     return sum(numbers) / len(numbers)


# def calculate_median(numbers):
#     if len(numbers) == 0:
#         return None

#     sorted_numbers = sorted(numbers)
#     n = len(sorted_numbers)
#     middle = n // 2

#     if n % 2 == 1:
#         return sorted_numbers[middle]
#     else:
#         return (sorted_numbers[middle - 1] +
#                 sorted_numbers[middle]) / 2


# def find_minimum(numbers):
#     if len(numbers) == 0:
#         return None
#     return min(numbers)


# def find_maximum(numbers):
#     if len(numbers) == 0:
#         return None
#     return max(numbers)


# def calculate_range(numbers):
#     if len(numbers) == 0:
#         return None
#     return max(numbers) - min(numbers)


# # Test with three datasets
# datasets = [
#     [10, 20, 30, 40, 50],
#     [5, 10, 15, 20],
#     [8, 2, 12, 4, 6]
# ]

# for numbers in datasets:
#     print("\nNumbers:", numbers)
#     print("Mean:", calculate_mean(numbers))
#     print("Median:", calculate_median(numbers))
#     print("Minimum:", find_minimum(numbers))
#     print("Maximum:", find_maximum(numbers))
#     print("Range:", calculate_range(numbers))

'''oncepts Covered
Functions, parameters, return values, lists, sorting, arithmetic calculations, edge cases.

Task 17: Employee Performance Evaluator
Problem Statement
Create a function that evaluates an employee's performance based on a monthly target and actual achievement.

Requirements
Create a function named:

evaluate_performance(name, monthly_target, actual_achievement)
The function should calculate the achievement percentage and return a performance category.

Performance Criteria
Achievement Percentage	Category
100% or above	Target Achieved
80% to below 100%	Near Target
Below 80%	Needs Improvement
Example Input
Employee Name: Amit
Monthly Target: 100
Actual Achievement: 85
Expected Output
Employee: Amit
Achievement Percentage: 85.0%
Performance Category: Near Target
Requirements
Calculate the achievement percentage.
Return the appropriate category.
Display the employee's performance report.
Handle a zero or negative monthly target appropriately.
Concepts Covered
Functions,parameters,return values,arithmetic operators,conditional logic.'''
# def evaluate_performance(name, monthly_target, actual_achievement):

#     if monthly_target <= 0:
#         return "Invalid monthly target"

#     percentage = (actual_achievement / monthly_target) * 100

#     if percentage >= 100:
#         category = "Target Achieved"
#     elif percentage >= 80:
#         category = "Near Target"
#     else:
#         category = "Needs Improvement"

#     return percentage, category


# name = input("Employee Name: ")
# monthly_target = float(input("Monthly Target: "))
# actual_achievement = float(input("Actual Achievement: "))

# print("Employee:", name)
# print("Monthly Target:", monthly_target)
# print("Actual Achievement:", actual_achievement)

# result = evaluate_performance(name, monthly_target, actual_achievement)

# if result == "Invalid monthly target":
#     print(result)
# else:
#     percentage, category = result
#     print("Achievement Percentage:", percentage, "%")
#     print("Performance Category:", category)

'''Task 18: Attendance Management Functions
Problem Statement
Develop an attendance management program using reusable functions.

The program should calculate attendance percentages and determine whether students are eligible to appear for an examination.

Sample Data
attendance = {
    "Aarav": {"present": 85, "total": 100},
    "Diya": {"present": 70, "total": 100},
    "Rahul": {"present": 60, "total": 90},
    "Priya": {"present": 95, "total": 100}
}
Requirements
Create the following functions:

calculate_attendance(present, total) — returns the attendance percentage.
check_eligibility(percentage) — returns whether the student is eligible.
display_student_attendance(name, present, total) — displays an attendance report.
find_low_attendance_students(attendance_data) — returns students whose attendance is below 75%.
Eligibility Rule
Students must have at least 75% attendance to be eligible for the examination.

Expected Output
Aarav: 85.0% - Eligible
Diya: 70.0% - Not Eligible
Rahul: 66.67% - Not Eligible
Priya: 95.0% - Eligible
Additional Requirements
Handle cases where total classes are zero.
Validate that attendance values are not negative.
Ensure the number of classes attended does not exceed the total classes conducted.
Concepts Covered
Multiple functions, parameters, return values, lists, dictionaries, loops, conditional statements.
'''
# attendance = {
#     "Aarav": {"present": 85, "total": 100},
#     "Diya": {"present": 70, "total": 100},
#     "Rahul": {"present": 60, "total": 90},
#     "Priya": {"present": 95, "total": 100}
# }
# # Calculate Attendance
# def calculate_attendance(present,total):
#     if present <0 or total <0:
#         return "Invaild attendance value"

#     if total==0:
#         return "Total Classes canot be Zero"

#     if present>total:
#         return "Present classes cannot exceed total classes"

#     percentage=(present/total)*100
#     return percentage

# # check Eligibility
# def check_Eligibility(percentage):
#     if percentage>=75:
#         return "Eligible"
#     else:
#         return "Not ELigible"

# # display student attendance
# def display_student_attendance(name,present,total):
#     percentage=calculate_attendance(present,total)
#     if not isinstance(percentage,(int,float)):
#         print(name,":",percentage)
#         return
#     status=check_Eligibility(percentage)

#     print(f"{name}:{percentage:.2f}%-{status}")

# # find low attdance student
# def find_low_attdance_student(attdance_data):
#     low_attdance=[]
#     for name ,detils in attdance_data.items():
#         percentage=calculate_attendance(
#             detils["present"],
#             detils["total"])          

#         if isinstance(percentage,(int,float)) and percentage<75:
#             low_attdance.append(name)
#     return low_attdance

# # display all students
# for name,detils in attendance.items():
#     display_student_attendance(
#         name,
#         detils["present"],
#         detils["total"]

#     )
# low_student=find_low_attdance_student(attendance)
# print("\nStudents with low Attendance:",low_student)

'''Section 5: Integrated Mini Projects'''
'''Task 19: Retail Sales Analysis System
Problem Statement
Build a retail sales analysis system using a collection of sales transactions.

Each transaction contains the product name, quantity sold, and unit price.

Sample Data
sales_transactions = [
    {"product": "Laptop", "quantity": 2, "unit_price": 45000},
    {"product": "Mouse", "quantity": 5, "unit_price": 500},
    {"product": "Keyboard", "quantity": 3, "unit_price": 800},
    {"product": "Monitor", "quantity": 2, "unit_price": 7500},
    {"product": "Laptop", "quantity": 1, "unit_price": 45000}
]
Requirements
Create a program that:

Calculates revenue for each transaction.
Calculates total revenue.
Finds the highest-revenue transaction.
Calculates total revenue for each product.
Calculates the average transaction value.
Identifies transactions above the average transaction value.
Displays a complete sales summary.
Calculation Rules
Transaction Revenue = Quantity × Unit Price
Total Revenue = Sum of All Transaction Revenues
Average Transaction Value = Total Revenue ÷ Number of Transactions
Suggested Functions
calculate_transaction_revenue(transaction)
calculate_total_revenue(transactions)
calculate_product_revenue(transactions)
find_highest_revenue_transaction(transactions)
calculate_average_transaction_value(transactions)
display_sales_report(transactions)
Additional Requirements
Use reusable functions.
Handle an empty transaction list.
Avoid repeating the same calculations unnecessarily.
Display currency values clearly.
Concepts Covered
Lists, dictionaries, loops, conditions, functions, aggregation, nested data structures.'''


# sales_transactions = [
#     {"product": "Laptop", "quantity": 2, "unit_price": 45000},
#     {"product": "Mouse", "quantity": 5, "unit_price": 500},
#     {"product": "Keyboard", "quantity": 3, "unit_price": 800},
#     {"product": "Monitor", "quantity": 2, "unit_price": 7500},
#     {"product": "Laptop", "quantity": 1, "unit_price": 45000}
# ]


# # 1. Calculate Transaction Revenue
# def calculate_transaction_revenue(transaction):

#     revenue = transaction["quantity"] * transaction["unit_price"]

#     return revenue


# # 2. Calculate Total Revenue
# def calculate_total_revenue(transactions):

#     total_revenue = 0

#     for transaction in transactions:
#         total_revenue += calculate_transaction_revenue(transaction)

#     return total_revenue


# # 3. Calculate Product Revenue
# def calculate_product_revenue(transactions):

#     product_revenue = {}

#     for transaction in transactions:

#         product = transaction["product"]
#         revenue = calculate_transaction_revenue(transaction)

#         if product in product_revenue:
#             product_revenue[product] += revenue
#         else:
#             product_revenue[product] = revenue

#     return product_revenue


# # 4. Find Highest Revenue Transaction
# def find_highest_revenue_transaction(transactions):

#     if not transactions:
#         return None

#     highest = transactions[0]

#     for transaction in transactions:

#         if calculate_transaction_revenue(transaction) > calculate_transaction_revenue(highest):
#             highest = transaction

#     return highest


# # 5. Calculate Average Transaction Value
# def calculate_average_transaction_value(transactions):

#     if not transactions:
#         return 0

#     total = calculate_total_revenue(transactions)

#     average = total / len(transactions)

#     return average


# # 6. Display Sales Report
# def display_sales_report(transactions):

#     if not transactions:
#         print("No sales transactions available")
#         return

#     print("----- SALES REPORT -----")

#     print("\nTransaction Revenue:")

#     for transaction in transactions:

#         revenue = calculate_transaction_revenue(transaction)

#         print(transaction["product"], ":", "Rs.", revenue)

#     # Total Revenue
#     total = calculate_total_revenue(transactions)

#     print("\nTotal Revenue: Rs.", total)

#     # Highest Revenue Transaction
#     highest = find_highest_revenue_transaction(transactions)

#     print("\nHighest Revenue Transaction:")
#     print("Product:", highest["product"])
#     print("Revenue: Rs.", calculate_transaction_revenue(highest))

#     # Product Wise Revenue
#     product_revenue = calculate_product_revenue(transactions)

#     print("\nProduct Wise Revenue:")

#     for product, revenue in product_revenue.items():
#         print(product, ":", "Rs.", revenue)

#     # Average Transaction
#     average = calculate_average_transaction_value(transactions)

#     print("\nAverage Transaction Value: Rs.", round(average, 2))

#     # Above Average Transactions
#     print("\nAbove Average Transactions:")

#     for transaction in transactions:

#         revenue = calculate_transaction_revenue(transaction)

#         if revenue > average:
#             print(transaction["product"], ":", "Rs.", revenue)


# # Main Program
# display_sales_report(sales_transactions)


'''Task 20: Student Management System
Problem Statement
Build a menu-driven student management system that allows users to manage student records.

Store student records in a dictionary and organize major operations into separate functions.

Required Features
Add a new student.
Update a student's marks.
Search for a student by name or ID.
Display all student records.
Calculate and display a student's grade.
Calculate the class average.
Identify the topper.
Delete a student record.
Exit the program.
Suggested Data Structure
Use a dictionary to store student records.

Example:

students = {
    "S101": {
        "name": "Aarav",
        "marks": 85
    },
    "S102": {
        "name": "Diya",
        "marks": 92
    },
    "S103": {
        "name": "Rahul",
        "marks": 76
    }
}
Grading Criteria
Marks	Grade
90 and above	A+
75 to below 90	A
60 to below 75	B
40 to below 60	C
Below 40	Fail
Assume marks are out of 100.

Suggested Functions
add_student(students)
update_marks(students)
search_student(students)
display_students(students)
calculate_grade(marks)
calculate_class_average(students)
find_topper(students)
delete_student(students)
main()
Program Flow
Display a menu similar to the following:

========== STUDENT MANAGEMENT SYSTEM ==========

1. Add Student
2. Update Marks
3. Search Student
4. Display All Students
5. Calculate Grade
6. Calculate Class Average
7. Find Topper
8. Delete Student
9. Exit

Enter your choice:
Requirements
Keep the program running until the user selects Exit.
Use separate functions for major operations.
Prevent duplicate student IDs.
Display meaningful messages when a student is not found.
Validate marks to ensure they are between 0 and 100.
Handle an empty student database.
Identify all toppers if multiple students share the highest marks.'''


# students = {
#     "S101": {"name": "Aarav", "marks": 85},
#     "S102": {"name": "Diya", "marks": 92},
#     "S103": {"name": "Rahul", "marks": 76}
# }


# # 1. Add Student
# def add_student(students):

#     student_id = input("Enter Student ID: ")

#     if student_id in students:
#         print("Student ID already exists!")
#         return

#     name = input("Enter Student Name: ")
#     marks = float(input("Enter Marks: "))

#     if marks < 0 or marks > 100:
#         print("Marks must be between 0 and 100")
#         return

#     students[student_id] = {
#         "name": name,
#         "marks": marks
#     }

#     print("Student added successfully!")


# # 2. Update Marks
# def update_marks(students):

#     student_id = input("Enter Student ID: ")

#     if student_id not in students:
#         print("Student not found!")
#         return

#     marks = float(input("Enter New Marks: "))

#     if marks < 0 or marks > 100:
#         print("Invalid marks! Enter between 0 and 100")
#         return

#     students[student_id]["marks"] = marks

#     print("Marks updated successfully!")


# # 3. Search Student
# def search_student(students):

#     search = input("Enter Student Name or ID: ")

#     found = False

#     for student_id, details in students.items():

#         if student_id == search or details["name"].lower() == search.lower():

#             print("Student ID:", student_id)
#             print("Name:", details["name"])
#             print("Marks:", details["marks"])

#             found = True

#     if not found:
#         print("Student not found!")


# # 4. Display All Students
# def display_students(students):

#     if not students:
#         print("No student records available!")
#         return

#     print("\n----- ALL STUDENT RECORDS -----")

#     for student_id, details in students.items():

#         print("Student ID:", student_id)
#         print("Name:", details["name"])
#         print("Marks:", details["marks"])
#         print("------------------------")


# # 5. Calculate Grade
# def calculate_grade(marks):

#     if marks >= 90:
#         return "A+"
#     elif marks >= 75:
#         return "A"
#     elif marks >= 60:
#         return "B"
#     elif marks >= 40:
#         return "C"
#     else:
#         return "Fail"


# def display_grade(students):

#     student_id = input("Enter Student ID: ")

#     if student_id not in students:
#         print("Student not found!")
#         return

#     marks = students[student_id]["marks"]

#     grade = calculate_grade(marks)

#     print("Student:", students[student_id]["name"])
#     print("Marks:", marks)
#     print("Grade:", grade)


# # 6. Calculate Class Average
# def calculate_class_average(students):

#     if not students:
#         print("No student records available!")
#         return

#     total_marks = 0

#     for details in students.values():
#         total_marks += details["marks"]

#     average = total_marks / len(students)

#     print("Class Average:", round(average, 2))


# # 7. Find Topper
# def find_topper(students):

#     if not students:
#         print("No student records available!")
#         return

#     highest_marks = max(
#         details["marks"] for details in students.values()
#     )

#     print("----- CLASS TOPPER -----")

#     for student_id, details in students.items():

#         if details["marks"] == highest_marks:

#             print("Student ID:", student_id)
#             print("Name:", details["name"])
#             print("Marks:", details["marks"])


# # 8. Delete Student
# def delete_student(students):

#     student_id = input("Enter Student ID to Delete: ")

#     if student_id not in students:
#         print("Student not found!")
#         return

#     del students[student_id]

#     print("Student deleted successfully!")


# # 9. Main Function
# def main():

#     while True:

#         print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
#         print("1. Add Student")
#         print("2. Update Marks")
#         print("3. Search Student")
#         print("4. Display All Students")
#         print("5. Calculate Grade")
#         print("6. Calculate Class Average")
#         print("7. Find Topper")
#         print("8. Delete Student")
#         print("9. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_student(students)

#         elif choice == "2":
#             update_marks(students)

#         elif choice == "3":
#             search_student(students)

#         elif choice == "4":
#             display_students(students)

#         elif choice == "5":
#             display_grade(students)

#         elif choice == "6":
#             calculate_class_average(students)

#         elif choice == "7":
#             find_topper(students)

#         elif choice == "8":
#             delete_student(students)

#         elif choice == "9":
#             print("Thank you for using Student Management System!")
#             break

#         else:
#             print("Invalid choice! Please select 1 to 9.")


# # Run Program
# main()
































