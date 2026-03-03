def main():
    name = input("What's your name?")

    try:
        age = int(input("How old are you?"))
    except ValueError:
        print("Please enter a valid integer for age.")
        return

    print(f"Your name is {name}")
    print(f"Your age is {age}")
    
    print(f"In 20 years you will be {age + 20}")

