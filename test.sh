#!/bin/bash
# 1 = mountdir
# 2 = filesize
# 3 = no. of iterations 
# 4 = no. of threads 

echo $3
echo $2
echo $4
echo "Write Throughput"
for ((n=0;n<$3;n++))
        do
#		source cache.sh
                python create.py $1 $2
        done
echo "Read Throughput"
for ((n=0;n<$3;n++))
        do
#		source cache.sh
                python read.py $1 $2
        done

echo "Multi Client FTW"
for ((n=0;n<$3;n++))
	do
		#sudo command 
		start=$(date +%s.%N)
		./thread $4
		end=$(date +%s.%N)
		echo $end - $start | bc
	done

echo "Multi Client Read"
for ((n=0;n<$3;n++))
        do
                #sudo command
		python create.py $1 $2 > /dev/null
		mv "$2.txt" "myfile.txt"
                start=$(date +%s.%N)
                ./multiread $4
                end=$(date +%s.%N)
                echo $end - $start | bc
        done

echo "Overhead of creating small files"
for ((n=0;n<$3;n++))
	do
		#source cache.sh
#		python large.py $1 2048 
		echo "I am supposed to run small file test"
	done

echo "File utilities"
#source cache.sh
mkdir copyfolder
start=$(date +%s.%N)
cp -r $1/large copyfolder
end=$(date +%s.%N)
echo "Copy"
echo  $end - $start | bc

#source cache.sh
start=$(date +%s.%N)
grep -Iir project739 copyfolder
end=$(date +%s.%N)
echo "Grep"
echo  $end - $start | bc

#source cache.sh
start=$(date +%s.%N)
rm -r copyfolder
end=$(date +%s.%N)
echo "Remove"
echo  $end - $start | bc

