#!/usr/bin/env python
import os
import time
import sys

mountdir = sys.argv[1]                  # dir where you have mounted your filesystem
bmType = sys.argv[2]                    # acceptable values make a dictionary 
dataSize = sys.argv[3]                  # possible values make a dictionary as in create.py 
numIter = int(sys.argv[4])                   # no. of iterations for each experiment 

if not os.path.exists(mountdir):
        os.makedirs(mountdir)

size = {}
size['1k']    =  1024
size['64k']   =  64*1024
size['128k']  =  128*1024
size['256k']  =  256*1024
size['512k']  =  512*1024
size['1m']    =  1024*1024
size['16m']   =  16*1024*1024
size['64m']   =  64*1024*1024
size['128m']  =  128*1024*1024
size['256m']  =  256*1024*1024
size['512m']  =  512*1024*1024
size['1g']    =  1024*1024*1024

def clearAllCache():
	os.system("exec /bin/bash")
	os.system("sudo sh -c \"sync; echo 3 > /proc/sys/vm/drop_caches\"")
	
	
def readWriteThruput():
	os.chdir(mountdir)
        filename = dataSize +".txt"
        if os.path.exists(filename):
                os.unlink(filename)
                fD = open(filename,'w')
        bytesToWrite = size[sys.argv[3]]

        charS = ""
        for i in range(0,bytesToWrite):
                charS = charS + 'a'

        start =  "%.9f" % time.time()
        fD.write(charS)
        fD.flush()
        os.fsync(fD)
        fD.close()
        end =  "%.9f" % time.time()
        timeTaken = (float(end)-float(start))
        print "Time taken: %.9f" %timeTaken


if bmType == '1':
	print("**************************************************************")
	print("| Benchmark - Read/Write Throughput for data size - %s |" %dataSize)
	print("**************************************************************")
	#print("Changing dir to %s" %mountdir)
	for i in range(0,numIter):
#		clearAllCache()
		readWriteThruput()

