# Property Decorators
# allows our class attributes getter, setter and deleter functionalit

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

# add property decorator above the method
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# SETTER
    @fullname.setter
    def fullname(self, name):
        # split the name and assign first/last on the space
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Ben Griffin'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname