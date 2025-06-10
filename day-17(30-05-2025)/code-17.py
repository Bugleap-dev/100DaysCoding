#SHORTS: FOR LOOP

def main():
    names = ["Mario", "Luigi", "Yoshi"]
    for guests in names:
        print(write_letter(guests, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    |-----------------------------------------------|    
        Dear {receiver},
        You are cordially invited to a ball at 
        Peach's castle this evening, 7:00 PM.

        Sincerlely,
        {sender}
    |-----------------------------------------------|
    """

main()

##########################

def main():
    names = ["Mario", "Luigi", "Yoshi"]
    for i in range(len(names)):
        print(write_letter(names[i], "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    |-----------------------------------------------|    
        Dear {receiver},
        You are cordially invited to a ball at 
        Peach's castle this evening, 7:00 PM.

        Sincerlely,
        {sender}
    |-----------------------------------------------|
    """

main()