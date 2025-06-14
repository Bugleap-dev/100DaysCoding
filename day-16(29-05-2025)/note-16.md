# **DAY 16 - 29/05/2025**

# **CS50P: Introduction To Programming with Python**

# #Lecture 2 – Loops (Continued): Practice with Patterns

## Table of Contents
1. [Printing Columns](#1-printing-columns)

2. [Printing Rows](#2-printing-rows)

3. [Nested Loops for Grids and Squares](#3-nested-loops-for-grids-and-squares)

4. [Function Decomposition](#4-function-decomposition)

5. [Output Comparisons](#5-output-comparisons)

### 1. Printing Columns
Using "\n" to repeat a vertical column of #:

```python
def print_column(height):
    print("#\n" * height, end="")

# Output:

#
#
#

```
### 2. Printing Rows
A single horizontal row:

```python
def print_row(width):
    print("#" * width)

# Output:

####
```
### 3. Nested Loops for Grids and Squares
Using nested for loops to print a square:

```python
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
```

Or, using string multiplication instead of an inner loop:

```python
def print_square(size):
    for i in range(size):
        print("#" * size)

# Both versions produce the same output:

# Output:

####
####
####
####
```

### 4. Function Decomposition
Breaking the pattern printing into smaller functions:

```python
def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
```    
This approach demonstrates modular programming, improving readability and reusability.

### 5. Output Comparisons
Function Call	Output

```py
print_column(3)	#\n#\n#\n
print_row(4)	####
print_square(4)	####\n####...
```

Nested Functions	Same square pattern