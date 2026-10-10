'''Recap'''
# name = "Rahul"
# quantity = 5
# price = 1000
# sales = quantity * price
# print(name)
# print(sales)

'''Arithmetic Operators'''
# a = 20
# b = 6

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** 2)

'''Comparison Operators'''
# sales = 50000

# print(sales > 40000)
# print(sales < 40000)
# print(sales >= 50000)
# print(sales == 50000)
# print(sales != 50000)

'''= vs =='''
# sales = 50000
# sales == 50000

'''Logical Operators'''
'''and'''
# age = 25
# salary = 50000

# print(age >= 18 and salary >= 30000)

'''or'''
# sales = 30000
# profit = 5000

# print(sales > 50000 or profit > 1000)

'''not'''
# is_active = True

# print(not is_active)

'''Assignment Operators'''
# sales = 50000
# sales += 10000

# print(sales)

"""if Statement"""
# sales = 75000

# if sales > 50000:
#  print("High Sales")

'''if-else'''

# sales = 30000

# if sales > 50000:
#     print("High Sales")
# else:
#     print("Low Sales")


# sales = 100000
# cost = 85000

# profit = sales - cost

# if profit > 0:
#     print("Profit")
# else:
#     print("Loss")

'''if-elif-else'''
# sales = 85000

# if sales >= 100000:
#     print("Excellent")
# elif sales >= 75000:
#     print("Good")
# elif sales >= 50000:
#     print("Average")
# else:
#     print("Poor")

'''Multiple Conditions'''
# sales = 100000
# profit = 25000

# if sales >= 100000 and profit >= 20000:
#     print("High Performing Order")

'''Customer Segmentation'''
# purchase_amount = 75000

# if purchase_amount >= 100000:
#     print("Premium Customer")
# elif purchase_amount >= 50000:
#     print("Gold Customer")
# elif purchase_amount >= 25000:
#     print("Silver Customer")
# else:
#     print("Regular Customer")

'''Discount Calculation'''
# amount = 75000

# if amount >= 100000:
#     discount = 20
# elif amount >= 50000:
#     discount = 10
# else:
#     discount = 5

# print("Discount:", discount, "%")

'''Nested if'''
# sales = 100000
# profit = 25000

# if sales >= 50000:
#     if profit > 0:
#         print("Profitable High-Sales Order")

'''Employee Bonus'''
# sales = 120000
# profit = 25000

# if sales >= 100000:
#     if profit >= 20000:
#         print("Eligible for Bonus")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")


'''User Input + Conditions'''
# sales = float(input("Enter sales amount: "))

# if sales >= 100000:
#     print("Excellent Sales")
# elif sales >= 50000:
#     print("Good Sales")
# else:
#     print("Low Sales")

'''Student Result'''
# marks = float(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 60:
#     print("Grade C")
# elif marks >= 35:
#     print("Grade D")
# else:
#     print("Fail")

''' Data Quality Check'''
# age = int(input("Enter customer age: "))

# if age >= 18 and age <= 100:
#     print("Valid Age")
# else:
#     print("Invalid Age")

'''Sales Validation'''
# sales = float(input("Enter sales amount: "))

# if sales < 0:
#     print("Invalid Sales")
# else:
#     print("Valid Sales")

'''Customer Status'''
# purchase = float(input("Enter purchase amount: "))

# if purchase >= 50000:
#     status = "Premium"
# elif purchase >= 25000:
#     status = "Gold"
# elif purchase >= 10000:
#     status = "Silver"
# else:
#     status = "Regular"

# print("Customer Status:", status)

''' Mini Project — Sales Performance Analyzer
Create a program that accepts:

Sales Amount
Cost Amount
Calculate:

Revenue
Profit
Profit Percentage
Performance
Business Rules
Condition	Performance
Sales >= 100000 and Profit >= 20000	Excellent
Sales >= 75000	Good
Sales >= 50000	Average
Otherwise	Poor
Solution for Classroom Demonstration'''

#sales = float(input("Enter sales: "))
# cost = float(input("Enter cost: "))

# profit = sales - cost
# profit_percentage = (profit / sales) * 100

# if sales >= 100000 and profit >= 20000:
#     performance = "Excellent"
# elif sales >= 75000:
#     performance = "Good"
# elif sales >= 50000:
#     performance = "Average"
# else:
#     performance = "Poor"

# print("Sales:", sales)
# print("Cost:", cost)
# print("Profit:", profit)
# print("Profit %:", profit_percentage)
# print("Performance:", performance)

