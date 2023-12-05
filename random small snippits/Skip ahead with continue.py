while True:
        value = input("String to capitalize [type q to quite]: ")
        if value == "q": #quit
            break
        number = int(value) #local variable
        if number % 2 == 0: #an even number
              continue
        print(number, "squared is", number * number)