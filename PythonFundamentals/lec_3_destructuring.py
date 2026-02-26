
#Destructuring 

friend = [("rolf",22),('roy',25)]

for name,age in friend:
    print(f"this is {name} and age is {age}")
    
# now we are learning iterating over dictionaries

friends_ages = {"rolf":21,"self": 24,"nelf": 14,"helf": 40}

for name,age in friends_ages.items():
    print(f"{name} is {age} year old")
    
""" 
Output:
rolf is 21 year old
self is 24 year old
nelf is 14 year old
helf is 40 year old
"""


