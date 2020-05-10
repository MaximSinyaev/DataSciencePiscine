from employees import Employee, Janitor
from employees import Receptionist, Cook
import random


class HR:
    def __init__(self):
        self.month = 0

    class Retire(Employee):
        name = 'Retiring employee'
        salary = 2100
        description = 'I am retiring, give me a bonus!'

    class ExhaustionException(Exception):
        def __init__(self):
            message = "This employee is exhausted and cannot work anymore"
            super().__init__(message)

    def vacation(self):
        self.month = 0

    def work(self, empl):
        self.month += 1
        if self.month > 10:
            raise HR.ExhaustionException
        return random.choice([empl, self.Retire])


if __name__ == "__main__":
    pass