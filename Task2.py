'''Task 1 — Number Classification
Take a number and determine whether it is:

Positive
Negative
Zero'''

# number=int(input("Enter your number"))
# print(number)
# if number >0:
#     print("Positive")
# elif number <0:
#     print("Negative")
# else :
#     print("Zero")

'''Task 2 — Even or Odd
Take a number and determine whether it is even or odd. Use %.'''

# Number=int(input("Enter your number"))
# if Number % 2 == 0:
#     print("Even")
# else:
#     print("odd")

'''Task 3 — Sales Classification
Sales	Category
>= 100000	Excellent
>= 75000	Good
>= 50000	Average
< 50000	Poor'''

# sales=float(input("Enter Sales:"))
# print(sales)
# if sales >=100000:
#     Sales_Category = "Excellent"
# elif sales >=75000:
#    Sales_Category="Good"
# elif sales >=50000:
#     Sales_Category="Average"
# else:
#     Sales_Category="Poor"

# print(Sales_Category)

'''Task 4 — Profit or Loss
Take sales and cost and determine profit or loss.'''

# sales=float(input("Enter Your Sales"))
# cost=float(input("Enter your Cost"))
# profit=sales-cost
# print(profit)
# if profit >=0:
#     print("Profit")
# else :
#     print("loss")

'''Task 5 — Customer Segmentation
Purchase	Customer Type
>= 100000	Premium
>= 50000	Gold
>= 25000	Silver
< 25000	Regular'''

# sales=float(input("Enter Sales:"))
# print(sales)
# if sales >=100000:
#     Customer_Type="Premium"
# elif sales >=50000:
#    Customer_Type="Gold"
# elif sales >=25000:
#     Customer_Type="Sliver"
# else:
#     Customer_Type="Regular"
# print(Customer_Type)

'''Task 6 — Discount Calculator
Amount	Discount
>= 100000	20%
>= 50000	10%
>= 25000	5%
< 25000	0%
Calculate the final amount.'''

# Amount=float(input("Enter Amount:"))

# if Amount >=100000:
#     Discount=20
# elif Amount >=50000:
#     Discount=10
# elif Amount >=25000:
#     Discount=5
# else:
#     Discount=0
# print("Discount:", Discount, "%")

'''Task 7 — Employee Bonus
Take employee sales and profit.

Sales >= 100000 AND Profit >= 20000
→ Bonus Eligible

Otherwise
→ Not Eligible'''

# sales=float(input("Enter Your Sales"))
# Profit=float(input("Enter your Profit"))
# if sales>=100000 and Profit >=20000:
#    Employee_Bonus="Bonus Eligible"
# else :
#    Employee_Bonus="Not Eligible"
# print("Employee_Bonus:",Employee_Bonus)

'''Task 8 — Data Validation
Take customer age.

18 to 100 → Valid
Otherwise → Invalid'''

# age=int(input("Enter Your Age:"))
# print(age)
# if age >=18 and age <=100:
#     Data_validation="Valid"
# else :
#     Data_validation="Invaild"
# print("Data_validation:",Data_validation)

'''Task 9 — Student Result
90+ → A
75–89 → B
60–74 → C
35–59 → D
Below 35 → Fail
'''
# Marks=float(input("Enter Your Marks:"))
# print(Marks)
# if Marks >=90:
#     Student_Result="A"
# elif Marks >=75 :
#     Student_Result="B"
# elif Marks >=60:
#     Student_Result="C"
# elif Marks >=35 :
#     Student_Result="D"
# else:
#     Student_Result="Fail"
# print("Student_Result:",Student_Result)

'''Task 10 — Order Valida100000tion
Take quantity and unit price.

Both must be greater than 0.

Display Valid Order or Invalid Order'''

# quantity=int(input("Enter_quantity:"))
# print(quantity)
# Unit_price=int(input("ENter Unit_price:"))
# print(Unit_price)
# if quantity >0 and Unit_price>0:
#     Order_Validation="Valid"
# else :
#     Order_Validation="Invalid"
# print("Order_Validation:",Order_Validation)


''' Challenge Task — Customer Classification
Customer Name
Purchase Amount
Number of Orders
Rules
Premium:
Purchase >= 100000  AND Orders >= 10

Gold:
Purchase >= 50000 AND Orders >= 5

Silver:
Purchase >= 25000

Regular:
Everything else
Display:

Customer Name
Purchase Amount
Number of Orders
Customer Segment
'''

# Customer_Name=input("Enter Your Name:")
# Purchase_Amount=float(input("Enter Purchase Amount:"))
# Number_of_Orders=int(input("Enter Numbers of Orders:"))
# if Purchase_Amount >=100000 and Number_of_Orders>=10:
#     Customer_Segment="Premium"
# elif Purchase_Amount>= 50000 and Number_of_Orders>=5:
#     Customer_Segment="Gold"
# elif Purchase_Amount>= 25000 :
#     Customer_Segment="Silver"
# else :
#     Customer_Segment="Regular"
# print("Customer_Name:",Customer_Name)
# print("Purchase_Amount:",Purchase_Amount)
# print("Number_of_Orders:",Number_of_Orders)
# print("Customer_Segment:",Customer_Segment)
