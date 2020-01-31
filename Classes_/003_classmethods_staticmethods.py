# reg methods - automatically take the instance (self) as the first argument.

# class methods - automatically take the class as the first argument.
    # add a `@` decorator to the class method
    # A class method receives the class as implicit first argument, just like an instance method receives the instance self

# static methods - dont pass anything automatically! Behave just like regular functions but have logical connections to the class

class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # @ decorator sets a class method
    @classmethod
    def set_raise_amt(cls, amount):
        # working with our class and not the instance
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Ben', 'Griffin', 50000)
emp_2 = Employee('Test', 'User', 60000)


## STATIC METHODS
import datetime # date time module
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))



### Class Methods
# we can use class methods to provide many ways of creating our objects
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-75000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

###############################
# use class method to update raise amt
# we do not generally run class methods on single instances bc it changes the entire class no matter what.
    # Employee.set_raise_amt(1.05)
    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)