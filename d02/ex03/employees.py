class Employee:
    salary = 3000
    name = 'data scientist'
    description = 'A professional who can analyze data with code.'

    def __init__(self):
        pass

    def __str__(self):
        print(f'name: "{self.name}"')
        print(f'salary: {self.salary}')
        print(f'description: "{self.description}"')


class Janitor(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 1000
        self.name = 'Janitor'
        self.description = 'A profession who keeps the facilities clean.'


class Receptionist(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 1300
        self.name = 'Receptionist'
        self.description = 'A profession that helps visitors to connect ' \
                           'with the staff.'


class Cook(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 3000
        self.name = 'Cook'
        self.description = 'A profession who cooks a meal for the staff.'
