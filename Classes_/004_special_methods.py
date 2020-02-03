# Special Methods - allow us to emulate built in behavior within python and operator overloading
## dunder == `__ __` so dunder init == `__init__`

class Employee:

    raise_amt = 1.04

    # initialize/constructor
    def __init__(self, first, last, pay): 
         self.first = first
         self.last = last
         self.pay = pay
         self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # repr method - is a good fallback if we call str on a class that does not have a dunder str but does have a dunder repr
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # calculate pays using dunder add custom
    def __add__(self, other):
        return self.pay + other.pay
        


# Instances
emp_1 = Employee('Ben', 'Griffin', 60000)
emp_2 = Employee('John', 'Doe', 75000)

print(emp_1)
print(emp_1 + emp_2)

# repr => unambiguous representation of the object and should be used for debugging and logging. Intended to be seen by other devs
# repr(emp_1)

# str => readable representation of an object used to display to the end user
# str(emp_1)