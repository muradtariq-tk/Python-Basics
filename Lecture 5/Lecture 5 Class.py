# >>> Classes
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)


# Initialization function
class Person:
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object functions/methods
class Person:
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# >>> delete object
del p1

