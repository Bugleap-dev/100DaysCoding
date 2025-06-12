# DAY 9 - 22/05/2025
# CS50P: Introduction To Programming with Python

# EXERCISES:

## 1: Number Comparison

def main():
    x = int(input("Firdt number(x): "))
    y = int(input("Second number(y): "))
    z = int(input("Third number(z): "))

    result = compare(x,y,z)
    print(result)


def compare(a,b,c):
    if a > b and a > c:
        return "x is the greatest"
    elif b > a and b > c:
        return "y is the greatest"
    elif c > a and c > b:
        return "z is the greatest"
    else:
        return "There is a tie"
main()

### 2: Grade Evaluator

def main():
    result = int(input("What's the score?: "))
    graded_result = grade(result)

    print(graded_result)

def grade(num):
    if num >= 90:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 70:
        return "C"
    elif num >= 60:
        return "D"
    else:
        return "F"


main()

### 3: Even, Odd or Zero

def main():
    num = int(input("What's the number: "))
    result = check_number(num)

    print(result)

def check_number(n):
    if n == 0:
        return "Zero"
    elif n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
main()

### 4: Hogwarts House

def main():
    name = input("Enter name: ")
    match name.title():
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case "Cedric":
            print("Hufflepuff")
        case _:
            print("Unknown House")


main()


## 5: Divisibility Checker

def main():
    num = int(input("Enter your number: "))
    result = divisible(num)

    print(result)

def divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Divisible by 3 and 5"
    elif num % 3 == 0:
        return "Divisible by 3"
    elif num % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 3 or 5"

        
main()