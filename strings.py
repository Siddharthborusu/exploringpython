# learning strings
# An f-string is a Python string that lets you put variables or calculations directly inside {} by adding f before the quotes.
name = "siddharth"
greeting = f"hello {name}"
print(greeting)
name_upper = name.upper()
name_lower = name.lower()
print(name_lower, name_upper)

# repetetion

star = "*"
stars = star * 10  # "**********"

separator = "-" * 20  # "--------------------"
print(stars, separator)


# finding and replacing the words in strings

message = "the world is beautiful"
message_upper = message.upper()
print("world " in message)
print(message.startswith("the"))  # returns true
# replacing certain words
message = message.replace("the", "The")
message = message.replace("beautiful", "absurd")
print(message)
