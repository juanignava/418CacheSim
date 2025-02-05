"""
Script that generates the code that will be used to compare the MSI and MESI 
protocol, this is useful to notice the advantage of having the E state
"""

#!/usr/bin/python

f = open("MSIvMESI.trace", "w")

for i in range(1,1001):
    for j in range(0, 16):
        f.write(str(j) + " R " + "0x" + str((i * 16 + j) * 64) + "\n")
        f.write(str(j) + " W " + "0x" + str((i * 16 + j) * 64) + "\n")

f.close()
