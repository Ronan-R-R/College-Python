#prompt user imput

user_input = input("please enter a number: ")

# Present a choice based on the input

if user_input.isdigit():
    number = int(user_input)
    print(f"The Number you entered is {number}.")
    print("What do you want to do?")
    print("1. double the number the number")
    print("2. square the number the number")
    print("3. take a SQRT the number the number")

    mychoice=input("Please enter choice(1,2,3)")
    if mychoice == "1":
        doublenumber= number * 2
        print(f"The {number} doubled is {doublenumber}.")
    elif mychoice == "2":
        squarenumber= number ** 2
        print(f"The {number} squared is {squarenumber}.")
    elif mychoice == "3":
        SQRT= number ** 0.5
        print(f"The {number} SQRT is {SQRT}.")
    else:
        print ("invalid code")
else:
        print("invalid input, please enter a number")