import functools

user = {'username':'shrey123','access_level':'admin'}

def user_has_permission(func):
    @functools.wraps(func) ## from this we can see exact function we are calling through dunder method
    def secure_func(panel):
        if user.get('access_level') == "admin":
            return func(panel)
    return secure_func
    # raise RuntimeError

@user_has_permission('admin')
def my_function(panel):
    return f'Password for admin {panel} panel is 1234'





print(my_function.__name__)
print(my_function("Sports"))
print(my_function.__doc__)