#lists
"""
Lists: Like a shopping list (ordered items)
"""
name='sdrt'
my_list=['ai','ml','ds','dl', name]
print(my_list)
my_list[0]='artificialintelligence'
print(my_list[0:5])
my_list.append("hello")
my_list.append("hi")
my_list.remove('ml')

my_list.append('hey')
my_list.insert(1,'why')

# list methods
print(len(my_list))
print(my_list.count('hey'))
print(my_list.index('hi'))
print(my_list.sort())
print(my_list.reverse())

new_list=my_list.copy
print(new_list)



#dictionary 
person = {
    "name" : "Siddharth",
    "age"  : 25,
    "city" : 'Hyderabad'
}



person['name']
person['city']

person['license'] = False
del person['license']

#tuple - immutable and hence cant be changed
empty=()
point=(3,5)
colors = ('red', 'blue', 'green', 'orange')
colors.index('orange')


# sets


# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange", 'mango', 'berry', 'banana'])
# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}





