# >>> Range
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number.

x = range(6)
for n in x:
    print(n)

x = list(range(6))
for n in x:
    print(n)

x = range(3, 6)
for n in x:
  print(n)

x = range(3, 20, 2)
for n in x:
  print(n)  