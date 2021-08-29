class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    # def __str__(self):
    #     return f'{self.name} is {self.age} years old who got {self.grade} in the test.'

class Course:
    def __init__(self, name, max):
        self.name = name
        self.max = max
        self.ave_grade = 0
        self.student_lst = []
        self.student_str = ''

    def add_student(self, student):
        if len(self.student_lst) < self.max:
            self.student_lst.append(student)

    def ave_grades(self):
        for i in self.student_lst:
            i = i.get_grade()
            self.ave_grade += i
        self.ave_grade = self.ave_grade / len(self.student_lst)
        return self.ave_grade


    def __str__(self):
        for a in self.student_lst:
            self.student_str += f'{a.name}, '
        return f'The {self.name} course has {len(self.student_lst)} students, namely {self.student_str}. The average grade is {self.ave_grade}'

ken = Students('Ken', 10, 10)
khoi = Students('Khoi', 10, 30)
print(ken)
maths = Course('maths', 2)
maths.add_student(ken)
maths.add_student(khoi)
print(maths.ave_grades())
print(maths)
