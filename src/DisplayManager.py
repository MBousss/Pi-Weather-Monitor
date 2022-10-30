import adafruit_character_lcd.character_lcd as characterlcd
import board
import digitalio

class DisplayManager:
    def __init__(self):
        # Raspberry Pi pin configuration:
        self.lcd_rs = digitalio.DigitalInOut(board.D26)
        self.lcd_en = digitalio.DigitalInOut(board.D19)
        self.lcd_d7 = digitalio.DigitalInOut(board.D27)
        self.lcd_d6 = digitalio.DigitalInOut(board.D22)
        self.lcd_d5 = digitalio.DigitalInOut(board.D24)
        self.lcd_d4 = digitalio.DigitalInOut(board.D25)
        
        self.lcd_columns = 16
        self.lcd_rows    = 2

    def display(self, data):
        text = self.formatDataToText(data)
        # Initialize the LCD using the pins above.
        lcd = characterlcd.Character_LCD_Mono(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7, self.lcd_columns, self.lcd_rows)
        lcd.clear()
        lcd.message = text
        
    def formatDataToText(self, data):
        return "{}\n{}: {}".format(data['location'], data['text'], data['temp'])