# **DAY 02 - 15/05/2025**

**CS50P: Introduction To Programming with Python**

## Table of Contents
1. [Shorts](#shorts)
2. [Exercises](#exercises)
    - [Print basics](#-1-print-basics)
    - [Input basics](#-2-input--output)
    - [String methods](#-3-string-methods)
    - [Integer and flaot](#-4-integer-and-float)
    - [Round function](#-5-round-function)
    - [Defining functions](#-6-defining-functions)
    - [Return vs print](#-7-return-vs-print)
    - [Bonus Challenge](#-8-bonus-challenge)

---

## **SHORTS**
- **Visual Studio Code for CS50**
- * List of visual studio command lines.
    - * *ls* - list all files in current directory.
    - * *cp* - copy from one directory to another.
    - * *mv* - move file from one directory to another.
    - * *rm* - delete a file.
    - * *mkdir* - make a directory or folder.
    - * *cd* - change directory from one directory to another.
    - * *rmdir* - remove or delete a directory.
    - * *clear* - clear terminal (OR You can press **Ctrl + L**)


## EXERCISES:
These exercises are based on the concepts covered in **Lecture 0: Function & Variable**.

---

## 🔹 1. Print Basics
**a. Print with Comma and Plus**  
Write a program that prints the following using both `,` and `+`:

Hello World!
Hello-World!
Hello World!

**b. Newline Character**  
Print the following using one `print()` and `\n`:
Hello
CS50P
Python

## 🔹 2. Input & Output
**a. Greeting with F-string**
Ask for the user's name and greet them:
Hello, <name>!

**b. String Length**  
Ask the user to enter a word and print the number of characters in it using `len()`.

## 🔹 3. String Methods
**a. Capitalize and Title**  
Ask the user for a name (e.g., "joHN doe") and print it:
- With `.capitalize()`
- With `.title()`

**b. Whitespace Trimming**  
Ask for a name with spaces and show the output using:
- `.lstrip()`
- `.rstrip()`
- `.strip()`

## 🔹 4. Integer and Float
**a. Simple Calculator**  
Ask for two integers and print:
- Their sum
- Their product
- The remainder (using `%`)

**b. Float Addition with Rounding**  
Ask for two float numbers and:
- Print the sum
- Print the sum rounded to 1, 2, and 3 decimal places

## 🔹 5. Round Function

**a. Banker's Rounding Check**  
Use `round()` to check and print the result of:
round(2.5)
round(3.5)
round(-2.5)
round(-3.5)

## 🔹 6. Defining Functions
**a. Hello Function**
Define a function hello(name="World") that prints Hello, <name>.
Test it with and without an argument.

**b. Split Full Name**
Ask the user for their full name. Use .split() to separate first and last names and print each on a separate line.

## 🔹 7. Return vs Print
**a. Add Function with Return**
Create a function add(a, b) that returns the sum.
Get two numbers from the user and print the result.

**b. Square Function**
Write a function square(n) that returns n ** 2.
Prompt the user and print the squared value.

# 🔹 8. Bonus Challenge
**a. Formatted Division Output**
Ask for two floats a and b, compute a / b, and show the result formatted to:

 - 1 decimal place

 - 2 decimal places

 - 3 decimal places

15. Tip Calculator
Ask the user:

 - Total bill amount

 - Tip percentage

    Calculate and print the final amount with tip included (rounded to 2 decimal places).