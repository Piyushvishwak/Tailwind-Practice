# -----------------------------
# Python Data Types / Object Types
# -----------------------------

# ---- Number Types ----
# num1 = 1234          # Integer
# num2 = 3.1415        # Float
# num3 = 3 + 4j        # Complex number
# num4 = 0b111         # Binary literal (7 in decimal)
# from decimal import Decimal
# num5 = Decimal('10.5')   # Decimal type
# from fractions import Fraction
# num6 = Fraction(1, 3)    # Fraction type

# # ---- String Types ----
# s1 = 'spam'                 # String with single quotes
# s2 = "Bob s"                # String with double quotes
# s3 = b'a\x01c'              # Bytes literal
# s4 = u'sp\xc4m'             # Unicode string
# s5 = 'three'                # Another string

# # ---- List ----
# lst1 = [1, 2, 3, 4.51]             # List with numbers
# lst2 = list(range(10))             # List from 0 to 9

# # ---- Tuple ----
# t1 = ('U',)                        # Single-element tuple
# t2 = tuple('spam')                 # Tuple of characters
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# t3 = Point(2, 3)                   # Named tuple

# # ---- Dictionary ----
# d1 = {'food': 'spam', 'taste': 'yum'}   # Dictionary
# d2 = dict(hours=10)                     # Dictionary using dict()

# # ---- Set ----
# s1 = set('abc')                 # Set from string characters

# # ---- File ----
# f1 = open('eggs.txt')           # Open file (read mode by default)
# f2 = open(r'C:\ham.bin', 'wb')  # Open file in binary write mode

# ---- Boolean ----
# True, False

# ---- None---
# None

# ---- Functions ----
# function
# modules
# classes

# ---- Advance ----
# decorators
# generators
# context managers
# iterators
# meta programming

print("Data types and object types are defined in the comments above.")

username="JohnDoe"
print(f"Username: {username}")
print(username[-1])
print(username[0:4])
print(username[4:])
