#!/bin/sh
#echo "Start: " $(date +%s.%N)
start=$(date +%s.%N)
#./thread $1
tree > /dev/null
#echo "End: " $(date +%s.%N)
end=$(date +%s.%N)

echo $end - $start | bc
