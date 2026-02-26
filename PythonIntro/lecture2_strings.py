my_string = 'Hello world !'
print(my_string)

# in python yu cannot combine int and string together

#if you want to print any variable that we have created put f in the starting like below 

name = "shrey"
print(f'my name is {name}')

# there are alternative ways also using format function like below
#here in the getting string we are passing empty braces that is replaced my the string that we are passing in the format function 


name = "jariwala"
greeting_string = 'Hello mr. {}!'
formatted_string = greeting_string.format(name)
print(formatted_string)



# getting user name by user input using input() function

my_name= "shrey"
user_name= input('please enter your name:')
print(f"Hello {user_name}. My name is {my_name}")


# example for input by caculating age 

age = input("Enter you age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months ")


# EXERSICE: 1 ===> calculate how many seconds user has lived based on age 


user_age = input("Please Enter your Age : ")
age_num = int(user_age)
age_to_days= age_num * 365
age_to_sec = age_to_days * 24 * 60 * 60
print(f"You have lived for {age_to_sec} seconds")
 

