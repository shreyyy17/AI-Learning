##
divide = lambda x,y : x/y
print(divide(10,2))


# =================================

# avg = lambda seq: sum(seq) / len(seq)
# total = lambda seq: sum(seq)
# top = lambda seq: max(seq)


# to optimise the code we can directly use this functions inside the dictionary association like below


## Association

operations = {
    "avg" : lambda seq: sum(seq) / len(seq),
    "total":sum, # here we can pass directly sum function because there is no other calculation
    "top":max
}
students = [
    {"name":'roy',"grade":(90,24,64,76)},
    {"name":'soy',"grade":(60,90,87,65)},
    {"name":'foy',"grade":(40,65,23,87)},
    {"name":'doy',"grade":(30,34,45,88)},
]


for student in students:
    name = student["name"]
    grade = student["grade"]
    
    print(f"Student:{name}")
    operation = input("Enter what you want (avg,total or top) :")
    
    # if operation == "avg":
    #     print(avg(grade))
    # elif operation == "total":
    #     print(total(grade))
    # elif operation == "top":
    #     print(top(grade))
    # else:
    #     print("You have made wrong selection !!!")
    
    
    ## using association we don't require to write this much of code
    
    operation_function = operations[operation]
    print(f" Here is your result : {operation_function(grade)}")