'''Homework Assignment'''
# Employee and Sales Analytics Using Functions


'''1)Calculate the total salary expense for a list of employee salaries.'''
Salary=[10000,50000,60000,70000]
def total_Salary(Salary):
     return sum(Salary)
result=total_Salary(Salary)
print("total_Salary:",result)


'''2)Calculate average salary.'''
Salary=[10000,50000,60000,70000]
def average_Salary(Salary):
     return sum(Salary)/len(Salary)
result=average_Salary(Salary)
print("average_Salary:",result)


'''3)Find the highest and lowest salary.'''
Salary=[10000,50000,60000,70000]
def Highest_Salary(Salary):
     return max(Salary)

def Lowest_Salary(Salary):
     return min(Salary)


highest=Highest_Salary(Salary)
lowest=Lowest_Salary(Salary)
print("Highest_Salary:",highest)
print("Lowest_Salary:",lowest)


'''4)Count employees earning above a specified salary.'''
Salary=[10000,50000,60000,70000]
def count_employess(Salary,Specified_Salary):
     count=0
     for Salary in Salary:
          if Salary>Specified_Salary:
               count+=1
     return count
result=count_employess(Salary,50000)
print("Employees earning above salary:",result)



'''5)Calculate the percentage increase between previous and current sales.'''
previous_sales = 50000
current_sales = 70000

def percentage_increase(previous_sales,current_sales):
     increase=current_sales-previous_sales
     return(increase/previous_sales)*100
result=percentage_increase(previous_sales,current_sales)
print("Percentage Increase:", result, "%")



'''6)Classify sales performance against a target.'''
def sales_performance(sales, target):
    if sales >= target:
        return "Target Achieved"
    else:
        return "Target Not Achieved"

result = sales_performance(80000, 70000)

print("Sales Performance:", result)



'''7)Generate a summary report using the results returned by the functions.'''
Sales = [50000, 60000, 70000, 80000]
target = 65000

def total_sales(Sales):
    return sum(Sales)

def average_sales(Sales):
    return sum(Sales) / len(Sales)

def sales_performance(sales, target):
    if sales >= target:
        return "Target Achieved"
    else:
        return "Target Not Achieved"

total = total_sales(Sales)
average = average_sales(Sales)
performance = sales_performance(total, target)

print("----- Sales Summary Report -----")
print("Total Sales:", total)
print("Average Sales:", average)
print("Sales Target:", target)
print("Performance:", performance)



