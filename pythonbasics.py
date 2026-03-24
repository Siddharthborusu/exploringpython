#learning python
#ref tutorial: https://www.youtube.com/https://www.youtube.com/watch?v=ygXn5nV5qFc&t=8800s
"""
this is multi line comment or docstring, it can be used to provide documentation for a module,
class, method, or function. 
It is enclosed in triple quotes (""" """) and can span multiple lines.
Docstrings are typically used to describe the purpose and usage of a piece of code,
making it easier for other developers to understand and use it effectively.
"""

print("hello sid, we're learning the basics of python and we'll get there")
name= "sdrt"
age=21 
is_student = False

# Check different types
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Check variables
age = 25
print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>

# we can use single or double quotes for strings
greeting1 = 'Hello, World!'
greeting2 = "Hello, World!"
print(greeting1)         # Hello, World!
print(greeting2)         # Hello, World!
# would print both of them regardless 



name= "sdrt"
age=23
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old

# Or use f-strings (we'll learn more later)
message = f"I am {name} and I am {age} years old"
print(message)

firstname= "siddharth"
lastname= "borusu"
fullname = firstname + " " + lastname
print(fullname)  # siddharth borusu

count = len(fullname)


#boolean 
is_18 = age == 18
can_vote = age>=18
print(can_vote)

#operations
print(age == 25)     # True - equals
print(age != 30)     # True - not equals

# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal





# logical operators
age = 25
has_license = True
drunk = False
# AND - both must be true
can_drive = age >= 16 and has_license and not drunk
print(can_drive)  # True

 
# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False