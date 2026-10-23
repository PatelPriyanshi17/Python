'''1)Print all numbers from 1 to 50.'''
for numbers in range(1,51):
    print(numbers)

'''2)Print all even numbers between 1 and 100.'''
for numbers in range(2,101,2):
        print(numbers)

'''3)Calculate the sum of numbers from 1 to 100.'''
total = 0
for i in range(1, 101):
    total+=i
print("Sum:", total)

'''4)Calculate the total and average of a list of 10 sales values.'''
sales = [12000, 25000, 30000, 45000, 50000,
         60000, 35000, 40000, 55000, 48000]

total = 0
for i in sales:
    total+=i
    avg=total/len(sales)
print("Total Sales:", total)
print("Average Sales:", avg)

'''5)Count how many sales values exceed ₹50,000.'''
sales = [12000, 25000, 30000, 45000, 50000,
         60000, 35000, 40000, 55000, 48000]
count=0
for value in sales:
    if value >50000:
        count+=1
print("High Sales Count:", count)

'''6)Find the highest sales value without using max().'''
sales = [12000, 25000, 30000, 45000, 50000,
         60000, 35000, 40000, 55000, 48000]
highest=sales[0]
for value in sales:
    if value > highest:
        highest=value
print("Highest Value:",highest)

'''7)Find the lowest sales value without using min().'''
sales = [12000, 25000, 30000, 45000, 50000,
         60000, 35000, 40000, 55000, 48000]
lowest=sales[0]
for value in sales:
    if value < lowest:
        lowest=value
print("Lowest value:",lowest)


'''8)Count the number of negative values in a list of transactions.'''
transactions = [5000, -2000, 3000, -1500, 7000, -500]
count=0
for value in transactions:
    if value < 0:
        count+=1
print("Negative values:",count)

'''9)Calculate profit for each product using separate sales and cost lists.'''
sales = [50000, 80000, 60000]
cost = [30000, 50000, 45000]
for i in range(len(sales)):
        profit=sales[i]-cost[i]
        print("Product", i + 1, "Profit:", profit)

'''10)Count how many students passed, given a list of marks and a passing score of 35.'''
marks = [80, 25, 35, 60, 30, 90, 45, 20]

passed = 0

for mark in marks:
    if mark >= 35:
        passed += 1

print("Students Passed:", passed)

'''11)Print customer names from a list, skipping empty strings.'''
customers = ["Rahul", "", "Priya", "Amit", "", "Neha"]
for name in customers:
    if name != "":
        print(name)

'''12)Use a while loop to display numbers from 10 down to 1.'''
i=10
while i >= 1:
    print(i)
    i = i-1


'''13)Stop processing a list when the first value greater than ₹1,00,000 is found.'''
sales = [25000, 50000, 75000, 125000, 60000, 150000]
for value in sales:
    if value >100000:
        print("first value:",value)
        break
    print("Processing:", value)

'''14)Calculate total revenue for a list of product quantities and prices.'''
quantities = [10, 20, 15, 5]
prices = [100, 250, 300, 500]

total_revenue = 0
for i in range(len(quantities)):
    total_revenue=quantities[i]*prices[i]
    total_revenue+=1
print("Total Revenue:", total_revenue)

'''15)Build a sales report showing total sales, average sales, highest sales, and number of high-sales days.'''
sales = [25000, 60000, 45000, 80000, 35000,
         95000, 50000, 70000]

total_sales = 0
highest_sales = sales[0]
high_sales_days = 0

for value in sales:
    total_sales+=value

    if value >highest_sales:
        highest_sales=value

    if value > 50000:
        high_sales_days+=1
        
average_sales = total_sales / len(sales)
print("Total_Sales:",total_sales)
print("highest_sales:",highest_sales)
print("high_sales_days:",high_sales_days)
print("average_sales:",average_sales)

'''Create a program using a list of at least 10 daily sales values. Your program must:
- Display every daily sales value.
- Calculate total and average sales.
- Identify the highest and lowest sales.
- Count days with sales above ₹50,000.
- Count days with sales below ₹20,000.
- Calculate the percentage of days with sales above ₹50,000.
Use loops for calculations and display a clean summary report. can you explan please'''

sales = [25000, 60000, 45000, 80000, 15000,
         95000, 50000, 70000, 18000, 40000]

total = 0
count_above_50000 = 0
count_below_20000 = 0
highest = sales[0]
lowest = sales[0]
count = 0

print("Daily Sales Report")
for i in sales:
    print(i)
    total+=i
    count+=1
    if i > highest:
        highest=i

    if i < lowest:
        lowest =i 

    if i >50000:
        count_above_50000+=1

    if i <20000:
        count_below_20000+=1

avg=total/len(sales)
percentage = (count_above_50000 / count) * 100 

print("\n----- Sales Summary -----")
print("Total Sales:", total)
print("Average Sales:", avg)
print("Highest Sales:", highest)
print("Lowest Sales:", lowest)
print("Days above 50000:", count_above_50000)
print("Days below 20000:", count_below_20000)
print("Percentage above 50000:", percentage, "%")