# functions should be defined in pytho by def like below 

def greet():
    name=input('please enter your name :')
    print(f"Hello, {name}!")
    
    
greet()
    
    
# you can not call function before it intialized like below 

# greet()

# def greet():
#     name=input('please enter your name :')
#     print(f"Hello, {name}!")


# now handle the paramter inside the function


def greet(surname):
    name=input('please enter your name :')
    print(f"Hello, {name} {surname}!")
    
    
greet("jariwala")



# running function using variable 

cars=[
    {
    "make":"Ford",
    "model":"Fiesta",
    "mileage":23000,
    "fuel_consuption":460,
},  {
    "make":"Ford",
    "model":"Focus",
    "mileage":17000,
    "fuel_consuption":350,
},  {
    "make":"mazda",
    "model":"MX-5",
    "mileage":43000,
    "fuel_consuption":900,
},  {
    "make":"mini",
    "model":"Cooper",
    "mileage":31000,
    "fuel_consuption":235,
},
]


def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consuption"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")
    
    
for car in cars:
    calculate_mpg(car)
    
    
    
    
# Functions and Return Values 



def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consuption"]
    return mpg
    
def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

def car_info(car):
    name = car_name(car)
    mpg= calculate_mpg(car)  
    return f"{name} does {mpg} miles per gallon"
    
    
for car in cars:
  print(calculate_mpg(car)) 