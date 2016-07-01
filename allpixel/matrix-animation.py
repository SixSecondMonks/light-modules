#load the AllPixel driver. Works for LEDStrip AND LEDMatrix
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.drivers.serial_driver import *
from bibliopixel.drivers.visualizer import *

#display constants
matrixwidth = 10
matrixheight = 5

# Set up driver and LED strip
driver = DriverSerial(num = matrixwidth * matrixheight, type = LEDTYPE.WS2812B)
# driver = DriverVisualizer(width = matrixwidth, height = matrixheight)
# Now try with LEDStrip
# led = LEDStrip(driver)
led = LEDMatrix(driver, 10, 5)


class MatrixTest(BaseMatrixAnim):
    def __init__(self, led):
        #The base class MUST be initialized by calling super like this
        super(MatrixTest, self).__init__(led)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
# 	    self.rainbowLines(amt)
# 		self.whiteBoxes(amt)
		self.whiteDot(amt)
        
    def rainbowLines(self, amt): 
        for i in range(self.height):
    	    self._led.drawLine(0, i, self.width, i, self._colors[(self._step + i) % len(self._colors)])
        #Fill the strip, with each sucessive color
#         for i in range(self._led.numLEDs):
#             self._led.drawRect(-1, -1, i+1, i+1, self._colors[(self._step + i) % len(self._colors)])
        #Increment the internal step by the given amount
        self._step += amt	    
        
    def whiteBoxes(self, amt): 
        for i in range(self.height):
            self._led.drawRect(i, i, self.width - i, self.height - i, self._colors[(self._step + i) % len(self._colors)])    
        self._step += amt  
    
    def whiteDot(self, amt):
	    for i in range(self.height):
	    	for j in range(self.width):
	    		self._led.set(i,j,colors.White)    
	    self._step += amt
        
        
try:
    anim = MatrixTest(led)
    anim.run(fps=2)
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()