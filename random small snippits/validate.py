import re

while True: 
    email = input("enter your email address: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        break
    else:
        print("Invalid email, enter a valid email")