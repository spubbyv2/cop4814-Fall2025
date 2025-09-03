"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================
print("Gred", 3.14, 10) # this is a single line comment

"""This is a block comment"""
# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================
message = "Welcome to FIU"
print(type(message)) #type() is a function too, displays the datatype of an object
print(message)

a = 10
b = 2
print(type(a), type(b))

isOpen = True
print(type(isOpen))

print(message[0]) #outputs first index of a string
print(type(message[0]))
print(message[5])


# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(7 / 2) #division
print(7 // 2) #integer division
print(7 % 2)
print(a ** b) #exponents


# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "Sebastian"
last_name = "Medina"

print(first_name + last_name) #one object
print(first_name + " " + last_name) #still one object
print(first_name, last_name) #two objects

print(f"My name is {first_name} {last_name}.") #"f" formats (like printf) and string objects must be encased in {}
print(f"My name is {first_name.upper()} {last_name.title()}.")
print("2" + "3") #concatination
print(2 + 3) #addition

print("***Welcome to Software Dev***".strip('*'))
# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

# Lists (often associated with Arrays)
professors = ["greg", "richard", "kianoosh", "debra", "jason", "leo", "heather"]
print(type(professors))
print(professors[0]) #returns first index
print(professors[-1]) #returns last index
print(professors[2:5]) #defines what indexes are included (2,3,4)
print(professors[:5]) #starts from index 0, ends at 4
print(professors[3:]) #starts from index 3 all the way to the end
print(professors[:]) #outputs everything (creates a copy of a given list)

professors.append("todd")
print(professors)
professors.extend(["michael", "mustafa", "naomi"])
print(professors)
professors.insert(2, "vyoma")
print(professors)
professors.remove("greg")
print(professors)
x = professors.pop(2) #removes a record based off index
print(professors,x)
professors.reverse()
print(professors)

professors.sort() #sorts in alphabetical order
print(professors)
professors.sort(reverse=True) #does so in reverse order
print(professors)
# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78, 99.5) #immutable, cannot alter
print(type(grades))
# grades[0] = 91.3 would give an error

members = {"greg", "richard", "greg"}
print(members) # this is going to be the answer of a future assignment :)


# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================



