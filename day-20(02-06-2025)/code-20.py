# SHORT: DICTIONARY METHODS

WORDS = {
    "HAIR": 4,
    "CHAIR": 5,
    "PAIR": 4
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word: ")

        if guess.upper() == "HAIR":
            print(f"{WORDS["HAIR"]} points")
            WORDS.pop("HAIR")
        
        if guess.upper() == "CHAIR":
            print(f"{WORDS["CHAIR"]} points")
            WORDS.pop("CHAIR")

        if guess.upper() == "PAIR":
            print(f"{WORDS["PAIR"]} points")
            WORDS.pop("PAIR")
        
        
    print("That's the game!")
    print("Total point: 13")


    
main()

####
WORDS = {
    "HAIR": 4,
    "CHAIR": 5,
    "PAIR": 4,
    "GRAPHIC": 7
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word: ")
        guess_upper = guess.upper()

        if guess_upper in WORDS:
            print(f"{WORDS[guess_upper]} points")
            if guess_upper == "GRAPHIC":
                print("You've won")
                WORDS.clear()
            else:
                WORDS.pop(guess_upper)
        else:
            print("Incorrect or already used word.")

    print("That's the game!")

main()

######

WORDS = {
    "HAIR": 4,
    "CHAIR": 5,
    "PAIR": 4,
    "GRAPHIC": 7
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    for word in WORDS:
        print(f"{word} is worth {WORDS[word]}")
main()

######

WORDS = {
    "HAIR": 4,
    "CHAIR": 5,
    "PAIR": 4,
    "GRAPHIC": 7
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    for word, points in WORDS.items():
        print(f"{word} was worth {points}")
main()

