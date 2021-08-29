class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        return self.pay * self.raise_amt

    @classmethod
    def fromstring(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    def __str__(self):
        return f'{self.first} {self.last} earns ${self.pay} annually.'

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'


class Developer(Employee):
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)
        self.employees = []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def get_employees(self):
        for employee in self.employees:
            return f'---> {employee.get_name()}'


khoi = Developer('Khoi', 'Dang', 10000, 'Python')
viet = Manager('Viet', 'Dang', 100000, )
viet.add_employee(khoi)
viet.remove_employee(khoi)
print(viet.get_employees())
print(khoi.email)
