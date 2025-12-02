# main.py
from rpi_backlight import Backlight
import sys

bl = Backlight()
arg = sys.argv[1]

if arg == "true":
        bl.power = True
elif arg == "false":
        bl.power = False
else:
  bl.brightness = int(arg)
