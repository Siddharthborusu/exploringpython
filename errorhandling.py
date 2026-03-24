"""
Errors happen. 
Files might not exist, APIs might be down, users might enter invalid data.
 Error handling lets your program deal with these problems gracefully instead of crashing.

Errors you make as a programmer:
Typos and syntax mistakes (VS Code shows yellow squiggly lines)
Logic errors like dividing by zero (only show up when code runs)
Using variables before defining them
Calling methods that don’t exist
"""

"""
examples of errors:

# Missing colon
if x > 5  # SyntaxError
    print("Big number")

    
# Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
print(score)  # NameError

# Wrong type
"hello" + 5  # TypeError


Why handle errors?

# This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing

The following program handles the error's
"""
# This keeps running even if file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here


"""
The try block contains code that might fail. The except block runs if an error happens:
"""

#catching specific errors
try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")



#Multiple error types

try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


"""

The else clause
Code in else runs only if no error happened:
"""

try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")


"""
The finally clause
Code in finally always runs, error or not:
"""

try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")