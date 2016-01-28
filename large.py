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

for f in os.listdir(dirName):
	if str(f).endswith(".txt"):
	        os.unlink(f)

charS = ""
for i in range(0,perfile):
        charS = charS + 'a'

start = "%.9f" % time.time()
for i in range(0,chunks):
        fileName = "lg-"+str(i)+".txt"
        if os.path.exists(fileName):
                os.unlink(fileName)
        fileD = open(fileName,"w")
	fileD.write(charS)
	fileD.flush()
 	os.fsync(fileD)
        fileD.close()

end =  "%.9f" % time.time()
print "%.9f" %(float(end)-float(start))
