import re

pattern = r'\bcat\b' # b is boundary

string = 'The cat is sleeping on the mat.'

#search for matches
match = re.search(pattern, string)

#check if there was a match
if match:
    print(f'Match found at index{match.start()}')
else:
    print('No match found.')