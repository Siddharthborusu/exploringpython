# this here is the parent class 

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return(f"{self.name} is eating")
    def sleep(self):
        return(f"{self.name} is sleeping")
    

#dog is a child class for Animal
class Dog(Animal):
    def bark(self):
        return(f"{self.name} says woof! 🐶")
    
#cat is a child class for Animal
class Cat(Animal):
    def meow(self):
        return(f"{self.name} says meow!😸")
    

my_dog = Dog("Danger")
print(my_dog.sleep())
print(my_dog.bark())
print(my_dog.eat())

#

my_cat = Cat(name='kitty')

print(my_cat.eat())
print(my_cat.sleep())
print(my_cat.meow())

    
