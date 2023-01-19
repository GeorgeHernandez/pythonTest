"""
This is a Hello world test.
Every module should have a module-level docstring.
"""

# Run me with: python hello.py
# If VSC & Python extension installed,
# then run by right-click to "Run Python File in Terminal"

# Some random dictionary
my_dict = {"user": "George", "address": "123 Main St", "age": 25}

# Variant without a labeled input request:
# who = input()
# print("Hello", who)

# Variant with a labeled input request:
def hello(name):
    """Take a name and respond."""
    return "Hello " + name


name_again = input("Enter your name: ")
print(hello(name_again))
