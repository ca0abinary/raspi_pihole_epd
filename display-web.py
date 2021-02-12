#!/usr/bin/python3

import time, subprocess, epd2in7
from selenium import webdriver
from xvfbwrapper import Xvfb
from PIL import Image

with Xvfb(width=528, height=352) as xvfb:
  browser = webdriver.Chrome()
  browser.get('http://localhost/admin/')
  browser.execute_script('document.getElementById("queries-over-time").scrollIntoView()')
  time.sleep(3)
  browser.save_screenshot('temp.png')
  browser.close()

cmd = 'convert temp.png -define dither:diffusion-amount=85% -remap 4gray.png -resize 264x176\! -flop BMP3:output.bmp'
subprocess.call(cmd, shell=True)

epd = epd2in7.EPD()
epd.init()
epd.Clear(0xFF)
epd.Init_4Gray()
Himage = Image.open('output.bmp')
epd.display_4Gray(epd.getbuffer_4Gray(Himage))
epd.sleep()
epd.Dev_exit()
