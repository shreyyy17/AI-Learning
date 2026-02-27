## this is for @classmethod

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()

## this is for @staticmethod

class Foo:
    @staticmethod
    def hi():
        print("Hellow this is static methid")


my_object = Foo()
my_object.hi()




## Examples ==================================
class FixedFloat:
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return f'<FixedFloat {self.value:.1f}>'

    @classmethod
    def from_sum(cls,val1,val2):
        return cls(val1+val2)

number = FixedFloat(10.5869)
valule = FixedFloat.from_sum(16.054,55.23)
print(number)
print(valule)




## -----2

class Euro(FixedFloat):
    def __init__(self,value):
        super().__init__(value)
        self.symbol = 'e'

    def __repr__(self):
        return f'<Euro {self.symbol} {self.value:.2f}>'

money = Euro.from_sum(79.454,10.33)
print(money)

## classmethod is more feasible and understandable to use
# don't use staticmethod
