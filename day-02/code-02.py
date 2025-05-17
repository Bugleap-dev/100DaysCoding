# DAY 2 - 15/05/2025
#CS50P: Introduction To Programming with Python
#SHORTS

### STRING EFFECTS:

def main():
    guess = int(get_guess())

    if guess == 50:
        print("Correct!")

    else:
        print("Incorrect!")

def get_guess():
    guess = input("Enter a guess: ")
    return guess

main()


### SIDE EFFECT:

emoticon = ":("

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Hi there!")

def say(phrase):
    print(phrase + " " + emoticon)

main

#Output:
# Is anyone there? :(
# Ho there! :D


#########################

# EXERCISE:
# 🔹 1. Print Basics

# a. Print Basics
print("Hello "+"World!")
print("Hello","World!",sep="-")
print("Hello", "World!")

"""
Output:
Hello World!
Hello-World!
Hello World!
"""

# b. Newline Character
print("Hello\nCS50P\nPython")

# 🔹 2. Input & Output

# a. Greeting with F-string
name1 = input("Enter your name: ")
print(f"Hello {name1}")

# b.String Length**  
word = input("Enter a word: ")
print(f"The numbers of characters in your word is {len(word)}")

# 🔹 3. String Methods

#**a. Capitalize and Title**  
name2 = input("")
print(f"Your name is Capitalized format: {name2.capitalize()}")
print(f"Your name is Title case: {name2.title()}")

#b. Whitespace Trimming**  
name3 = input("Enter your name: ")
print(f"Your name without left whitespaces: {name3.lstrip()}")
print(f"Your name without right whitespaces: {name3.rstrip()}")
print(f"Your name without whitespaces: {name3.strip()}")

#🔹 4. Integer and Float

# a. Simple Calculator
num1 =input("Enter num1: ")
num2 =input("Enter num2: ")
add = int(num1) + int(num2)
multiply = int(num1) * int(num2)
remainder = int(num1) % int(num2)
print(f"Summation: {add}")
print(f"Product: {multiply}")
print(f"Remainder: {remainder}")

# b. Float Addition with Rounding
num3 = input("Enter your number: ")
num4 = input("Enter your number: ")

addition = float(num3) + float(num4)
print(f"Sum: {addition}")
print(f"Rounding to 1 decimal place: {addition:.1f}")
print(f"Rounding to 2 decimal place: {addition:.2f}")
print(f"Rounding to 3 decimal place: {addition:.3f}")

# 🔹 5. Round Function

print(round(2.5))           # Output: 2
print(round(3.5))           # Output: 4
print(round(-2.5))          # Output: -2
print(round(-3.5))          # Output: -4

## 🔹 6. Defining Functions

# a. Hello Function
def hello(name = "World"):
    print(f"Hello {name}!")
    name = input("Enter your name: ")
    print(f"Hello {name}!")


hello()

# b. Split Full Name
name4 = input("Enter your name in Firstname, Lastname order:")
firstname,lastname = name4.split(" ")

print(f"Your firstname: {firstname}")
print(f"Your firstname: {lastname}")

# 🔹 7. Return vs Print
**a. Add Function with Return**
Create a function add(a, b) that returns the sum.
Get two numbers from the user and print the result.

**b. Square Function**
Write a function square(n) that returns n ** 2.
Prompt the user and print the squared value.