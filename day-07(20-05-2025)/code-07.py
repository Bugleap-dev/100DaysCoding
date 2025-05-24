# **DAY 07 - 20/05/2025**

# **CS50P: Introduction To Programming with Python**

# PSET 1

# 1. [Deep Thought](#1-deep-thought)


def main():
    response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    deep = forty_two(response)
    print(deep)

def forty_two(num):
    match num:
        case "42"|"forty two"|"forty-two":
            return "Yes"
        case _:
            return "No"
        
main()

# 2. [Home Federal Saving Bank](#2-home-federal-savings-bank)


def main():
    greet = input("Greeting: ")
    greeting = hello(greet)
    print(greeting)


def hello(response):
    response_lower = response.lower().strip()
    if "hello" in response_lower:
        return "$0"
    elif response_lower[0] == "h":
        return "$20"
    else:
        return "$100"

main()

