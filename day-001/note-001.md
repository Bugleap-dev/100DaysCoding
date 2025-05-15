# **DAY 001 - 15/04/2025**

# **CS50P: Introduction To Programming with Python**
    
# **LECTURE 0: Function_Variable**

## Table of Contents
1. [Definition](#Definition)
2. [Parameters](#parameters)
3. [Difference between Arguments and Parameters](#differnce-between-arguments-and-parameters)
4. [Differnce between using Comma and plus for Concatenation](#differnce-between-using-comma-and-plus--for-concatenation)
5. [String](#string)
6. [Integer and float](#integer-and-float)
7. [Python Interactive mode](#python-interactive-mode)
8. [Round function](#round-function)
   - [Round half or Banker's rounding](#round-half)
9. [Def function](#-def-function)
10. [Return](#return-statement)
11. [Return VS Print Function](#return-vs-print)

---
# Definition
- **$code hello.py**: Creates a file "hello" in python(py) format

- **Syntax**: refers to the sedof rules that defines hoe code must be written for the computer to understand it, i.e Syntax = the rules for writing code correctly.

- **$python hello.py**: runs the python code "hello.py"

- **Function** : is an action or a verb that lets you do something in the program.

- **Arguments**: is an input to a function that influences its behaviour.

- **Side Effects**: is the display of a function, it could be visual, audio, etc.

- **Bugs**: is a mistake in a program.

- **Return values**: is the result that a function gives back after execution.

- **Variable**: is a placeholder for information you want python to recall later in the coding process when you need to complete an action.

- **Comments**: are notes in a code, it is written with an **Hash(#)** at the beginning or three quotation marks at the beginning and end for multiple lines (" " ").

- **Pseudo-code**: is plain English, half code outline describing a program's logic, serving as a blueprint before writing actual code, using the **Hash (#)** for comments.

## **Parameters**
- Parameters: are variables used in function definitions to accept input values when the function is called.

- * Name parameter: parameters that must be passed in the correct order.
- * Position parameter: parameters with default values, used if no argument is provided.

### ***DIFFERNCE BETWEEN ARGUMENTS AND PARAMETERS***
   * Parameters acts a placeholder for the values that will be passed.
   * While Arguments are actual values passed to the function when you call it.

- **Concatenation**: the process of joining two or more string into a new string. This is done using operators the ***plus operator (+).***

### ***DIFFERNCE BETWEEN USING COMMA(,) AND PLUS (+) FOR CONCATENATION***
   * Using + (Concatenation Operator): joins strings together with no space. Both operands must be string.
   * Using , (concatenation operator): Automatically adds a space between items. Can mix data types(e.g string and int without conversion).

**FROM PYTHON DOCUMENATION:**
- *docs.python.org/3/library/functions.html*
    - Print() Syntax: 
    ```python
    print(*objects,sep=' ',end='\n',file=sys.stdout,flush=False)
    ```

 - * *objects : the values to be printed. Can be multiple items.
    - * sep='' : seperator between the objects(default is a space).
    - * end=\n : what to print at the end(default is newline).

- **\n** is the *newline character*. It tells the program to move the cursor to the next line when printing text. *\n* = "linebreak"

- * **USING QUOTATION MARKS INSIDE PRINT() FUNCTION**
    - * Using Escape character(\n)
    - * Using Different quotation mark, single quotation(''), double quotation, (""), triple quoatation("' '")

- **F-string**: is a way to make strings that include variables or expressions directly inside them by putting an **f** before the string and using {} to insert values.

## **STRING**
* String is a sequence of characters, enclosed in single (''), double ("") and triple ('""')quotes.

-  * **STRING FUNCTION**: is any function that works with strings -either built in functions like len(),or methods like uppper().
   - * len(): returns the length of a sting.
   - * str(): converts other data types into string.
   - * type(): tells you the data type.

- * **STRING METHODS**:is a built-in function in python that you can use with strings to perform specific tasks like changing text, finding things or formatting. **Method** is a function that is associated with an object. **Functions** are independent and can work on different types of data, while methods are attached to objects and work only on that specific type.

   - * .strip(): is used to remove leading and trailing whitespaces from a string. 
      - * .lstrip(): removes left space only.
      - * .rstrip(): removes right space only.
   - * capitalize(): convert the first character of a string and the rest to lowercases.
   - * .title(): capitalizes the first letter of each word in a string while converting the rest to lowercase. 
   - * .split(): is used to split a string into a list based in a separator(like a space or comma)

## **INTEGER AND FLOAT**
- Integers are whole numbers without a decimal point, e.g, 1, -5, 100, 0, etc.
- Float are numbers with a decimal point or in exponential form, properly called a floating point value, e.g, 3.14, -0.5, 2.0, 1e3,3e5,etc.

- * Arithmetic operators:
   - * **Addition (+)**: adds two values.
   - * **Sutraction(-)**:subtracts the right operand from the left.
   - * **Multiplication(*)**: multiplies teo values.
   - * **Division(/)**: divides and return a float.
   - * **Floor(//)**: divides and retuen the integer part (floor) of the result.
   - * **Modulus(%)**: returns the remainder of the division.

```python
>>> 1+2
3
>>> 5-1
4
>>> 5*2
10
>>> 1+2
3
>>> 5-1
4
>>> 5*2
10
>>> 7/2
3.5
>>> 9//5
1
>>> 7%5
2
```
### **PYTHON INTERACTIVE MODE**
- Python interactive mode is a way to run Python commands one at a time and get immediate feedback. It's super useful for testing small pieces of code, exploring libraries, or doing quick calculations.
- * How to Access Interactive Mode:
   - * From the Terminal/Command Line,
   - Just type *python* or *python3* (depending on your system).
- * To Exit Interactive mode:
   - * Press ***Ctrl + Z***

### **ROUND() FUNCTION**:
- - Round() Function in python is used to round a number to the nearest integer or to a specified number if decimal places.
- - Syntax:
   ```python
      round(number[,ndigits])
   ```
   - * number: The number you want to round.
   - * ndigits: number of decimal places to round to.
      - - if omitted, it rounds to the nearest **whole number**.
      - - if given, it rounds to that many decimal places.

### Round Half():
   Python uses a rule called ***ROUND HALF TO EVEN***, ALSO KNOWN AS ***BANKER'S ROUNDING*** If a number is exactly halfway between two integers (like -2.5 is between -2 and -3 ), ***python will round to the nearest even number.***

### * **DEF FUNCTION:**
   - * def is used to define a function.

### **RETURN statement:**
   - * return statement is used in a function to send a value back to the caller. It ends the function and returns the apecified value.
   - * reurn statement syntax:
   ```python
         def function():
             return value
   ```

### ***Return VS Print***
   - * ***return*** sends data to caller, while ***print*** just shows data to the screen.
   - * ***return*** is used in calculation and logic, whereas ***print*** is used for debugging and displaying,
   - * ***return*** function output is usable, while ***print*** output is not usable in code
