friend = ['rey','clay','bro']
family = ['roy','toy','cloy']

user_name = input('please enter your name: ')

if user_name in friend:
    print("access granted to friend")
elif user_name in family:
    print("you are family authorized person")
else:
    print("you are not family or friends so not authorized")