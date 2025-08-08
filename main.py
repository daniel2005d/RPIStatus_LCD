import psutil
from PIL import Image, ImageDraw, ImageFont
from lcd_status import Led
import socket
import psutil
import clock
import RPi.GPIO as GPIO
import time

led = Led()

def memusage():
    mem = psutil.virtual_memory()
    percent = mem.percent
    total = mem.total // (1024**2)
    used = mem.used // (1024**2)
    return f"RAM: {used}MB / {total}MB"

def cpuusage():
    total = psutil.cpu_percent(interval=1)
    return f"CPU: {total}%"

def temperaturecpu():
    message = ""
    if hasattr(psutil, "sensors_temperatures"):
        temperaturas = psutil.sensors_temperatures()
        
        # Verificar si se tiene información sobre la CPU
        if 'cpu_thermal' in temperaturas:  # En Linux, "coretemp" es común, pero puede variar
            for sensor in temperaturas['cpu_thermal']:
                message+=f"{sensor.label}: {sensor.current}°C"
    return message

def getipaddress():
    address = []
    addrs = psutil.net_if_addrs()
    for interface, addr_list in addrs.items():
        if interface == 'lo':
            continue
        for addr in addr_list:
            if addr.family == socket.AF_INET:
                #print(f"  {interface}: {addr.address}")
                address.append(f"{interface}: {addr.address}")

    return address
        #elif addr.family == psutil.AF_LINK:  # Esto sí es de psutil
        #    print(f"  MAC: {addr.address}")

def critialprocess():
    # Obtener todos los procesos en ejecución
    process = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            process.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Excluir procesos que ya no existen o a los que no podemos acceder
            pass
    
    # Ordenar los procesos por el uso de CPU (en orden descendente)
    sorted_process = sorted(process, key=lambda x: x['cpu_percent'], reverse=True)
    
    # El proceso con más CPU utilizado
    if sorted_process:
        high_process = sorted_process[0]
        return f"Name={high_process['name']}, CPU={high_process['cpu_percent']}%"
    else:
        return "No se pudo obtener información sobre los procesos."

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            if GPIO.input(17) == GPIO.LOW:
                print_list = getipaddress()
                print_list.append(memusage())
                print_list.append(temperaturecpu())
                led.println(print_list)
                time.sleep(30)
            else:
                clock.show()
            
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
    


if __name__ == "__main__":
    main()
