# PiHole e-Paper Display

![e-paper hat image](https://www.waveshare.com/w/thumb.php?f=2.7inch-e-paper-hat-3.jpg&width=300)

Outputs the result of `pihole chronometer` to a [Waveshare 2.7 inch e-Paper hat](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT).

## Installation

```sh
sudo apt update -y && sudo apt install -y python3 python3-pil
git clone https://github.com/ca0abinary/raspi_pihole_epd.git
```

To make it run on a schedule:

```sh
cd raspi_pihole_epd
crontab -l > cronjobs
echo "* * * * * $(pwd)/display.py" >> cronjobs
crontab cronjobs
```

## Files

- display.py
  - Main application, parses the output of `pihole chronometer` and displays on the result to the e-paper hat
- display-web.py
  - Displays the website graph using selenium, webdriver, and imagemagick
  - 4gray.png
    - Support for converting images to 4 grey (from adafruit)
- EPD support files
  - epd2in7.py - if you have another type of display this file can be swapped out
  - epdconfig.py - config file from waveshare
  - font.ttc - font from waveshare
