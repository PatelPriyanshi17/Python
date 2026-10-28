'''1)Convert string into uppercase.'''
Name="priyanshi"
print(Name.upper())

'''2)Split sentence into words.'''
Text="I Like Python"
print(Text.split())

'''3)Add 5 values into list using append().'''
numbers=[]
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)
print(numbers)

'''4)Sort list in descending order.'''
numbers=[6,9,2,5,8,3,1]
numbers.sort()
print(numbers)

'''5)Create dictionary and print keys & values.'''
student={
    "Name":"Piyu",
    "Age":21,
    "City":"Ahmedabad"
}
print(student.keys())
print(student.values())

for keys,values in student.items():
    print(keys,":",values)


