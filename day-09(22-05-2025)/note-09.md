# **DAY 9 - 22/05/2025**

**CS50P: Introduction To Programming with Python**

## LECTURE 1 - LOOPS

## Table of Contents
1. [While Loops](#while-loops)
2. [For Loops](#for-loops)
3. [Loop Input Validation](#loop-input-validation)
4. [Function Design with Loops](#function-design-with-loops)
5. [Custom Loop Patterns](#custom-loop-patterns)

---

### While Loops
`while` loops allow repeated execution of a block of code as long as a condition is true.

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```
Shorthand using -=:

```python
i = 3
while i != 0:
    print("meow")
    i -= 1
```
Alternative style:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```
---

## For Loops:
A for loop iterates over a sequence or range.

```python
for i in range(3):
    print("meow")
```

If the loop variable isn't needed, use _:
```python
for _ in range(3):
    print("meow")
```

String multiplication:
```python
print("meow\n" * 3, end="")
```
---

## Loop Input Validation

Using while True to repeatedly prompt user input until a valid condition is met:
```python
while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
    print(_)
```

---

## Function Design with Loops
Using functions to organize input validation and looping logic:
```python
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

Improved with a dedicated input function:
```py
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break        # OR just: return n
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
```
---

## Custom Loop Patterns
Using nested loops and counters for patterns:
```py
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

