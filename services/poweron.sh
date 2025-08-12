#!/bin/bash
set -euo pipefail
echo "$(date) - poweron.sh running" >> /var/log/poweron.log
/home/daniel/RPIStatus_LCD/.venv/bin/python /home/daniel/RPIStatus_LCD/poweron.py