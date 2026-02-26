
friends = ["Rold","sold","eold","hold"]
time_since_seen=[3,7,15,11]

# here we previously converted this friends into dictionary but we can do that into simpler way using Zip function

# long_timer={
#     friends[i]: time_since_seen[i] 
#     for i in range(len(friends))  
#     if time_since_seen[i] > 5 
# }




# zip function basically combines 2 list or more into one list.

zip_value= zip(friends,time_since_seen)
long_timer = dict(zip_value)

print(long_timer)