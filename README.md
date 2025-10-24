# Connect to KMDO 96C  I2C

| LCD KMDO 96C | Raspberry Pi GPIO  | Función      |
| ------------ | ------------------ | ------------ |
| VCC          | Pin 1 (3.3V)       | VCC          |
| GND          | Pin 6 (GND)        | Ground       |
| SCL          | Pin 5 (GPIO 3/SCL) | Clock        |
| SDA          | Pin 3 (GPIO 2/SDA) | Data         |


# PUSH Button

| Button | GPIO Raspberry Pi      |
| ----- | ---------------------- |
| Pin 1 | GPIO17 (pin 11) |
| Pin 2 | GND (pin  6)     |


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

# Kali

```bash
sudo apt install python3-pip
pip install RPi.GPIO

sudo vim /boot/firmware/config.txt
dtparam=i2c_arm=on # Uncomment this line

sudo modprobe i2c-dev
echo "i2c-dev" | sudo tee -a /etc/modules
sudo apt install i2c-tools
sudo reboot
```
