"""
Script that generates the code that will be used to compare the MOESI vs Dragon
protocol, this is useful to notice the advantage of the write update protocols
over the write invalidate protocols
"""

#!/usr/bin/python

f = open("MOESIvDragon.trace", "w")

for i in range(1,1001):
    f.write("0 W 0x100\n")
    for j in range(1, 16):
        f.write(str(j) + " R 0x100\n")

f.close()
