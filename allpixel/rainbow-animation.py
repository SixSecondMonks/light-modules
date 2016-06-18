#load the AllPixel driver. Works for LEDStrip AND LEDMatrix
from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.visualizer import *
driver = DriverSerial(num = 50, type = LEDTYPE.WS2812B)
# driver = DriverVisualizer(width = 50, height = 50, pixelSize = 15)

#import the bibliopixel base classes
from bibliopixel import *
from bibliopixel.animation import *
class BasicAnimTest(BaseStripAnim):
    def __init__(self, led):
        super(BasicAnimTest, self).__init__(led)
        #do any initialization here

    def step(self, amt = 1):
        for i in range(50):
            self._led.set(i, colors.hue2rgb((i*4+self._step)%256))
	self._step += amt


#Now try with LEDStrip
led = LEDMatrix(driver)

try:
    anim = BasicAnimTest(led)
    anim.run(fps=50)
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()
