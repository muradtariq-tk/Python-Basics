# >>> Branching IF
a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Nested IF
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# Empty if statement
a = 33
b = 200

if b > a:
  pass