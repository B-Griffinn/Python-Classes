# Create and Instantiate simple classes
# Classes are great for logically grouping data and functions in a way that is easy to reuse and build upon if need be.

    # Data in a class = attributes
    # Functions in a class = methods 

class Employee:
    # initialize/constructor
    def __init__(self, first, last, pay): 
         self.first = first
         self.last = last
         self.pay = pay
         self.email = first + '.' + last + '@company.com'
    
    # initialize an action for our employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def emp_email(self):
        return self.email


# Instance example
emp_1 = Employee('Ben', 'Griffin', 60000)
print(emp_1.email)
print(emp_1.fullname()) # method and not an attr so () is needed
print(emp_1.emp_email())