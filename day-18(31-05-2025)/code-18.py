# DAY 18 - 31/05/2025

# CS50P: Introduction To Programming with Python

# EXERCISE

## SET 3: Lists & Dictionaries

## 1. Add "Luna" to the list below and print each student on a new line with their number (e.g., 1. Hermione, ...):

students = ["Hermione", "Ron", "Harry"]

students.append("Luna")

for student in range(len(students)):
    print(student + 1,".",students[student])

## 2. Using a for loop, print only the names of students from this dictionary who belong to "Griffindor":
students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}

for student in students:
    if students[student] == "Griffindor":
        print(student)

# SET 4

## 1. Modify the print_square(size) function to print a rectangle with 3 rows and 6 columns.

def main():
    while True:
        x =int(input("heigth: "))
        y =int(input("length: "))

        if x > 0 and y > 0:
            break
    
    rectangle(x,y)
    
def rectangle(x,y):

    for i in range(x):
        print("#" * y)

main()


# 2. Write a function print_triangle(height) that prints a right-angled triangle like this:

def main():
    while True:
        num = int(input("numbers of row: "))
        if num > 0:
            break
    
    print_triangle(num)

def print_triangle(row):

    one = 1

    while row >= one:
        print("#"*one)
        one +=1
    
main()

# 3. 

def print_rectangle():

    while True:
        rows = int(input("rows: "))
        cols = int(input("columns: "))

        if rows and cols > 0:
            break

    print_row(rows,cols)

def print_row(x,y):
    for _ in range(x):
        print("#" * y)


print_rectangle()
