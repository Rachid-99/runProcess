# Python program to demonstrate
# command line arguments

import sys

# total arguments
if len(sys.argv) != 3 :
    print("parameter error\n")
    exit(0)

somme = int(sys.argv[1]) + int(sys.argv[2])

print("the sum of ", sys.argv[1], " and ", sys.argv[2], " is ", somme, "\n")

