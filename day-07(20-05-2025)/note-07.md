# **DAY 07 - 20/05/2025**

# **CS50P: Introduction To Programming with Python**

# Lecture 1 – Conditionals (Continued)

---

## Table of Contents
1. [Even or Odd Function](#even-or-odd-function)

2. [House Assignment Using if-elif](#house-assignment-using-if-elif)

3. [House Assignment Using match Statement](#house-assignment-using-match-statement)

4. [Grouping Cases in match](#grouping-cases-in-match)

---

### Even or Odd Function
Demonstrates how to create a simple function is_even() to check whether a number is even or odd.

```py
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0


main()
```

### House Assignment Using if-elif
Uses multiple if-elif conditions to match the user's input (student name) to their Hogwarts house.

```py
name = input("What's your name: ")
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

```
### House Assignment Using match Statement
Introduced in Python 3.10, the match statement simplifies multiple condition checking.

```py
name = input("What's your name: ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

### Grouping Cases in match
Improved version of the above match statement using pattern grouping to avoid repetition.

```py
name = input("What's your name: ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```