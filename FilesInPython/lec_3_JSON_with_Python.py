import json

file = open('friend_json','r')
file_contents = json.load(file)

file.close()

# print(file_contents['friends'][0])



cars = [
    {'make':'Ford','modal':'Fiesta'},
    {'make':'Ford','modal':'Focus'},
]

file = open('friend_json','w')
json.dump(cars,file)
file.close()


## dumps allows you to turn dictionary into string
## loads allows you to turn string into dictionary
## jso allows you to ue dict and

my_json_string = '[{"name":"alfa","released":1985}]'

incorrect_car = json.loads(my_json_string)

print(incorrect_car[0])