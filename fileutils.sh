#!/bin/bash
#sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"

source cache.sh
mkdir copyfolder
start=$(date +%s.%N)
cp -r /users/krai/cephfs/hive-1.2.1 copyfolder
end=$(date +%s.%N)

echo "Time to copy : "
echo  $end - $start | bc

source cache.sh
start=$(date +%s.%N)
grep -Iir project739 copyfolder
end=$(date +%s.%N)

echo "Time to grep : "
echo  $end - $start | bc

source cache.sh
start=$(date +%s.%N)
rm -r copyfolder
end=$(date +%s.%N)

echo "Time to remove : "
echo  $end - $start | bc
