import argparse
from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.visualizer import *
from bibliopixel import colors
from bibliopixel import LEDStrip
from bibliopixel import LEDMatrix
#import the module you'd like to use

from animations import YellowTwinkle
from animations import Hexazoom
from BiblioPixelAnimations.strip import WhiteTwinkle
from BiblioPixelAnimations.strip import Rainbows
from BiblioPixelAnimations.strip import FireFlies
from BiblioPixelAnimations.strip import LarsonScanners
from BiblioPixelAnimations.strip import PartyMode
from BiblioPixelAnimations.strip import PixelPingPong
from BiblioPixelAnimations.strip import Wave
from BiblioPixelAnimations.strip import ColorPattern

parser = argparse.ArgumentParser()
parser.add_argument("--ledtype", help="LED type.  `ws` or `apa`.", action="store", default="ws")
parser.add_argument("--ledcount", help="Count of LED lights.", action="store", default=10, type=int)
parser.add_argument("--animation", help="Name of animation.", action="store", default="rainbow")
parser.add_argument("--framerate", help="set framerate.", action="store", type=int, default=60)
args = parser.parse_args()

# switch LED type of necessary
if args.ledtype == 'apa':
	ledtype = LEDTYPE.APA102
else:
	ledtype = LEDTYPE.WS2812B

# initialize led strip and driver
driver = DriverSerial(type=ledtype, num=args.ledcount)
led = LEDStrip(driver)

# colors 
rainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Purple]
binary = [colors.Blue, colors.White]

# depending on arg, run selected animation
if args.animation == "whitetwinkle":
	anim = WhiteTwinkle.WhiteTwinkle(led)
elif args.animation == "larsonscanners":
	anim = LarsonScanners.LarsonScanner(led, colors.Red)
elif args.animation == "hexazoom":
	anim = Hexazoom.Hexazoom(led)
elif args.animation == "yellowtwinkle":
	anim = YellowTwinkle.YellowTwinkle(led)
else:
	anim = Rainbows.RainbowCycle(led)

#init animation; replace with whichever animation you'd like to use
# anim = Rainbows.RainbowCycle(led)
# anim = WhiteTwinkle.WhiteTwinkle(led)
# anim = FireFlies.FireFlies(led, rainbow)
# anim = LarsonScanners.LarsonScanner(led, colors.Red)
# anim = LarsonScanners.LarsonRainbow(led)
# anim = PartyMode.PartyMode(led, rainbow)
# anim = PixelPingPong.PixelPingPong(led)
# anim = Wave.Wave(led, colors.Blue, 10)
# anim = ColorPattern.ColorPattern(led, binary, 2)

try:
    #run the animation
    anim.run(fps=args.framerate)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update() 