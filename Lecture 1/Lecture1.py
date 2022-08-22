# >>> output some thing
print("Hello, World!")

# >>> no brackets
if 5 > 2:
       print("Five is greater than two!")

# >>> my first program
a = 10
print(a)

# >>> multi line comments
#This is a comment
#written in
#more than just one line
print("Hello, World!")

# >>> Paragraph comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# >>> Changing types of a value
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# >>> Check type of a variable
x = 5
y = "John"
print(type(x))
print(type(y))

# >>> double and single quotes difference
x = "John"
# is the same as
x = 'John'

# >>> Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

# >>> Variable name rules
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
# Variable names are case-sensitive (age, Age and AGE are three different variables)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case Variables
myVariableName = "John"
#Pascal Case Variables
MyVariableName = "John"
#Snake Case Variables
my_variable_name = "John"




# >>> Assigning multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# >>> Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# >>> Output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



# >>> Global Variables
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
# concept
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
