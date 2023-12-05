num = [1,2,5]
position = 0
while position < len (num):
    num1 = num[position]
    if num1 % 2 == 0:
        print('Found even number', num1)
        break
    position = position + 1
else: #break not called
    print("No even number found")