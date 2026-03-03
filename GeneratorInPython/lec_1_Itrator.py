class FirstHundradGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            count = self.number
            self.number += 1
            return count
        else:
            raise StopIteration()

my_gen = FirstHundradGenerator()
print(next(my_gen))
print(next(my_gen))

# itrator are those object which have dunder method


