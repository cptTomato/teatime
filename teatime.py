import time
import sys


h = int(input("Please enter your tea time (sec): " +  "\n"))

while h>0:
    print(h)
    time.sleep(1)
    h = h-1
    if h==0:
        print("Your tea is ready! ENJOY!")
