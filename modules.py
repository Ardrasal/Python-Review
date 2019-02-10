# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# import datetime
# or
from datetime import date
import time
# or
from time import time

# Pip module
from camelcase import CamelCase  # pipenv install camelcase

# Import custpm module
import validator
from validator import validate_email


c = CamelCase()
# print (c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')

today = date.today()
# today = datetime.date.today()
# timestamp = time.time()
# using line 8
timestamp = time()

# print(today)
print(timestamp)
