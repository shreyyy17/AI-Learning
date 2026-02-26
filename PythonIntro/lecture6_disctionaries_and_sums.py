# dictionary contains {key:value} property and it is mutable 

friends_ages = {"rolf":21,"self": 24}

print(friends_ages["self"])

# add new value
friends_ages['roy'] = 35



print(friends_ages)


# convert array into dictionaty using dict() funtion like below 

frined = [("rolf",22),('roy',25)]
friends_ages = dict(frined)
print(friends_ages)

#Sum Function
grades = [32,52,95,85,65]

total = sum(grades)
len = len(grades)

print(f"{total} === {len}")



# for comma sapreted values  
friends = ["solf","golf","eolf"]
comma_saprated_value = "- ".join(friends)
print(comma_saprated_value)



