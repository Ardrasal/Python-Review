# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor (A function that runs when you instantiate an object from a class)
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}. :)'

    def has_birthday(self):
    # Adds 1 to age.
        self.age += 1

# Extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}, and my balance is ${self.balance}. :('

# Init user object
anna = User('Anna Smith', 'anna@gmail.com', 36)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

# print(type(anna))
# print(anna.age)
anna.has_birthday()
print(anna.greeting())
