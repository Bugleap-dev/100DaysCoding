vowels = ["a", "e", "i", "o", "u"]

user_input = input("Input: ")

for vowels in user_input.lower():
    print(user_input.replace(vowels, ""),end="")