# list comprehension


# this is without list comprehension

numbers = [0,1,2,3,4]
doubled_number = []


for number in numbers:
    doubled_number.append(number*2)
     
print(doubled_number)

# this is with list comprehension

numbers = [0,1,2,3,4]

doubled_number =  [number * 2 for number in numbers]
print(doubled_number) 

# this is with list comprehension using range

doubled_number =  [number * 2 for number in range(5)]
print(doubled_number) 

# using list comprehension for lowering the string case

names = ["Roy","Toy","Soy"]
lower_Name= [name.lower() for name in names]
print(lower_Name)

#Title case

names = ["roy","toy","soy"]
title_Name= [name.title() for name in names]
print(title_Name)



## List Comprehension with conditionals

ages = [22,35,27,21,28]
odds = [age for age in ages if age %2 != 0]

print(odds)

friends = ["Rold","sold","eold","hold","gold","fold"]
guests = ["jose","Bob","Rold","eold","Gold"]
friends_to_lower = [friend.lower() for friend in friends]


present_friends = [
    name.title() 
    for name in guests 
    if name.lower() in friends_to_lower
]

print(present_friends)

 