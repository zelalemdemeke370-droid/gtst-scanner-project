#!/bin/bash

# Validate that both parameters (IP and Script name) are supplied
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <Target_IP> <NSE_Script_Name>"
    echo "Example: $0 192.168.1.1 http-enum"
    exit 1
fi

TARGET_IP=$1
SCRIPT_NAME=$2

echo "=================================================="
echo "Initializing Nmap NSE Scan..."
echo "Target IP: $TARGET_IP"
echo "Executing Script: $SCRIPT_NAME"
echo "=================================================="

# Run the Nmap scan calling the specific engine script
nmap --script "$SCRIPT_NAME" "$TARGET_IP"

echo "=================================================="
echo "Scan execution completed."