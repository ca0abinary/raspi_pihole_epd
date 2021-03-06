# PiHole e-Paper Display

![e-paper hat image](raspi_pihole_epd.jpg)

Outputs the result of `pihole chronometer` to a [Waveshare 2.7 inch e-Paper hat](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT).

## Enable SPI Interface on the Raspberry Pi

Before connecting the e-paper display to the Raspberry Pi the SPI interface needs to be enabled. This can be accomplished by using the `raspi-config` command and selecting `Interfacing options -> SPI -> Yes`

![enable interface](https://www.waveshare.com/w/upload/1/1e/RPI_open_spi.png)

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
  - 4gray.png <img src="4gray.png" height="24">
    - Support for converting images to 4 grey (from [adafruit article](https://learn.adafruit.com/adafruit-eink-display-breakouts/drawing-bitmaps))
- EPD support files
  - epd2in7.py - if you have another type of display this file can be swapped out
  - epdconfig.py - config file from waveshare
  - FiraCore-Regular.ttf - mono-space font from the excellent [FiraCode project](https://github.com/tonsky/FiraCode). This can be swapped out for a standard font such as Roboto if the strings running off-screen bothers you. A mono-space font makes the chronometer output look nicer.
