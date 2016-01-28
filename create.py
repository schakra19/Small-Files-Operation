#!/usr/bin/env python
import os
import time
import sys
rootdir = sys.argv[1]
filesize = sys.argv[2]
if not os.path.exists(rootdir):
        os.makedirs(rootdir)

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
size['2g']    =  2*1024*1024*1024
size['5g']    =  5*1024*1024*1024

os.chdir(rootdir)
filename = sys.argv[2]+".txt"
if os.path.exists(filename):
        os.unlink(filename)
fD = open(filename,'w')

bytesToWrite = size[sys.argv[2]]

charS = ""
for i in range(0,bytesToWrite):
        charS = charS + 'a'

start =  "%.9f" % time.time()
fD.write(charS)
fD.flush()
os.fsync(fD)
fD.close()
end =  "%.9f" % time.time()
print "%.9f" %(float(end)-float(start))
