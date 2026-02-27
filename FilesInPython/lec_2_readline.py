



friends = input("Enter three friend names, separated by a comma (np spaces, please) :").split(',')

people = open('demo','r')
people_nearby=  [line.strip() for line in people.readlines()]
people.close()

friends_set=set(friends)
people_nearby_set=set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)
print(friends_nearby_set)
nearby_friends_file = open('nearby_friends', 'w')
for friend in friends_nearby_set:
    print(f"{friend} is nearby !! Meet u with them")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()