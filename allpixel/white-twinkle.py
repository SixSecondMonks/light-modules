from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.visualizer import *
from bibliopixel import colors
from bibliopixel import LEDStrip
from bibliopixel import LEDMatrix
#import the module you'd like to use
from BiblioPixelAnimations.strip import WhiteTwinkle
from BiblioPixelAnimations.strip import Rainbows
from BiblioPixelAnimations.strip import FireFlies
from BiblioPixelAnimations.strip import LarsonScanners
from BiblioPixelAnimations.strip import PartyMode
from BiblioPixelAnimations.strip import PixelPingPong
from BiblioPixelAnimations.strip import Wave
from BiblioPixelAnimations.strip import ColorPattern

# total leds
ledstringnum = 169

#init driver with the type and count of LEDs you're using
driver = DriverSerial(type=LEDTYPE.WS2812B, num=ledstringnum)
# driver = DriverVisualizer(width = 10, height = 10)

#init controller
led = LEDStrip(driver)

# colors 
rainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Purple]
binary = [colors.Blue, colors.White]

#init animation; replace with whichever animation you'd like to use
# anim = Rainbows.RainbowCycle(led)
anim = WhiteTwinkle.WhiteTwinkle(led)
# anim = FireFlies.FireFlies(led, rainbow)
# anim = LarsonScanners.LarsonScanner(led, colors.Red)
# anim = LarsonScanners.LarsonRainbow(led)
# anim = PartyMode.PartyMode(led, rainbow)
# anim = PixelPingPong.PixelPingPong(led)
# anim = Wave.Wave(led, colors.Blue, 10)
# anim = ColorPattern.ColorPattern(led, binary, 2)

try:
    #run the animation
    anim.run(fps=60)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update() 