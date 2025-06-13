# **DAY 13 - 26/05/2025**

# **CS50P: Introduction To Programming with Python**

## Lecture 2 – Loops (Continued)

## Table of Contents

Using Return to Exit Loops

Modular Loop with Functions

Introduction to Lists

Accessing List Elements

Iterating Over Lists

Enumerating Lists with Index

### 1. Using return to Exit Loops
Using return in a function both exits the loop and ends the function early.
```py
def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break   # This can also be replaced by 'return n'
    return n
```
### 2. Modular Loop with Functions
Encapsulates input validation and repetition logic in separate functions:
```py
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            return n    # Cleaner: return ends loop & function

def meow(n):
    for _ in range(n):
        print("meow")

main()
```
3. Introduction to Lists
Lists allow storage and access of multiple values in a single variable.

```py
students = ["Hermione", "Ron", "Harry"]

print(students)       # Prints the entire list
print(students[0])    # Accesses individual elements
print(students[1])
print(students[2])

#Output:

['Hermione', 'Ron', 'Harry']
Hermione
Ron
Harry
```

### 4. Accessing List Elements in a Loop
Looping directly over elements (preferred and more Pythonic):

```py
students = ["Hermione", "Ron", "Harry"]

for student in students:
    print(student)

# Output:
Hermione  
Ron  
Harry
```
### 5. Enumerating Lists with Index
Using range() and len() to access both index and value:

```py
students = ["Hermione", "Ron", "Harry"]

for i in range(len(students)):
    print(str(i + 1) + ". ", students[i])

Output:
1.  Hermione  
2.  Ron  
3.  Harry
```