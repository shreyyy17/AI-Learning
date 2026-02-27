my_student = {
    'name': 'rolf',
    'grades':[70,85,96,45],
    # 'average
}

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades


    def average(self):
        average = sum(self.grades)/len(self.grades)
        return average

student_one=Student('Rolf',[70,85,96,45])
student_two=Student('Golf',[40,35,94,23])
print(student_one.average())
print(student_two.name)

