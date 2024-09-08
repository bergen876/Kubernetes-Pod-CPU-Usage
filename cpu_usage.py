#!/bin/bash

NAMESPACES=("kube-system" "replace with your namespace" "calico-system")
OUTPUT_FILE="resource_usage.log"

echo "Timestamp (ms),Namespace,Pod Name,CPU Usage (m),Memory Usage (Mi)" > $OUTPUT_FILE

while true; do
    TIMESTAMP=$(date +%s%3N)  # Current time in milliseconds

    for NAMESPACE in "${NAMESPACES[@]}"; do
        # Get all pod metrics for the namespace in one call
        kubectl top pod -n $NAMESPACE --no-headers | while read -r POD CPU_MEM; do
            CPU_M=$(echo $CPU_MEM | awk '{print $1}' | sed 's/m//')
            MEMORY_M=$(echo $CPU_MEM | awk '{print $2}' | sed 's/Mi//')

            # Debugging output
            echo "DEBUG: NAMESPACE=$NAMESPACE POD=$POD CPU_M=$CPU_M MEMORY_M=$MEMORY_M"

            if [[ -z "$CPU_M" || -z "$MEMORY_M" ]]; then
                echo "Skipping logging due to missing values."
                continue
            fi

            echo "$TIMESTAMP,$NAMESPACE,$POD,$CPU_M,$MEMORY_M" >> $OUTPUT_FILE
        done
    done

    sleep 0.1
done
