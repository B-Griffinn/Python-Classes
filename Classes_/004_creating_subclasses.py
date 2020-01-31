# Python Class Inheritance
    ## subclasses can inherit attrs and methods from a parent class
    # great for over writing the child class without hurting the parent

## PARENT CLASS
class Employee:

    # class vars
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

## SUBCLASS 1 - DEVELOPER
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # we do not need to repeat logic from parent init method
        # will pass all args into our parent class and allow parent to handle
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

####
## MANAGER SUBCLASS
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # ADD employees from list
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # DELETE employees from list
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('~~> ', emp.fullname())



dev_1 = Developer('Ben', 'Griffin', 50000, 'Java')
dev_2 = Developer('Test', 'User', 60000, 'Python')

## DEV PRINTS
# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)


### MANAGER PRINTS
# mgr_1 = Manager('Sue', 'smith', 90000, [dev_1])

# print(mgr_1.email)
# mgr_1.add_employee(dev_2)
# mgr_1.remove_employee(dev_1)
# mgr_1.print_emps()