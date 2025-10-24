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

# Install

```bash
git clone https://github.com/daniel2005d/RPIStatus_LCD.git
cd RPIStatus_LCD
sudo apt install python3-dev python3-pip python3-setuptools python3-wheel build-essential
python -m venv .venv
source .venv/bin/activate
pip install RPi.GPIO
```

## Kali

```bash
sudo vim /boot/firmware/config.txt
dtparam=i2c_arm=on # Uncomment this line

sudo modprobe i2c-dev
echo "i2c-dev" | sudo tee -a /etc/modules
sudo apt install i2c-tools
sudo reboot
```

# Check

```bash
sudo apt install i2c-tools
ls /dev/i2c*
sudo i2cdetect -y <Devide ID>
```
