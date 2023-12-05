import time
#start timer
starttime = time.time()
#code to be timed
for i in range(30000):
    print("hello world")
#stop the timer
stoptime = time.time()
#Calculate the time elapse
timeelapsed=stoptime-starttime
#print the time spent
print("The spent wa: ",timeelapsed, "seconds")