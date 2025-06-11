# DAY 6 - 19/05/2025
# CS50P: Introduction To Programming with Python

# CONTINUATION OF LECTURE 1 -CONDITIONALS

x = int(input("What's x? "))
y = int(input("What's y? "))

if x!=y:
    print("x is not equal to y")
else:
    print("X is equal to y")

######

x = int(input("What's x?: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#####

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
main()

#####

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")        


def is_even(n):
    return True if n % 2 == 0 else False

main()

