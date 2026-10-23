'''1)Create variables for:

name
age
percentage
is_pass
Print their data types.'''

name="Priyanshi"
age=21
percentage=80.0
is_pass=True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_pass))

'''2)Create a list of 5 cities and replace one city.'''
City=["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Bhavnagar"]
City[0]="Gandhinagar"
print(City)

'''3)Create dictionary of student information.'''
Students={
    "name":"Priyanshi",
    "age":21,
    "percentage":80.0,
    "city":"Ahmedabad"
}
print(Students)

'''4)Convert:

"100" → int
50 → string
10 → float '''

age="100"
new_age=int(age)
print(new_age)

age=50
text=str(age)
print(text)

age=10
print(float(age))

'''Homework'''
'''1)Create a student database using dictionary'''
Students={
    1:{
    "name":"Priyanshi",
    "age":21,
    "percentage":80.0,
    "city":"Ahmedabad"
},
2:{
    "name":"Neel",
    "age":22,
    "percentage":81.0,
    "city":"mumbai"
},
3:{
    "name":"Hitarth",
    "age":21,
    "percentage":90.0,
    "city":"udaipur"
},
}

print("Students Database")
for Student_Id,detils in Students.items():
    print("\nStudents name:",detils["name"])
    print("Students age:",detils["age"])
    print("Students percentage:",detils["percentage"])
    print("Students city:",detils["city"])

'''2)Create a shopping cart using list'''
Shopping_cart=["Laptop", "Mouse", "Keyboard", "Headphones"]

print("Shopping_cart:",Shopping_cart)

Shopping_cart.append("Mobile")
print("After adding cart:",Shopping_cart)

Shopping_cart.remove("Mouse")
print("Remove Cart:",Shopping_cart)

print("Total Item",len(Shopping_cart))

'''3)Explain mutable vs immutable with examples'''
# matuble
list=[10,20,30]
list[0]=100
print(list)

# immutable
name="priyanshi"
name= name + " patel"
print(name)

'''4)Create a program using all data types together'''
# Integer 
age=21

# string
name="Priyanshi"

# float
percentage=80.0

# boolean
is_pass=True

# list
subjects = ["Python", "SQL", "Excel"]

# tuple
cities = ("Ahmedabad", "Surat", "Vadodara")

# set
skills = {"Python", "SQL", "Power BI"}

# Dictionary
student = {
    "name": name,
    "age": age,
    "percentage": percentage
}

result=None


print(age,(type(age)))
print(name,(type(name)))
print(percentage,(type(percentage)))
print(is_pass,(type(is_pass)))
print(subjects,(type(subjects)))
print(cities,(type(cities)))
print(skills,(type(skills)))
print(student,(type(student)))
print(result,(type(result)))

