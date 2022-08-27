# >>> Basic Datatypes
# >>> String

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

txt = "welcome to the jungle"
x = txt.split(" ")
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

# >>> int, float, complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
# float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
# complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# >>> boolean
a=True
b=False
print(a,b)
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))