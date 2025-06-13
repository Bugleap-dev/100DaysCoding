# **DAY 13 - 26/05/2025**

# **CS50P: Introduction To Programming with Python**

## Lecture 2 – Loops

## Table of Contents
1. [While Loop](#1-while-loop)

2. [While Loop with Condition Variants](#2-while-loop-with-condition-variants)

3. [For Loop with range()](#3-for-loop-with-range)

4. [String Multiplication](#4-string-multiplication)

5. [Input Validation Loop](#5-input-validation-loop)

6. [Function with Loop Logic](#6-function-with-loop-logic)

7. [Star Pattern Using While Loop](#7-star-pattern-using-while-loop)

### 1. While Loop
Repeats a block of code while a condition is True.

```py
i = 3
while i != 0:
    print("meow")
    i = i - 1
```

### 2. While Loop with Condition Variants
Shorthand assignment (i -= 1) and alternate condition (i < 3).

```py
# Using shorthand
i = 3
while i != 0:
    print("meow")
    i -= 1

# Counting up
i = 0
while i < 3:
    print("meow")
    i += 1
```

### 3. For Loop with range()
The for loop provides a clean way to repeat actions a set number of times.

```py
# Using index variable
for i in range(3):
    print("meow")

# Ignoring index with underscore
for _ in range(3):
    print("meow")
```

### 4. String Multiplication
Repeating a string multiple times using *.

```py
print("meow\n" * 3, end="")
```

### 5. Input Validation Loop
Ensures the user inputs a positive number.

```py
while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
    print(_)
```

### 6. Function with Loop Logic
Encapsulating the meow logic in a function.

```py
def main():
    num = int(input("what's n? "))
    meow(num)

def meow(n):
    while True:
        if n > 0:
            break
    for _ in range(n):
        print("meow")

main()
```

### 7. Star Pattern Using While Loop
Prints an increasing star (*) pattern:

```py
*
**
***
...

def main():
    n = int(input("number of rows: "))
    star(n)

def star(n):
    while True:
        if n > 0:
            break

    one = 1
    while n > one:
        print("*" * one)
        one += 1

main()
```