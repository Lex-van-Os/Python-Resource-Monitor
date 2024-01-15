#!/bin/bash

# Sleep before executing the script to simulate different connection times to the server
sleep $STARTUP_DELAY

# Open write end and read end of the pipe to the server
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

    # Create a JSON object
    message="{\"timestamp\": \"$timeStamp\", \"processes\": $processes, \"cpuUsage\": $cpuUsage, \"memoryUsage\": $memoryUsage}"

    echo $message

    echo $message >&3
    
    sleep 1
done

# Close both the write end and read end of the pipe
exec 3>&-
exec 3<&-