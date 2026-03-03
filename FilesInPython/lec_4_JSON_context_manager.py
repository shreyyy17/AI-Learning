import json

# file = open('friend_json','r')
# file_contents = json.load(file)
#
# file.close()

## new methods and easier one context manager

with open('friend_json','r') as file:
    file_contents = json.load(file)



print(file_contents['friends'][0])



cars = [
    {'make':'Ford','modal':'Fiesta'},
    {'make':'Ford','modal':'Focus'},
]

with open('friend_json','w') as file:
    json.dump(cars,file)



## dumps allows you to turn dictionary into string
## loads allows you to turn string into dictionary
## json allows you to use dict and

my_json_string = '[{"name":"alfa","released":1985}]'

incorrect_car = json.loads(my_json_string)

print(incorrect_car[0])