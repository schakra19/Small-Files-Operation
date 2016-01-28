#!/bin/bash
echo "Running create script $2 times"
echo "******************************"
for ((n=0;n<$2;n++))
        do
		source cache.sh
                python create.py $3 $1
        done


echo "Running read script $2 times"
echo "******************************"
for ((n=0;n<$2;n++))
        do
		source cache.sh
                python read.py $3 $1
        done
~            
