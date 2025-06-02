# DAY 10 - 23/05/2025
# CS50P: Introduction To Programming with Python

# CONTINUATION OF LECTURE 1 - LOOPS

students = ["Hermione", "Ron","Harry"]

for student in students:
    print(student)

"""Output:
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

#dict:

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
    }

print(students["Ron"])          #Output: "Griffindor"

for student in students:
    print(student)

"""
Output:

Hermione
Harry
Ron
Draco

"""

for student in students:
    print(student, students[student],sep = ", ")

"""
Output:

Hermione, Griffindor
Harry, Griffindor
Ron, Griffindor
Draco, Slytherin

"""

############

#USING DICTIONARY IN LIST
students = [

    {"name": "Hermione", "house":"Griffindor", "patronus": "Otter"},
    {"name":"Harry", "house":"Griffindor", "patronus": "Stag"},
    {"name":"Ron", "house":"Griffindor","patronus": "Jack Russell terrier"},
    {"name":"Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"],sep = ", ")

"""
Output:

Hermione, Griffindor, Otter
Harry, Griffindor, Stag
Ron, Griffindor, Jack Russell terrier
Draco, Slytherin, None

"""

##############

# Mario:

def main():
    print_column(3)

def print_column(height):
    for i in range(height):
        print("#")


main()

"""
Output:

###
###
###

"""
