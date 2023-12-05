#call sys.path() to get a list of strings that sepcifies the search paths for modules
#call list.append (directory/files)
#to add the cuurrent to the path

import sys
sys.path.append(".")

#import class from file
from pythgoncarclass import Car

#instatiate an Object

Ferrari = Car()
Bugatti = Car()


#Populate data to our object
Ferrari.fuelConsumption = 11
Ferrari.tankCapacity = 45

Bugatti.fuelConsumption = 13
Bugatti.tankCapacity = 58

#print consumption
print ("With a tank capacity of " + str (Ferrari.tankCapacity)  + " liters "
       + " and a fuel capacity rate of " + str (Ferrari.fuelConsumption)
       + " liters per 100km, this car can travel a distance of "
       + str ("%.2f"%((Ferrari.tankCapacity/Ferrari.fuelConsumption)* 100))
       + " kilometers on a single tank. \n")

print ("With a tank capacity of " + str (Bugatti.tankCapacity)  + " liters "
       + " and a fuel capacity rate of " + str (Bugatti.fuelConsumption)
       + " liters per 100km, this car can travel a distance of "
       + str ("%.2f"%((Bugatti.tankCapacity/Bugatti.fuelConsumption)* 100))
       + " kilometers on a single tank. \n")