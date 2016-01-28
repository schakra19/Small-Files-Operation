#!/usr/bin/env python
import os
import sys
import time
rootdir = sys.argv[1]
chunks = int(sys.argv[2])
total = 256*1024*1024
perfile = total/chunks
#print("Size perfile is %d" %perfile)
dirName = rootdir+"/large"
if not os.path.exists(dirName):
        os.makedirs(dirName)
os.chdir(dirName)
#print dirName


start = "%.9f" % time.time()
for i in range(0,chunks):
        fileName = "lg-"+str(i)+".txt"
        fileD = open(fileName,"r")
        s = fileD.read()
        fileD.close()

end =  "%.9f" % time.time()
print "Time taken: %.9f" %(float(end)-float(start))
