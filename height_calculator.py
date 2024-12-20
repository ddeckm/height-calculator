while True:
    print("---Lets calculate you height in inches---")
    while True:
        try:
            feet = int(input("Enter your height in feet: "))
            if feet < 0:
                print("!!! Height must be poitive !!!")
            else:
                break
        except ValueError:
            print("!!! Invalid input please enter a positive whole number !!!")
    while True:
        try:
            inches = int(input("And inches: "))
            if inches < 0:
                print("!!! Height must be positve !!!")
            else:
                break
        except ValueError:
            print("!!! Please enter a positive whole number !!!")
    print(f"Your height in inches is: {(feet * 12)+inches}")
    if input("Would you like me to calculate your height in inches again? (Y/N): ").lower() != "y":
        break
