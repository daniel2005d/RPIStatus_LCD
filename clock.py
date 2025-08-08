import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


# Inicializar I2C y display
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Limpiar la pantalla
display.fill(0)
display.show()

# Crear imagen para dibujar
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# Cargar fuente
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
except:
    font = ImageFont.load_default()

def show():
    draw.rectangle((0, 0, display.width, display.height), outline=0, fill=0)

    # Obtener hora actual
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    # Calcular tamaño del texto (usando getbbox para compatibilidad moderna)
    bbox = font.getbbox(current_time)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Centrar el texto
    x = (display.width - text_width) // 2
    y = (display.height - text_height) // 2

    # Dibujar texto
    draw.text((x, y), current_time, font=font, fill=255)

    # Mostrar en pantalla
    display.image(image)
    display.show()
