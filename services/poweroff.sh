#!/bin/bash
set -euo pipefail
echo "$(date) - poweroff.sh ejecutado" >> /var/log/poweroff.log
/home/daniel/RPIStatus_LCD/.venv/bin/python /home/daniel/RPIStatus_LCD/poweroff.py