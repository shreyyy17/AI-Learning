class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []  

    def average(self):
        return sum(self.marks)/len(self.marks)


class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    def weekly_salary(self):
        return self.salary * 40


rolf = WorkingStudent('Rolf','Fennu',23)
print(rolf.salary)
rolf.marks.append(100)
rolf.marks.append(90)
print(rolf.average())

print(rolf.weekly_salary())