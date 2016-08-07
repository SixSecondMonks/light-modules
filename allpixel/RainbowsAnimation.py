from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.visualizer import *
from bibliopixel import colors
from bibliopixel import LEDStrip
#import the module you'd like to use
from BiblioPixelAnimations.strip import Wave

#init driver with the type and count of LEDs you're using
# driver = DriverSerial(type=LEDTYPE.WS2812B, num=10)
driver = DriverVisualizer(num=50)

#init controller
led = LEDStrip(driver)

#init animation; replace with whichever animation you'd like to use
# anim = Rainbows.RainbowCycle(led)
anim = Wave.WaveMove(led, colors.Red, 4)

try:
    #run the animation
    anim.run()
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update() 