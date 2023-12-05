import re

pattern = r'\b[A-Za-z0-9._%+-]+@ctucareer\.co\.za\b'

#\b: a word boundary, ensures that the pattern macthes a complete sentence
#\d{3}: three digits
#[-.]?: an optional of dash(-) or period(.)

#Define the string to search 
string1 = "my email address is john@ctucareer.co.za"
string2 = "email is jane.doe@ctucareer.co.za"
string3 = "my email jojo@gmail.com"
string4 = "email is jojo2003@ctucareer.co.za"

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