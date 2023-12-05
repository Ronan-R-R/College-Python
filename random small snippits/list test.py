mylist = [[1,2,3],[4,5,6],[7,8,9]]
element = mylist[0][1]
print(element)

for row in mylist:
    for element in row:
        print(element, end=" ")
    print()