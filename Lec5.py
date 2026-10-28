'''Upper'''
name="Priyanshi"
print(name.upper())

'''Methods in String (str)'''
'''
upper()	Convert to uppercase
lower()	Convert to lowercase
title()	First letter capital
capitalize()	Capitalize first character
strip()	Remove spaces
replace()	Replace text
split()	Convert string into list
join()	Join list into string
find()	Find position
count()	Count occurrences
startswith()	Check starting
endswith()	Check ending
isdigit()	Check digits
isalpha()	Check alphabets'''

'''Upper'''
name="Priyanshi"
print(name.upper())

'''Lower'''
name="Priyanshi"
print(name.lower())

'''Title'''
name="priyanshi patel"
print(name.title())

'''capitalize()'''
name="priyanshi patel"
print(name.capitalize())

'''strip()'''
name = " priyanshi "
print(name.strip())

'''replace()'''
text="I Like Java"
print(text.replace("Java" ,"Python"))

'''split'''
data="Sql Python Excel Powerbi"
print(data.split())

'''join()'''
skills=["Python","PowerBi","Excel"]
print("/".join(skills))

'''Find'''
name="Priyanshi"
print(name.find("h"))

'''count()'''
text="Patel Priyanshi "
print(text.count("P"))

'''startswith() and endswith()'''
name="Priyanshi Patel"
print(name.startswith("Pr"))
print(name.endswith("tel"))

'''isdigit()'''
num = "123456"
print(num.isdigit())

"isalpha()"
name="Priyanshi"
print(name.isalpha())


'''List Methods (list)'''

'''Common List Methods
Method	Purpose
append()	Add item
extend()	Add multiple items
insert()	Insert at position
remove()	Remove item
pop()	Remove by index
clear()	Remove all items
index()	Find position
count()	Count values
sort()	Sort list
reverse()	Reverse list
copy()	Copy list'''


'''append()'''
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

'''extend()'''
numbers=[1,2]
numbers.extend([3,4,5])
print(numbers)

'''insert()'''
name=["Piyu","Neel" ]
name.insert(0,"Priyanshi")
print(name)

'''remove()'''
fruits = ["Apple", "Banana"]
fruits.remove("Apple")
print(fruits)

'''Pop'''
numbers = [10,20,30]
numbers.pop(1)
print(numbers)

'''clear()'''
numbers=[10,20,30]
numbers.clear()
print(numbers)

"Index"
name=["A","B","C"]
print(name.index("B"))

"count()"
numbers=[1,2,1,2,3,3,4]
print(numbers.count(4))

'''sort()'''
numbers=[10,6,9,5,4,3,8,2,1]
numbers.sort()
print(numbers)

'''reverse()'''
numbers=[10,6,9,5,4,3,8,2,1]
numbers.reverse()
print(numbers)

'''Copy()'''
a=[1,2,3]
b=a.copy()
print(b)


'''Tuple Methods (tuple)'''
'''Only two important methods:

Method	Purpose
count()	Count values
index()	Find position'''

'''count()'''
data=(1,1,1,2)
print(data.count(1))

'''index()'''
print(data.index(2))


'''Set Methods (set)'''
'''add()	Add item
update()	Add multiple items
remove()	Remove item
discard()	Remove safely
pop()	Remove random item
clear()	Remove all
union()	Combine sets
intersection()	Common values
difference()	Unique values'''

'''add()'''
num={1,2,3,4}
num.add(4)
print(num)

'''update'''
num={1,2,3,4,5}
num.update([6,7])
print(num)

'''remove and discard'''
num={1,2,3,4,5}
num.remove(5)
num.discard(5)
print(num)

'''pop'''
num={1,2,3,4}
num.pop()
print(num)

'''union()'''
a={1,2}
b={3,4}
print(a.union(b))

'''intersection()'''
a={1,2,3}
b={3,4,5}
print(a.intersection(b))

'''Dictionary Methods (dict)
Dictionaries store key-value pairs.'''

'''keys()	Get keys
values()	Get values
items()	Get key-value pairs
get()	Get value safely
update()	Update dictionary
pop()	Remove item
clear()	Remove all
copy()	Copy dictionary'''

'''keys()'''
student = {
    "name": "Rahul",
    "age": 21
}

print(student.keys())

'''values'''
student = {
    "name": "Rahul",
    "age": 21
}
print(student.values())

'''items'''
student = {
    "name": "Rahul",
    "age": 21
}
print(student.items())

'''get()'''
student = {
    "name": "Rahul",
    "age": 21
}
print(student.get("name"))

'''update'''
student = {
    "name": "Rahul",
    "age": 21
}
student.update({"City":"ahmedabad"})
print(student)

'''pop()'''
student = {
    "name": "Rahul",
    "age": 21
}
student.pop("age")
print(student)
