import os

user = os.getlogin()
print(f"Your current virtual env is {os.environ.get('VIRTUAL_ENV', 'None')}")
