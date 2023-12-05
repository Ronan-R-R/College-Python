def doublenumber(number):
    return number * 2
def squarenumber(number):
     return number **2
def SQRT(number):
     return number ** 0.5


user_input = input("please enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print(f"The Number you entered is {number}.")
    print("What do you want to do?")
    print("1. double the number the number")
    print("2. square the number the number")
    print("3. take a SQRT the number the number")

    mychoice=input("Please enter choice(1,2,3)")
    if mychoice == "1":
        result = doublenumber(number)
        print(f"The {number} doubled is {result}.")
    elif mychoice == "2":
        result = squarenumber(number)
        print(f"The {number} squared is {result}.")
    elif mychoice == "3":
        result = SQRT(number)
        print(f"The {number} SQRT is {result}.")
    else:
        print ("invalid code")
else:
        print("invalid input, please enter a number")