"""
Python Skills Assessment
Try to solve each challenge. If you get stuck, just write "# STUCK" and move on.
Don't look anything up - I want to see what you know NOW.
"""

# === CHALLENGE 1: Data Structures ===
# Create a list of your top 3 programming languages
# Then add "Python" to the end of the list
# Print the entire list

# Your code here:
programs = ["java","C#","Python"]
print(programs)



# === CHALLENGE 2: Dictionary ===
# Create a dictionary representing a person with keys: name, age, city
# Then print just their age

# Your code here:
person = {
	"name": "RDC",
	"age": 35,
	"city": "Paris"
}
#dont remember dictionnaries... can pick it up again fast though
print(person["age"])


# === CHALLENGE 3: Loop ===
# Write a loop that prints numbers 1 to 10

# Your code here:
number = 1
while number <= 10:
	print(number)
	number = number + 1
#dont remember correct synthax

# === CHALLENGE 4: Function ===
# Write a function called 'greet' that takes a name parameter
# and returns "Hello, [name]!"
# Then call it with your name

# Your code here:
name = "Ricardo"

def greet(name):
	print("Hello, " + name + "!")

greet(name)


# === CHALLENGE 5: Conditional ===
# Write code that checks if a number is even or odd
# If even, print "Even", if odd, print "Odd"
# Test with number = 7

# Your code here:

number = 7

def evenOrOdd(number):
	if number%2 != 0:
		print("Odd")
	else:
		print("Even")
evenOrOdd(number)
#dont remember if there's a function to check if a number is odd or not

# === CHALLENGE 6: List Comprehension ===
# Create a list of squares of numbers 1-5 using list comprehension
# (e.g., [1, 4, 9, 16, 25])

# Your code here:

# I could create a function that starts working with 1, calculates its square,
# stores it into a sort of list, then adds 1 to the last number it worked with
# so long as the number isn't 6, at which point it should stop, and then go
#back again at calculating its square and storing it into the list, etc, maybe
# printing out the list once the number it should work with is 6
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# === CHALLENGE 7: File I/O ===
# Write code that:
# 1. Creates a file called "test.txt"
# 2. Writes "Learning Python" to it
# 3. Closes the file
with open("test.txt", "w") as file:
    file.write("Learning Python")
# File auto-closes!

# Your code here:
#dont know... i've done it in the past, but, dont know how to now


# === CHALLENGE 8: Error Handling ===
# Write code that tries to divide 10 by 0
# Catch the error and print "Cannot divide by zero"

# Your code here:

#dont know... did it in the past though
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# === CHALLENGE 9: Class ===
# Create a simple class called Dog with:
# - An __init__ method that takes 'name'
# - A method called 'bark' that prints "[name] says Woof!"
# Then create a Dog instance and make it bark

# Your code here:

#dont remember using an __init__ function, although I may have
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy")
buddy.bark()

# === CHALLENGE 10: String Manipulation ===
# Take this string: "  hello world  "
# Remove whitespace from both ends and capitalize each word
# Result should be: "Hello World"

# Your code here:
# did this in the past... dont remember it now
text = "  hello world  "
result = text.strip().title()
print(result)  # Hello World
