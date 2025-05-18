#DAY 003 - 16/05/2025
#CS50P: Introduction To Programming with Python

# PSET 0

# 1. Indoor:

def main():
    message = input("")
    print(message.lower())


main()

# 2. Playback Speed:

def space():
    text = input("Enter your text: ")
    print(text.replace(" ", "..."))

space()

# 3. Making Faces:

# prompts the user for inputs
def main():
    message = input("")
    print(convert(message))


# converts user's input to emoticons
def convert(emoticon):
    return emoticon.replace(":)", "🙂").replace(":(","🙁")


main()

# 4. Einstein:

def main():
    m = int(input("m: "))
    c = pow(300000000,2)
    E = int(m * c)
    print(f"E: {E}")


main()

# 5. Tip Calculator:

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    return float(dollars.replace("$", ""))  # Removed the space

def percent_to_float(percent):
    return float(percent.replace("%", "")) / 100  # Convert to decimal

main()
