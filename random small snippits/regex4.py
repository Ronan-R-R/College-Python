import re

pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

#\b: a word boundary, ensures that the pattern macthes a complete sentence
#\d{3}: three digits
#[-.]?: an optional of dash(-) or period(.)

#Define the string to search 
string1 = "my phone number is 123-456-7890."
string2 = "call me at (011) 555-5555"
string3 = "my number is 123-4567 not 123-456-7890"
string4 = "number is 011.000.1000."

#search for the matches using the patterns
match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)
match4 = re.search(pattern, string4)

#check if there is a match
if match1:
    print(f'Match found in string 1: {match1.group(0)}')
if match2:
    print(f'Match found in string 2: {match2.group(0)}')
if match3:
    print(f'Match found in string 3: {match3.group(0)}')
if match4:
    print(f'Match found in string 4: {match4.group(0)}')