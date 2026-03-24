"""
function syntax
def function_name():
    #code goes here
    #must be indented

"""


def greet():
    print("hey its siddharth")
    print("its gonna happen!")


greet()


def check_weather():
    temperature = 29
    if temperature > 25:
        print("its hot")
    else:
        print("its nice weather")


check_weather()


# paramters in the functions
def greet_user(name, age):
    if age >= 18:
        print(f"hello {name}, you can vote")
    else:
        print(f"hey {name} ,you cannot vote")


greet_user("siddharth", 20)
greet_user("dan", 16)


# learning about the global vs local variables
discount = 20


def calculate_total(price):
    # default values
    tax_rate = 0.08
    # since discount here is declared locally
    discount = 10

    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total {final_price}")


calculate_total(100)

print(discount)  # prints 20 since it points out to the global variable


# learning about the return
def add_print(a, b):
    print(a + b)


add_print(10, 15)


# return helps us capture, use and redo the value later
def add_return(a, b):
    return a + b


add_return(10, 15)
result = add_return(10, 65)
result += 14
print(f"the result that is : {result}")
