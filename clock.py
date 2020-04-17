import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
from time import gmtime, strftime

RST = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()
#ctime = strftime("%H:%M:%S", gmtime())

while True:
    ctime = strftime("%I:%M:%S", gmtime())
    #flip the stuff

    
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Write two lines of text.
    disp.clear()
#   disp.display()
#    draw.text((x, top+0),     "     /+-+-+-+-+\\", font=font, fill=255)
    draw.text((x, top+8),     "     + Welcome +",  font=font, fill=255)
    draw.text((x, top+16),    "     |    to   |",  font=font, fill=255)
    draw.text((x, top+25),    "     |  B.L.U. |",  font=font, fill=255)
    draw.text((x, top+33),    "     +DigiGlass+",  font=font, fill=255)
    draw.text((x, top+42),    "     \-+-+-+-+-/",  font=font, fill=255)
    draw.text((x+33, top),     ctime,              font=font, fill=255)

    # Display image.
    mimage = image1.transpose(Image.FLIP_TOP_BOTTOM)
    disp.image(mimage.rotate(270))
    disp.display()
    time.sleep(.01)
