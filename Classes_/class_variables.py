# Class Variables are variables that are shared among all instances of a class
    # Class vars should be the same for each instance 

class Employee:

    # class vars
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # __init__ methods run every time we create a new employee/instance 
        # not using self bc we do not want it over written by new instances
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Ben', 'Griffin', 50000)
emp_2 = Employee('Test', 'User', 60000)


# num of employees
print('Number of employees', Employee.num_of_emps)


# update class var for entire class
# Employee.raise_amount = 1.05

# update class var for specific employee
# emp_1.raise_amount = 1.05


# print('Employee.raise_amount: ', Employee.raise_amount)
# print('emp_1.raise_amount: ', emp_1.raise_amount)
# print('emp_2.raise_amount: ', emp_2.raise_amount)

# print('Namespace of emp1', emp_1.__dict__ )
# # print('Namespace of EMP', Employee.__dict__ )

