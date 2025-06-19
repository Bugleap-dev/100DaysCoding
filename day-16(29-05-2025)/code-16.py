# DAY 16 - 29/05/2025

# CS50P: Introduction To Programming with Python

# CONTINUATION OF LECTURE 2 - LOOPS

def main():
    print_column(3)

def print_column(height):
    print("#\n" * height,end="")

main()

"""
Output:

#
#
#

"""

############

def main():
    print_row(4)

def print_row(width):
    print("#"*width)


main()
"""
Output:

####

"""

#############

def main():
    print_square(4)

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):
            print("#", end="")
            
        print()    


main()

"""
Output:

####
####
####
####

"""

################

def main():
    print_square(4)


def print_square(size):
    for i in range(size):
        print("#"*size)


main()

"""
Output:

####
####
####
####

"""

################

def main():
    print_square(4)


def print_column(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#"*width)
main()

"""
Output:

####
####
####
####

"""

