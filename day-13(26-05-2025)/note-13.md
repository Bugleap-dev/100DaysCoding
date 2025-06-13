# **DAY 13 - 26/05/2025**

# **CS50P: Introduction To Programming with Python**

Lecture 2 – Loops
📘 Table of Contents
While Loop

While Loop with Condition Variants

For Loop with range()

String Multiplication

Input Validation Loop

Function with Loop Logic

Star Pattern Using While Loop

1. While Loop
Repeats a block of code while a condition is True.

python
Copy
Edit
i = 3
while i != 0:
    print("meow")
    i = i - 1
2. While Loop with Condition Variants
Shorthand assignment (i -= 1) and alternate condition (i < 3).

python
Copy
Edit
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
3. For Loop with range()
The for loop provides a clean way to repeat actions a set number of times.

python
Copy
Edit
# Using index variable
for i in range(3):
    print("meow")

# Ignoring index with underscore
for _ in range(3):
    print("meow")
4. String Multiplication
Repeating a string multiple times using *.

python
Copy
Edit
print("meow\n" * 3, end="")
5. Input Validation Loop
Ensures the user inputs a positive number.

python
Copy
Edit
while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
    print(_)
6. Function with Loop Logic
Encapsulating the meow logic in a function.

python
Copy
Edit
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
7. Star Pattern Using While Loop
Prints an increasing star (*) pattern:

python-repl
Copy
Edit
*
**
***
...
python
Copy
Edit
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