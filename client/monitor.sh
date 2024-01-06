#!/bin/sh

echo "Hello World!"

while true
do
    # Timestamp: date
    # Number of running processes: ps
    # Cpu usage: mpstat
    # Free memory: free

    timeStamp=$(date +"%H:%M:%S")
    processes=$(ps --no-headers | wc -l)
    cpuUsage=$(mpstat 1 1 | awk '/Average:/ {print 100 - $NF}')
    memoryUsage=$(free | awk '/Mem:/ {print $4}')

    echo "Timestamp: $timeStamp, Processes: $processes, CPU Usage: $cpuUsage%, Memory Usage: $memoryUsage"
    
    sleep 1
done