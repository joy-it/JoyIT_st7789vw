from PIL import Image, ImageFont, ImageDraw
from st7789vw import ST7789VW
import time

# setup lcd
lcd = ST7789VW()

# generate canvas with the appropiate size and background colour
img = Image.new("RGB", (240, 240), (39, 92, 107))
# setup font and size
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
# generate draw object for writing on canvas
draw = ImageDraw.Draw(img)
# setup writing with position, text, font and text colour
draw.text((20, 100), "Hallo Joy-IT!", font=font, fill=(255, 255, 255))

# show canvas on display
lcd.display(img)

# show picture for 10 seconds
time.sleep(10)

# clear display
lcd.clear()

# close connection with lcd
lcd.close()