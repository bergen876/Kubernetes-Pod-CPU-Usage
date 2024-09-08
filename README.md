# Kubernetes Pod Resource Usage Monitor

This Bash script continuously monitors the CPU and memory usage of pods in specified Kubernetes namespaces and logs the data to a file. It captures metrics every 100 milliseconds and appends them to a CSV file for later analysis.

## Features
- Captures **CPU** and **memory usage** for each pod in specified namespaces.
- Logs data in a **CSV format** with timestamp (in milliseconds), namespace, pod name, CPU usage (in millicores), and memory usage (in MiB).
- Configurable to monitor multiple namespaces simultaneously.
- Minimal overhead, capturing metrics every 100ms.

## Prerequisites
- A Kubernetes cluster with `kubectl` installed and properly configured to access the cluster.
- The `kubectl top` command requires [metrics-server](https://github.com/kubernetes-sigs/metrics-server) to be installed and running in your cluster.

## How to Use

1. Clone this repository or download the script.
2. Modify the `NAMESPACES` array in the script to include the namespaces you want to monitor. By default, the script monitors the following namespaces:
   - `kube-system`
   - `riab`
   - `calico-system`

3. Make the script executable:
   ```bash
   chmod +x resource_usage.sh
