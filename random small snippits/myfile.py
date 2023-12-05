""" myfile = open("examplefile.txt", "w")
myfile.write("hello there")
myfile.close()  """

f = open("examplefile.txt", "r")
readfile = f.read()
print(readfile)
f.close()