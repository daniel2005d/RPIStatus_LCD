# Connect to KMDO 96C  I2C

| LCD KMDO 96C | Raspberry Pi GPIO  | Función      |
| ------------ | ------------------ | ------------ |
| VCC          | Pin 1 (3.3V)       | VCC          |
| GND          | Pin 6 (GND)        | Ground       |
| SCL          | Pin 5 (GPIO 3/SCL) | Clock        |
| SDA          | Pin 3 (GPIO 2/SDA) | Data         |


# Add to crontab

<!-- status.sh -->
```bash
#!/bin/bash
#

source /home/daniel/RPIStatus_LCD/.venv/bin/activate
python /home/daniel/RPIStatus_LCD/main.py
```

## crontab

```bash
* * * * * /status.sh >> crontab.log
```