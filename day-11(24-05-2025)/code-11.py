# PSET 1
# 1. File Extensions

def main():
    file_name = input("File name: ")
    file = sort(file_name)
    print(file, end='\n')

def sort(type):
    type_lower = type.lower().strip()
    if type_lower.endswith(".jpg") or type_lower.endswith(".jpeg"):
        return "image/jpeg"
    elif type_lower.endswith(".gif"):
        return "image/gif"
    elif type_lower.endswith(".png"):
        return "image/png"
    elif type_lower.endswith(".mp3"):
        return "audio/mpeg"
    elif type_lower.endswith(".mp4"):
        return "video/mp4"
    elif type_lower.endswith(".pdf"):
        return "application/pdf"
    elif type_lower.endswith(".txt"):
        return "text/plain"
    elif type_lower.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()


###########################

# 2. Math Interpreter

def main():
    prompt = input("Expression: ")
    x , y , z = prompt.split(" ")
    final_answer = calculate(x,y,z)
    print(final_answer)


def calculate(num1,num2,num3):
    float_num1 = float(num1)
    float_num3 = float(num3)

    if num2 == "+":
        return float_num1 + float_num3
    elif num2 == "-":
        return float_num1 - float_num3
    elif num2 == "*":
        return float_num1 * float_num3
    elif num2 == "/":
        return float_num1 / float_num3
    elif num2 == "/" and float_num3 == 0:
        return "Error: Division by zero"
    else:
        return "Unsupported Operation"


main()

##########################

# 3. Meal Time

def main():
    time = input("What time is it? ")
    time_in_hours = convert(time)

    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes_convert = float(minutes) / 60
    hours_float = float(hours) + minutes_convert
    return hours_float

if __name__ == "__main__":
    main()

