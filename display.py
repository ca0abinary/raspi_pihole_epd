#!/usr/bin/python3

import re, subprocess, epd2in7
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont

x = subprocess.run(['/usr/local/bin/pihole', '-c', '-e'], capture_output=True)
y = re.sub('\x1B\[([0-9]{1,3}((;[0-9]{1,3})*)?)?[m|K]', '', x.stdout.decode())
y = y.replace('\x1b[H\x1b[2J\x1b[3J', '')

restarted_pihole = False
if not 'Pi-hole: Active' in y:
  subprocess.run(['/usr/local/bin/pihole', 'restartdns'])
  restarted_pihole = True

epd = epd2in7.EPD()
epd.init()
epd.Clear(0xFF)
Himage = Image.new('1', (epd.height, epd.width), 255)
draw = ImageDraw.Draw(Himage)

font = ImageFont.truetype('FiraCode-Regular.ttf', 9)
font_height = font.getsize('A')[1]
ypos = 0
for line in y.split('\n'):
  draw.text((0,ypos), line.replace('    (', '('), font = font, fill=0)
  ypos = ypos + font_height

now = datetime.now().strftime('%c')
now_width, now_height = font.getsize(now)
throttled = subprocess.run(['/usr/bin/vcgencmd', 'get_throttled'], capture_output=True).stdout.decode()
message = 'Voltage OK' if throttled.split('=')[1] == '0x0\n' else 'Undervoltage'
message = f'{message} - restart' if restarted_pihole else message

draw.rectangle((0,ypos,epd.height,epd.width), fill = 0)
draw.text((0,ypos), message, font = font, fill = 1)
draw.text((epd.height - now_width, ypos), now, font = font, fill = 1)

epd.display(epd.getbuffer(Himage))
epd.sleep()
epd.Dev_exit()
