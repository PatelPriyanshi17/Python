'''A simple function'''
def greet():
    print("My Name is Priyanshi")
greet()


'''Calling a function multiple times'''
def greet():
    print("My Name is Priyanshi")
    print("My Name is Priyanshi")
    print("My Name is Priyanshi")
greet()

'''Parameters and Arguments'''
def greet_students(Name):
    print("Welcome",Name)
greet_students("Priyanshi")
greet_students("Neel")

''' Business calculation'''
def calculate_revenue(quantity, price):
    print("Total Revenue:", quantity * price)

calculate_revenue(10, 500)
calculate_revenue(20, 750)
calculate_revenue(5, 1200) 



'''Understanding return'''
'''print() versus return
print()	return
Displays information on the screen |	Gives a value back to the caller
Mainly used to show output	| Used to reuse a result in further calculations
Does not, by itself, provide a result to assign	| Allows the result to be stored in a variable'''

'''Example 1: Using print()'''
def calcualte_total(a,b):
    print(a+b)

result=calcualte_total(10,20)
print(result)

'''Example 2: Using return'''
def calcualte_total(a,b):
    return(a+b)

result=calcualte_total(10,20)
print(result)

'''Example 3: Reusing a returned value'''
def calculate_revenue(quantity, price):
    return quantity*price

revenue=calculate_revenue(10,500)
tax=revenue*0.18
final_amout=revenue+tax

print("revenue:",revenue)
print("Tax:",tax)
print("Final_amount:",final_amout)

''' Types of Arguments'''
'''positional Arguments'''
def employee_detils(name,department):
    print("name:",name)
    print("department:",department)
employee_detils("Piyu","IT")

'''Keywords Arguments'''
def employee_detils(name,department):
    print("name:",name)
    print("department:",department)
employee_detils(name="Piyu",department="IT")

'''defualt Arguments'''

def calculate_discount(price,discount=10):
    return price*discount/100

print(calculate_discount(100))
print(calculate_discount(1000,20))

'''Functions with Multiple Return Values'''

sales = [1200, 2500, 1800, 3200, 1500]

def analyze_sales(sales):
    total=sum(sales)
    avg=total/len(sales)
    highest=max(sales)
    lowest=min(sales)

    return total,avg,highest,lowest
total,avg,highest,lowest=analyze_sales(sales)


print("Total Sales:", total)
print("Average Sales:", avg)
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)


'''Functions with Conditions'''
def evaluate_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"

print(evaluate_performance(95))
print(evaluate_performance(80))
print(evaluate_performance(60))
print(evaluate_performance(35)) 


'''Working with *args and **kwargs'''
'''*args'''

def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10,20))
print(calculate_total(10,20,30,40))
print(calculate_total(10,20,30,40,50,60,70))

'''kwargs'''
def display_employee(**detils):
    for key,value in detils.items():
        print(key,":",value)

display_employee(
    name="Amit",
    department="IT",
    Salary=50000
)

'''Local and Global Variables'''
# Local 
def calculate_profit(): 
    revenue=5000
    expenses=3000
    profit=revenue-expenses
    print(profit)
calculate_profit()

# Global
a="Piyu"
def display_name():
    print(a)

display_name()

'''Writing Clean, Reusable Functions'''
def calculate_profit(revenue, expenses):
    """Calculate profit by subtracting expenses from revenue."""
    return revenue - expenses

profit = calculate_profit(100000, 65000)

print(profit)
print(calculate_profit.__doc__)


'''Practical Data Analytics Project'''
def calculate_revenue(quantity, unit_price):
    """Calculate gross sales revenue."""
    return quantity * unit_price


def calculate_discount(revenue, discount_percent):
    """Calculate the discount amount."""
    return revenue * discount_percent / 100


def calculate_net_revenue(revenue, discount):
    """Calculate revenue after discount."""
    return revenue - discount


def evaluate_sales(net_revenue):
    """Classify a transaction by net revenue."""
    if net_revenue >= 10000:
        return "High Value"
    elif net_revenue >= 5000:
        return "Medium Value"
    else:
        return "Low Value"


