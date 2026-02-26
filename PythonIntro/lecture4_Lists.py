# list is a built-in, ordered, and mutable collection data structure used to store multiple items in a single 

friends = ['solf','golf','eolf']
# get length of the string 
print(len(friends)) # 3


# below we have list of array and in that also we have multiple arrays so how to get any specific list value so below is the soltion

list = [['self',1],['me',3],['you',2]]

print(list[0][0]) # here list [0] (0 the index value) = [self, 1] and in that [0] = "self" so output will be "self" 

#append() ,remove()
list.append(['new',4])
print(list)
list.remove(['self',1])
print(list)

# Output : 
#[['self', 1], ['me', 3], ['you', 2], ['new', 4]]
#[['me', 3], ['you', 2], ['new', 4]]