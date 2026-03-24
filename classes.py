"""

Classes - Create your own data types

Without OOP: Tools scattered everywhere
With OOP: Tools organized in labeled compartments


In the context of AI, classes specifically help you:
Build clean interfaces to APIs
Manage complex data pipelines
Create reusable components
Organize stateful operations

"""
import pandas as pd 

# this is a class dog

#  __init__ is for setup when the thing is created

#__init__ looks weird with those double underscores! This is called a “dunder” method (double underscore). 
# It’s just how Python works - you’ll need to type it exactly like this.
#  Don’t worry, after writing it a few times it becomes second nature. Think of it as Python’s special way of saying “this is the setup method”.


#When defining methods in a class, you always include self as the first parameter.
# But when calling the method, you don’t pass it - Python does that automatically!

"""
Class: The blueprint (like a recipe)
Instance/Object: What you create from the class (like a cake from the recipe)

"""


class Dog:
    def __init__(self, name,breed, age):
        self.name = name
        self.breed=breed
        self.age=age

# creating a dog object - using positional arguments
dog1= Dog("danger", "golden retreiver", 5)
dog2 =Dog("gangster","pomerian", 6)

print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.breed)

dogs =[dog1,dog2]

data = []
for dog in dogs:
    data.append({
        'name':dog.name,
        'breed':dog.breed,
        'age':dog.age
    })

df = pd.DataFrame(data)
print(df)




