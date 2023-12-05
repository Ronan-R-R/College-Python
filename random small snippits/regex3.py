import re

#define the regex pattern

pattern = r'ab*c'
#match A, zero or more Bs and C

#Define the string to search 
string1 = "ac"
string2 = "abc"
string3 = "abbbbbc"
string4 = "ab"

#search for the matches using the patterns

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)
match4 = re.search(pattern, string4)

#check if there is a match
if match1:
    print(f'"{string1}" matches the pattern.')
if match3:
    print(f'"{string2}" matches the pattern.')
if match3:
    print(f'"{string3}" matches the pattern.')
if match4:
    print(f'"{string4}" matches the pattern.')
