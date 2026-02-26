friends = ["Rold","sold","eold","hold"]

# enumrate is basically index number for array like in the loop when we get full array showing one by one we also get index number with them but in python we need to use enumerate function like below


for counter,name in enumerate(friends):
    print(counter)
    print(name) 
    
    
 # in enumerate we can start from whatebver position  we want through passing the var in the enumerate function like below using start parameter

for counter,name in enumerate(friends,start=2):
    print(f"counter : --- {counter}")
    print(f"name : --- {name}") 
    
    
# list of enumerates 
print(list(enumerate(friends)))
print(dict(enumerate(friends)))
