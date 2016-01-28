#!/usr/bin/env python
import os
import time
import sys
rootdir = sys.argv[1]
filesize = sys.argv[2]
if not os.path.exists(rootdir):
        print("%s does not exist. check args" %rootdir)
else:
        os.chdir(rootdir)

filename = sys.argv[2]+".txt"
if not os.path.exists(filename):
        print("%s does not exist. check args" %filename)
fD = open(filename,'r')

start =  "%.9f" % time.time()
s = fD.read()
end =  "%.9f" % time.time()
#print("Bytes read %d" % len(s))
fD.close()
print "%.9f" %(float(end)-float(start))
