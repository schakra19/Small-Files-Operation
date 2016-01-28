#!/bin/bash
echo "Running create script $2 times"
echo "******************************"
for ((n=0;n<$2;n++))
        do
#		source cache.sh
		sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"
		source scriptls.sh 
        done
