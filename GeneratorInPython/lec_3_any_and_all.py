friends = [
    {
        "name": "Rolf",
        "location": "Washington DC",

    },
    {
        "name": "Rolf",
        "location": "Washington DC",

    },
    {
        "name": "Rolf",
        "location": "Washington DC",

    },
    {
        "name": "Rolf",
        "location": "Washington DC",

    },
]


your_location = input("Enter your location: ")

friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby) > 0:
    print("You are not alone !!!!!")
