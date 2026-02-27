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

    @property ## with use of this we don't need to add () after calling this function
    def weekly_salary(self):
        return self.salary * 40


rolf = WorkingStudent('Rolf','Fennu',23)

print(rolf.weekly_salary) # # here we can see




