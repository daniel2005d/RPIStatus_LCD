from setuptools import setup
from glob import glob
import os

modules = glob("./*.py")
module_names = [
    os.path.splitext(os.path.basename(f))[0]
    for f in modules
    if os.path.basename(f) != "setup.py"
]


setup(
    author="Daniel Vargas",
    platforms=["RaspBerry Pi"],
    name="lcd-status",
    version="1.0",
    py_modules=module_names,
    
    install_requires=["Adafruit_Blinka==8.56.0",
                    "adafruit_circuitpython_ssd1306==2.12.19",
                    "board==1.0",
                    "psutil",
                    "Pillow==11.1.0",
                    "psutil==7.0.0"], 
    entry_points={
        "console_scripts": [
            "rpi-status-lcd=main:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10"
    ]
)
