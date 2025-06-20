# DAY 13 - 26/05/2025

# CS50P: Introduction To Programming with Python

# LECTURE 2 - LOOPS

i = 3
while i != 0:
    print("meow")
    i = i-1

#####

i = 3
while i != 0:
    print("meow")
    i -= 1              ##PYTHON SHORTHAND FOR (i = i - 1)

#####

i = 0
while i < 3:
    print("meow")
    i += 1              ##PYTHON SHORTHAND FOR (i = i + 1)

#####

#for loop:
for i in range(3):
    print("meow")

#####

for _ in range(3):
    print("meow")

#####

print("meow\n"*3,end="")

###

while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
    print(_)

#####

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

#####

def main():
    n = int(input("number of rows: "))
    star(n)
    
def star(n):
    while True:
        if n > 0:
            break
    
    one = 1
    while n > one:
        print("*"*one)
        one +=1
main()

#####
