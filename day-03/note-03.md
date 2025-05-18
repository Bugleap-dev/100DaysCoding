# **DAY 03 - 16/05/2025**

**CS50P: Introduction To Programming with Python**

# PSET 0
![Pset0](pset.png)

LINK: [https://cs50.harvard.edu/python/2022/psets/0/](https://cs50.harvard.edu/python/2022/psets/0/)


## 1. Indoor Voice
link: [https://cs50.harvard.edu/python/2022/psets/0/indoor/](https://cs50.harvard.edu/python/2022/psets/0/indoor/)

In a file called **indoor.py**, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a **str** of your own as an argument to **input**.

Hints:
 - Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](docs.python.org/3/library/functions.html#input).
 - Recall that a str comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](docs.python.org/3/library/stdtypes.html#string-methods).

## 2. Playback Speed
link: [https://cs50.harvard.edu/python/2022/psets/0/playback/](https://cs50.harvard.edu/python/2022/psets/0/playback/)

In a file called **playback.py**, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with **...** (i.e., three periods).

Hints:
 - Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](docs.python.org/3/library/functions.html#input).
 - Recall that a str comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](docs.python.org/3/library/stdtypes.html#string-methods).

## 3. Making Faces:
link: [https://cs50.harvard.edu/python/2022/psets/0/faces/](https://cs50.harvard.edu/python/2022/psets/0/faces/)

In a file called **faces.py**, implement a function called **convert** that accepts a **str** as input and returns that same input with any **:)** converted to 🙂 (otherwise known as a slightly smiling face) and any **:(** converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called **main** that prompts the user for input, calls **convert** on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a **str** of your own as an argument to **input**. Be sure to call main at the bottom of your file.

Hints:
 - Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](docs.python.org/3/library/functions.html#input).
 - Recall that a str comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](docs.python.org/3/library/stdtypes.html#string-methods).
 - An emoji is actually just a character, so you can quote it like any **str**, a la "😐". And you can copy and paste the emoji from this page into your own code as needed.

## 4. Einstein:
link: [https://cs50.harvard.edu/python/2022/psets/0/einstein/](https://cs50.harvard.edu/python/2022/psets/0/einstein/)

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

Hints:
 - Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](docs.python.org/3/library/functions.html#input).
 - Recall that int can convert a str to an int, per [docs.python.org/3/library/functions.html#int](docs.python.org/3/library/functions.html#int).
 - Recall that Python comes with several built-in functions, per [docs.python.org/3/library/functions.html](docs.python.org/3/library/functions.html).

## 5. Tip Calculator
link: [https://cs50.harvard.edu/python/2022/psets/0/tip/](https://cs50.harvard.edu/python/2022/psets/0/tip/)

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Hints
 - Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](docs.python.org/3/library/functions.html#input).
 - Recall that float can convert a str to a float, per [docs.python.org/3/library/functions.html#float](docs.python.org/3/library/functions.html#float).
 - Recall that a str comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](docs.python.org/3/library/stdtypes.html#string-methods).