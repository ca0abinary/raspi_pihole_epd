#!/usr/bin/python3

import re, subprocess, epd2in7
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont

x = subprocess.run(['/usr/local/bin/pihole', '-c', '-e'], capture_output=True)
y = re.sub('\x1B\[([0-9]{1,3}((;[0-9]{1,3})*)?)?[m|K]', '', x.stdout.decode())
y = y.replace('\x1b[H\x1b[2J\x1b[3J', '')

epd = epd2in7.EPD()
epd.init()
epd.Clear(0xFF)
Himage = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(Himage)

font = ImageFont.truetype('font.ttc', 9)
ypos = 0
for line in y.split('\n'):
  draw.text((0,ypos), line, font = font, fill=0)
  ypos = ypos + 9

now = datetime.now()
draw.rectangle((0,ypos,epd.height,epd.width), fill = 0)
draw.text((0,ypos), now.strftime('%c'), font = font, fill = 1)

epd.display(epd.getbuffer(Himage))
epd.sleep()
epd.Dev_exit()
