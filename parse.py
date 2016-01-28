import os
import time
import sys

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

f = open("p.txt","r")
lines = f.readlines()
iterN = lines[0].split("\n")[0]
ds = lines[1].split("\n")[0]
totalBytes = size[ds]
numThreads = lines[2].split("\n")[0]

print "*************************************************"
print "|           Benchmarking Tool v0.001            |"
print "|           Data size            = %-2s           |" %ds
print "|           No.of iterations     = %-2s           |" %iterN
print "|           No.of clients        = %-2s           |" %numThreads
print "*************************************************"

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

writeTimes = []
readTimes = []
multiFTW = []
multiRead = []
smallFiles = []

for i in range(0,len(lines)):
	if lines[i].startswith("Read Throughput"):
		n = int(iterN)
		while(n>0):
			readTimes.append(float(lines[i+n].split("\n")[0]))
			n = n-1
	if lines[i].startswith("Write Throughput"):
		n = int(iterN)
		while(n>0):
			writeTimes.append(float(lines[i+n].split("\n")[0]))
			n = n-1
	if lines[i].startswith("Multi Client FTW"):
                n = int(iterN)
                while(n>0):
                        multiFTW.append(float(lines[i+n].split("\n")[0]))
                        n = n-1 
	if lines[i].startswith("Multi Client Read"):
                n = int(iterN)
                while(n>0):
                        multiRead.append(float(lines[i+n].split("\n")[0]))
                        n = n-1
	if lines[i].startswith("Overhead of creating small files"):
		n = int(iterN)
        	while(n>0):
                	smallFiles.append(float(lines[i+n].split("\n")[0]))
                	n = n-1 
	if lines[i].startswith("Copy"):
		copyTime = float(lines[i+1].split("\n")[0])

	if lines[i].startswith("Grep"):
                grepTime = float(lines[i+1].split("\n")[0])
	
	if lines[i].startswith("Remove"):
                rmTime = float(lines[i+1].split("\n")[0])


den = 1024*1024
readTput = (totalBytes/median(readTimes))/den
writeTput = (totalBytes/median(writeTimes))/den
multiFTWtime = median(multiFTW)
multiReadtime = median(multiRead)
sfTime = median(smallFiles)


print "*************************************************"
print "|                      RESULTS                   |"
print "|   Read throughput           =  %.4f MB/s     |" %readTput
print "|   Write throughput          =  %.4f MB/s     |" %writeTput
print("|   ftw  by %-2s clients        =  %.4fs         |" % (numThreads, multiFTWtime))
print("|   Simult read by %-2s clients =  %.4fs         |" % (numThreads, multiReadtime))
print("|   Small files (2048)        =  %.4fs         |" %sfTime)
print("|   Copy   (cp -r)            =  %.4fs         |" %copyTime)
print("|   Grep   (grep -r)          =  %.4fs         |" %copyTime)
print("|   Remove (rm -r)            =  %.4fs         |" %copyTime)
print "*************************************************"

