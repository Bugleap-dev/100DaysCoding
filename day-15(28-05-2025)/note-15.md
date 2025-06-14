# **DAY 15 - 28/05/2025**

# **CS50P: Introduction To Programming with Python**

## Table of Contents
1. [Dictionaries (dict)](#1-dictionaries-dict)

2. [Looping Through Dictionaries](#2-looping-through-dictionaries)

3. [Formatting Dictionary Output](#3-formatting-dictionary-output)

4. [List of Dictionaries](#4-list-of-dictionaries)

5. [Mini Project: Mario Blocks (Column Print)](#5-mini-project-mario-blocks-column-print)

### 1. Dictionaries (dict)
Dictionaries store key-value pairs, useful for mapping related information.

```py
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

print(students["Ron"])     # Output: Griffindor
print(students["Harry"])   # Output: Griffindor
```

### 2. Looping Through Dictionaries
Iterating through keys of the dictionary:

```py
for student in students:
    print(student)

#Output:
Hermione
Harry
Ron
Draco
```

## 3. Formatting Dictionary Output
Printing key-value pairs together:

```py
for student in students:
    print(student, students[student])

# Output:

Hermione Griffindor  
Harry Griffindor  
Ron Griffindor  
Draco Slytherin
```

- Using sep=", " for cleaner formatting:

```py
for student in students:
    print(student, students[student], sep=", ")

# Output:

Hermione, Griffindor  
Harry, Griffindor  
Ron, Griffindor  
Draco, Slytherin
```

### 4. List of Dictionaries
Storing multiple dictionaries in a list allows complex data representation:

```python
students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

#Output:

Hermione, Griffindor, Otter  
Harry, Griffindor, Stag  
Ron, Griffindor, Jack Russell terrier  
Draco, Slytherin, None
```

### 5. Mini Project: Mario Blocks (Column Print)
Basic example of abstraction and function usage.

```python
def main():
    print_column(3)

def print_column(height):
    for i in range(height):
        print("#")

main()

### Output:
#
#
#
```