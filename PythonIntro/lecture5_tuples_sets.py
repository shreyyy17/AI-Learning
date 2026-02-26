#tuples are immutable and it is defined inside the () braces

tuple=('self',1)


# sets does not contains duplicate values inside it.
# sets does not keeps order

art_friends = {"holf","golf"}
sci_friends= {"ken","jen"}

# we can use append to add the value inside set
art_friends.add("ven")
sci_friends.add("golf")
print(art_friends)
print(sci_friends)

# we can use remove to remove the value inside set
art_friends.remove("ven")
sci_friends.remove("golf")
print(art_friends)
print(sci_friends)


# advanced set operations 
art_friends = {"holf","golf","rolf"}
sci_friends= {"ken","golf","charlie"}


# diffrence check what are the elements that is in one and not in the other 
art_but_not_science = art_friends.difference(sci_friends)
print(f"Diffrence: {art_but_not_science}")

# symmetric_diffrence means that check what elements are not in both 
not_in_both = art_friends.symmetric_difference(sci_friends)
print(f"symmetric_diffrence : {not_in_both}")

# intersection 
# union gives full result from bth sets 

#Exercise 2 :
nearby_people = {"Rolf", "Jen", "Anna"}
user_friends = set()  # This is an empty set, like {}

friend = input("Enter your friend name to see if he is nearby: ")

# Add the friend to the user_friends set
user_friends.add(friend)

# Print out the friends that are nearby... those which are in both sets!
print(user_friends.intersection(nearby_people))