# Transaction details
product = "Laptop"
quantity = 3
unit_price = 45000
discount_percent = 10

# Calculations
gross_revenue = calculate_revenue(quantity, unit_price)
discount = calculate_discount(gross_revenue, discount_percent)
net_revenue = calculate_net_revenue(gross_revenue, discount)
category = evaluate_sales(net_revenue)

# Report
print("Product:", product)
print("Gross Revenue:", gross_revenue)
print("Discount:", discount)
print("Net Revenue:", net_revenue)
print("Sales Category:", category)


''' Handling invalid input'''
def calculate_average(total, count):
    if count <= 0:
        return None

    return total / count

print(calculate_average(500, 5))
print(calculate_average(500, 0))

# In-Class Practical Exercises

'''Exercise 1 — Basic function (Easy)
Create a function named display_welcome() that prints a welcome message for a Data Analytics course.'''
def display_welcome():
    print("welcome Data Analytics course")
display_welcome()

'''Exercise 2 — Calculator (Easy)
Create a function that accepts two numbers and returns their sum, difference, product, and quotient. 
Consider division by zero.'''

def calculator(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b

    if b != 0:
        quotient = a / b
    else:
        quotient = "Cannot divide by zero"

    return sum_result, difference, product, quotient


result = calculator(10, 5)

print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])

'''Exercise 3 — Employee salary (Easy)
Create a function that accepts basic salary and bonus percentage and returns 
the final salary after adding the bonus.'''

def calculate_Salary(basic_salary,bouns_percentage):
    bouns=basic_salary*bouns_percentage/100
    final_salary=basic_salary+bouns

    return final_salary
result=calculate_Salary(30000,10)
print("final_Salary:",result)

'''Exercise 4 — Sales metrics (Medium)
Write a function that accepts a list of daily sales and returns 
the total, average, highest, and lowest sales.'''

Daily_Sales=[10000,40000,20000,15000]
def sales_metrics(sales):
    total=sum(sales)
    avg=total/len(sales)
    highest=max(sales)
    lowest=min(sales)

    return total,avg,highest,lowest

result=sales_metrics(Daily_Sales)
print("Total Sales:",result[0])
print("Avg Sales:",result[1])
print("highest Sales:",result[2])
print("Lowest Sales:",result[3])

'''Exercise 5 — Student results (Medium)
Create a function that accepts a student's marks and returns a grade based on thresholds you define. 
Test at least five scores.'''

def student_Grade(marks):
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=35:
        return "D"
    else: 
        return "fail"

print("marks: 95,grade:",student_Grade(95))
print("marks: 50,grade:",student_Grade(50))
print("marks: 65,grade:",student_Grade(65))
print("marks: 70,grade:",student_Grade(70))
print("marks: 72,grade:",student_Grade(72))


'''Exercise 6 — Discount calculator (Medium)
Write a function accepting product price and discount percentage. 
Return the discount amount and final price.'''
def discount_calculator(Price,discount_Percentage):
    discount_amount=Price*discount_Percentage/100
    final_Price=discount_amount+Price

    return discount_amount,final_Price
result=discount_calculator(100,10)
print("Discount Amount:",result[0])
print("final_Price:",result[1])

'''Exercise 7 — Customer transactions (Medium)
Create a function that accepts a list of transaction values and counts 
how many are greater than or equal to ₹5,000.'''
transactions=[10000,3000,2000,6000,7000,1000]
def count_transactions(transactions):
    count=0

    for amount in transactions:
       if amount >= 5000:
          count+=1

    return count
result=count_transactions(transactions)
print("Transactions >= Rs.5000:", result)


'''Exercise 8 — Mini analytics report (Challenge)
Create separate functions to calculate total revenue, average order value, 
and the number of orders from a list of order amounts.'''
Orders=[1000,250,560,700,490]
def total_revenue(Orders):
    return sum(Orders)

def average_order(Orders):
    return sum(Orders)/len(Orders)

def count_orders(Orders):
    return len(Orders)

print("Total Revenue:", total_revenue(Orders))
print("Average Order Value:", average_order(Orders))
print("Number of Orders:", count_orders(Orders))



