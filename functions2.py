def calculate_area(width,height):
    area = width*height
    area = 1.05* area
    return area



room_area =calculate_area(width=34.5, height=43.4)
print(f"Room size is : {room_area} sq ft")



# more examples of the returned values

def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

# another example of the return functions
def simple_function():
    numbers=[1,2,3,4,5]
    first_number=numbers[0]
    last_number=numbers[-1]
    return first_number,last_number

fist_number, last_number = simple_function()
