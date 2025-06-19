# **DAY 16 - 29/05/2025**

# **CS50P: Introduction To Programming with Python**

# EXERCISE

### SET 3: Lists & Dictionaries

1. Add "Luna" to the list below and print each student on a new line with their number (e.g., 1. Hermione, ...):

```python
students = ["Hermione", "Ron", "Harry"]
```
2. Using a for loop, print only the names of students from this dictionary who belong to "Griffindor":

```python
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}
```

3. Using this list of dictionaries, print only the students whose patronus is not None:

```python
students = [
    {"name": "Hermione", "house":"Griffindor", "patronus": "Otter"},
    {"name":"Harry", "house":"Griffindor", "patronus": "Stag"},
    {"name":"Ron", "house":"Griffindor","patronus": "Jack Russell terrier"},
    {"name":"Draco", "house": "Slytherin", "patronus": None}
]
```

### SET 4: Patterns and Repetition (Mario/Shapes)
1. Modify the print_square(size) function to print a rectangle with 3 rows and 6 columns.

2. Write a function print_triangle(height) that prints a right-angled triangle like this:

```shell
#
##
###
####
```

3. Given this function:

```python
def print_row(width):
    print("#" * width)
```

Create a new function print_rectangle(rows, cols) that uses print_row to print a rectangle of size rows by cols.