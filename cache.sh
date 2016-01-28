#!/bin/bash
#echo "Clearing cache on vms..."
sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"
#echo "Clearing cache on vm-2..."
ssh "node-1" 'bash -s' < l.sh
#echo "Clearing cache on vm-3..."
ssh "node-2" 'bash -s' < l.sh

