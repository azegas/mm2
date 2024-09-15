#!/bin/bash

# List of log files to clean
log_files=(
    "/home/$USER/GIT/mm2/logs/app.log"
    "/home/$USER/GIT/mm2/logs/cron_aliveness.log"
)

# Function to clean a log file
clean_log_file() {
    local file="$1"
    if [ -f "$file" ]; then
        echo "Cleaning $file"
        > "$file"
        echo "Cleaned $file"
    else
        echo "File not found: $file"
    fi
}

# Main script
echo "Starting log cleanup process..."

for file in "${log_files[@]}"; do
    clean_log_file "$file"
done

echo "Log cleanup process completed."
