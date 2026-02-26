# while loops and for loops 


#While loop =============================
is_learning = True

while is_learning:
    print("learning is on going")
    user_input = input("Are you currently learning ? : ")
    is_learning = user_input == "yes" 
    
    
    
    
# For loops ==========================

friend = ['rey','clay','bro']
family = ['roy','toy','cloy']

for name in friend:
    print(name)
    
    
# in large number of values in the loopyou can specify how many and from which position you want like here using range we are showing from 5 to 10 and last 10 is ignored so 5, 6, 7, 8, 9 is output

elements = [0,1,2,3,4,5,6,7,8,9]

for index in range(5,10):
   print(f"Hello Loops {index}") 

# if ou dont want to use the value so you can set var name to be _ like below

for _ in range(5,10):
   print("Hello Loops") 

    
# loop with dictionary
students = [
    {"name":'roy',"grade":90},
    {"name":'soy',"grade":60},
    {"name":'foy',"grade":40},
    {"name":'doy',"grade":30},
]

for student in students:
    name=student["name"]
    grade= student["grade"]
    
    print(f"student name is {name} and grade is {grade}")