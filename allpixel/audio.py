#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.network import DriverNetwork
from bibliopixel.led import *

import bibliopixel.gamma as gamma
import argparse

from FFT_Audio_Animation import EQ, BassPulse

w = 10
h = 5
print "Pixel Count: {}".format(w*h)

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("--visualizer", help="use the visualization driver", action="store_true")
parser.add_argument("--serial", help="Use the serial driver", action="store_true")
parser.add_argument("--network", help="use the network driver", action="store_true")
args = parser.parse_args()

if args.visualizer:
    driver = DriverVisualizer(width = w, height = h, stayTop = True)
    led = LEDMatrix(driver, width = w, height = h)
elif args.serial:
	driver = DriverSerial(num = w * h, type = LEDTYPE.WS2812B)
	led = LEDMatrix(driver, width = w, height = h)
else:
    driver = DriverNetwork(num=w*h, width=w, height=h, host = "192.168.210.203")
    #load the LEDMatrix class
    #change rotation and vert_flip as needed by your display
    led = LEDMatrix(driver, width = h, height = w, rotation = MatrixRotation.ROTATE_270, vert_flip = True)


led.setMasterBrightness(255)
import bibliopixel.log as log
#log.setLogLevel(log.DEBUG)

minFrequency   = float(50) # 50 Hz
maxFrequency   = float(15000) # 15000 HZ

try:
    # Equalizer/Spectrum Animation
    anim = EQ(led, minFrequency, maxFrequency)
    anim.run(fps=20, max_steps = 20 * 360) # 1 minute animation
    # Bass based pulse animation
    anim = BassPulse(led, minFrequency, maxFrequency)
    anim.run(fps=20, max_steps = 20 * 360) # 1 minute animation
except KeyboardInterrupt:
    pass

anim.endRecord()
led.all_off()
led.update()