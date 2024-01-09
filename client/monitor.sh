#!/bin/bash

exec 3<>/dev/tcp/monitor-server/8080

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

    message="Timestamp: $timeStamp, Processes: $processes, CPU Usage: $cpuUsage%, Memory Usage: $memoryUsage"

    echo $message

    echo $message >&3
    
    sleep 1
done

exec 3>&-
exec 3<&-