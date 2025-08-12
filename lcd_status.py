import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Led:

    def __init__(self, font_name=None, font_size=None):
        self.__initialize()
        if font_name and font_size:
            self._font = ImageFont.load_default()
        else:
            self._font = ImageFont.truetype(font_name, font_size)
    
    def __initialize(self):

        i2c = busio.I2C(board.SCL, board.SDA)
        self._display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
        self._display.fill(0)
        self._display.show()
        

    def show_text(self, lines):
        
        ascent, descent = self._font.getmetrics()
        line_height = ascent + descent + 2
       
        image = Image.new("1", (self._display.width, self._display.height))
        draw = ImageDraw.Draw(image)

        if isinstance(lines, str):
            lines = lines.splitlines()

        # Escribir cada línea
        for i, linea in enumerate(lines):
            y = i * line_height
            if y + line_height <= self._display.height:
                draw.text((0, y), linea, font=self._font, fill=255)
            else:
                break  # No escribir fuera del display

        
        self._display.image(image)
        self._display.show()
    
    def get_display_dimmsensions(self):
        return self._display.width, self._display.height
    
    def show_image(self, image):
        self._display.image(image)
        self._display.show()


    def println(self, lines):
        self.show_text(lines)
