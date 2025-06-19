# DAY 17 - 30/05/2025

# CS50P: Introduction To Programming with Python

# EXERCISE

## SET 1: Loops & Flow Control (while & for)

# 1. Modify this code to make it print "hello" 5 times instead of "meow" 3 times:

for _ in range(5):
    print("hello")

# 2. Rewrite this while loop as a for loop:

i = 2

for _ in range(i):
    print("meow")

# 3.

while True:
    n = int(input("how many times?: "))
    if n > 0:
        break

for _ in range(n):
    print("CS50P!")

## SET 2: Functions & Input Handling

# 1. Write a function called laugh(n) that prints "ha" n times, where n is input by the user and must be a positive integer. Use a helper function to validate the input.

def laugh():
    
    num = positive_integer()

    for _ in range(num):
        print("Ha")

def positive_integer():
    while True:
        n = int(input("how many times?: "))
        if n > 0:
            return n
        
laugh()

# 2. In the code below, the validation inside meow() is redundant. Refactor it to keep validation only in main():

def main():
    while True:
        num = int(input("what's n? "))
        if num > 0:
            break
    meow(num)

def meow(n):
    for _ in range(n):
        print("meow")
    
main()

# 3. Modify the star(n) function below to print a right-angled triangle of *, including the last row:

def star():
    while True:
        num = int(input("how many lines: "))
        if num > 0:
            break

    one = 1
    while num >= one:
        print("*"*one)
        one +=1


star()