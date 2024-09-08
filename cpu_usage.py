#!/bin/bash

NAMESPACE='enter your namespace'
NODE_NAME=$(kubectl get pod -n $NAMESPACE -o=jsonpath='{.items[0].spec.nodeName}')
TOTAL_CPU=$(kubectl describe node $NODE_NAME | grep 'cpu:' | head -n 1 | awk '{print $2}')
OUTPUT_FILE="cpu_usage.log"

echo "Timestamp,Pod Name,CPU Usage (%)" > $OUTPUT_FILE

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    PODS=$(kubectl get pod -n $NAMESPACE --no-headers -o custom-columns=":metadata.name")

    for POD in $PODS; do
        CPU_M=$(kubectl top pod $POD -n $NAMESPACE --no-headers | awk '{print $2}' | sed 's/m//')
        CPU_PERCENT=$(echo "scale=2; ($CPU_M / 1000) / $TOTAL_CPU * 100" | bc)
        echo "$TIMESTAMP,$POD,$CPU_PERCENT" >> $OUTPUT_FILE
    done

    sleep 1
done
