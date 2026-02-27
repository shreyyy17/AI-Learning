## everything in python is object


class Student:
    def __init__(self,name):
        self.name = name



movies= ['Matrix','fennuo']

print(movies.__class__)


## ======================= these below are dunder methods.

## ==== why to use dunder methods
# = when you are using debugger if you are only going to implement 1 then go with repr but if you want more discritive then go with both
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self,index):
        return self.cars[index]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    # def __str__(self):
    #     return f'Garage with {len(self)} cars'

ford = Garage()
ford.cars.append("audi")
ford.cars.append("redbull")
# print(ford.__len__())
# print(ford.__getitem__(1))


for car in ford:
    print(car)


print(ford)



