# **DAY 17 - 30/05/2025**

# **CS50P: Introduction To Programming with Python**

# EXERCISE

Exercise generated with chatgpt:

### SET 1: Loops & Flow Control (while & for)

1. Modify this code to make it print "hello" 5 times instead of "meow" 3 times:

```py
i = 3
while i != 0:
    print("meow")
    i -= 1

```
2. Rewrite this while loop as a for loop:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```
3. Create a program that keeps asking the user to enter a number n, and prints "CS50P!" n times only if n is a positive number, otherwise keeps asking.

### SET 2: Functions & Input Handling

1. Write a function called laugh(n) that prints "ha" n times, where n is input by the user and must be a positive integer. Use a helper function to validate the input.

2. In the code below, the validation inside meow() is redundant. Refactor it to keep validation only in main():

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

3. Modify the star(n) function below to print a right-angled triangle of *, including the last row:

```python
def star(n):
    one = 1
    while n > one:
        print("*"*one)
        one +=1
```