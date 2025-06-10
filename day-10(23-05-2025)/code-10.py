# DAY 10 - 23/05/2025
# CS50P: Introduction To Programming with Python

# CONTINUATION OF LECTURE 1 - LOOPS

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break                       #OR YOU CAN USE:    retun n
    return n                            #BECAUSE RETURN CAN BE USED TO BREAK OUT OF A LOOP AND END A FUNCITON

def meow(n):
    for _ in range(n):
        print("meow")


main()

#####

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()

####################

students = ["Hermione", "Ron","Harry"]

print(students)
print(students[0])
print(students[1])
print(students[2])
"""
Output:
['Hermione', 'Ron', 'Harry']
Hermione
Ron
Harry
"""

##################
students = ["Hermione", "Ron","Harry"]

for student in students:
    print(student)

"""
Output:
Hermione
Ron
Harry
"""
#############

students = ["Hermione", "Ron","Harry"]

for i in range(len(students)):
    print(str(i+1)+". ", students[i])

""" Output:

1.  Hermione
2.  Ron
3.  Harry

"""

################
