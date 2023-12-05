import re

#define the regex pattern
pattern = r'\d+' # + means match one or more. d means digit

#define the string to search
string = 'I have 3 apples and 2 bananas.'

#searh for matches using patterns
matches = re.findall(pattern, string)

print(matches)