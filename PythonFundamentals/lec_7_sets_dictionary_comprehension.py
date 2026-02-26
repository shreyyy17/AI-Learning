friends = ["Rold","sold","eold","hold","gold","fold"]
guests = ["jose","Bob","Rold","eold","Gold"]


friends_to_lower = {n.lower() for n in friends}
guests_to_lower = {n.lower() for n in guests}

present_friends = friends_to_lower.intersection(guests_to_lower)
present_friends = [ name.title() for name in present_friends]


print(present_friends)



# creating dict. 
# here you can directly provide condition and loop inside the set like below 

friends = ["Rold","sold","eold","hold"]
time_since_seen=[3,7,15,11]

long_timer={
    friends[i]: time_since_seen[i] 
    for i in range(len(friends))  
    if time_since_seen[i] > 5 
}

print(long_timer)