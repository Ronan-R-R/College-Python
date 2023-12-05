from random import * # * gives everything

fruits = ['apple', 'banana', 'orange', 'cherry']
myfruits=choice(fruits)
print(myfruits)

print("--------------------------")

import math
numb=25
sqrt=math.sqrt(numb)
print("The square root of ", numb, " is ", sqrt)

print("--------------------------")

import pprint #best for longer lists etc...
myDict = [{"Name": "John", "Age": 30, "Address": {"City": "Boksburg", "State":"Gauteng"}},
          {"Name": "Jane", "Age": 26, "Address": {"City": "Lambton", "State":"Gauteng"}}]
print("\n Using the print()")
print(myDict)
print("**************************")
pprint("\n Using the pprint()")
pprint.pprint(myDict)

print("--------------------------")