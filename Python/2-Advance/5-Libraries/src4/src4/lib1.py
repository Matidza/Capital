#Statistic Module
import statistics

print(statistics.mean([100,56,87,90]), sep="")

#New module (sys)

import sys
if len(sys.argv) < 2:
   print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])