#!/usr/bin/env python
import os
import time
import sys
rootdir = sys.argv[1]
if not os.path.exists(rootdir):
        os.makedirs(rootdir)

dirList = []

charS = ""
for i in range(0,10240):
        charS = charS + 'a'

for i in range(0,100):
        dirName = rootdir+"/dir"+str(i)
        dirList.append(dirName)

start =  "%.9f" % time.time()
for k in dirList:
        os.chdir(rootdir)
        if not os.path.exists(k):
                print("In %s" %k)
                os.makedirs(k)
        os.chdir(k)
        for i in range(0,1000):
                fileName = str(i)+".txt"
                if not os.path.exists(fileName):
                        fileD = open(fileName,'w')
                        fileD.write(charS)
                        fileD.close()
        subDir = k+"/subDir"
#        print subDir
        os.makedirs(subDir)
        os.chdir(subDir)
        for i in range(0,1000):
                fileName = str(i)+"-subdir.txt"
                if not os.path.exists(fileName):
                        fileD = open(fileName,'w')
                        fileD.write(charS)

end =  "%.9f" % time.time()
print "Time taken: %.9f" %(float(end)-float(start))
