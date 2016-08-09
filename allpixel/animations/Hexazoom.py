#  ## WhiteTwinkle ##
# This Bibliopixel animation randomly picks leds and slowly brightens them to a max brightness
# then dims them to off.
#
# Author: Bob Steinbeiser, based on work by Mark Kriegsman at:
#    https://gist.github.com/kriegsman/99082f66a726bdff7776
#
#  ## Usage ##
#
#  max_led -    The max number of pixels you want used ('None' for all leds)
#  speed   -    How fast the leds bighten then dim (best in range 2-40)
#  density -    The density (or number) of twinkling leds
#  max_bright - The maximum brightness, some leds twinkle better if they ramp to less than full
#                 brightness (19 - 255). Lower brightness also speeds up the twinkle rate.

import time, random
from bibliopixel.animation import *

class HexagonLed:

    def __init__(self, lt=None, rt=None, lm=None, rm=None, rb=None, lb=None):
        self.lt = lt
        self.rt = rt
        self.lm = lm
        self.rm = rm
        self.rb = rb
        self.lb = lb

class HexagonGrid:

    def __init__(self, side_length):

        self.sideLength = side_length
        self.totalPixels = self.calculateTotalPixels()
        self.longestRow = self.calculateLongestRow()
        self.midPoint = self.totalPixels / 2    

    def calculateTotalPixels(self):

        led_total = self.longestRow()

        # add up rest of pixels
        for i in range(1, side):
            both_rows = (self.longestRow() - i) * 2
            led_total = led_total + both_rows

        return led_total        

    def calculateLongestRow(self):
        return (self._hexSideCount * 2) - 1

class Hexazoom(BaseStripAnim):
    """ Zooming hexagon """

    def __init__(self, led, hex_side_count=8, speed=2, max_bright=255):

        super(Hexazoom, self).__init__(led, 0, -1)

        # based on hexagon side size, calculate pixels in use
        self._hexSideCount = hex_side_count
        self._hexPixelCount = self.calculateHexPixels(hex_side_count)
        self._hexMidPoint = self._hexPixelCount / 2 

        # set initial state
        self._current = 0
        self._minLed = 0
        self._maxLed = self._hexPixelCount
        if self._maxLed == None or self._maxLed < self._minLed:
            self._maxLed = self._led.lastIndex
        self.density = 50
        self.speed = speed
        self.max_bright = max_bright

        # If max_bright is even then leds won't ever dim, make it odd
        if (self.max_bright & 1 == 0):
            self.max_bright -= 1

        # If the speed is odd then the leds won't ever brighten, make it even
        if self.speed & 1:
            self.speed += 1

        # Make sure speed, density & max_bright are in sane ranges
        self.speed = min(self.speed, 100)
        self.speed = max(self.speed, 2)
        self.density = min(self.density, 100)
        self.density = max(self.density, 2)
        self.max_bright = min(self.max_bright, 255)
        self.max_bright = max(self.max_bright, 5)

    def longestRow(self):
        return (self._hexSideCount * 2) - 1

    def calculateHexPixels(self, side):

        led_total = self.longestRow()

        # add up rest of pixels
        for i in range(1, side):
            both_rows = (self.longestRow() - i) * 2
            led_total = led_total + both_rows

        return led_total

    def pixelRangeForHexLine(self, offset):

        ledPoints = []

        # automatically return midpoint if offset is zero or less
        if offset <= 0:
            ledPoints.append(self._hexMidPoint)
            return ledPoints
        else:
            # now we'll return the range of numbers
            leftmost_point = self._hexMidPoint - offset
            rightmost_point = self._hexMidPoint + offset

            ledPoints.append(leftmost_point)
            ledPoints.append(rightmost_point)

            pixelOffset = 0
            for o in range(1, offset):
                baseRowCount = self.longestRow() - o
                pixelOffset = pixelOffset + baseRowCount
                ledPoints.append(self._hexMidPoint - (pixelOffset - o))
                ledPoints.append(self._hexMidPoint + pixelOffset + (o-1))

        return ledPoints

    def step(self, amt = 1):

        # midLed = self._hexMidPoint

        self._led.set(self._hexMidPoint, colors.Red)

        for i in self.pixelRangeForHexLine(3):

            self._led.set(i, colors.Blue)
            # if self._step % 2 == 0: 
            #     self._led.set(i, colors.White)
            # else:
            #     self._led.set(i, colors.Black)

        # # The direction of fade is determined by the red value of the led color
        # self.pick_led(self.speed)

        # for i in range(self._maxLed):

        #     this_led = self._led.get(i)
        #     r = this_led[0]

        #     if r == 0:    # skip the black pixels
        #         continue;

        #     # if red is odd darken it, if its even brighten it 
        #     if r & 1: 
        #         self._led.set(i, self.qsub8(this_led, self.speed))
        #     else:
        #         self._led.set(i, self.qadd8(this_led, self.speed))

            #log.logger.info("Led: {0} - {1}".format(i, self._led.get(i)))

        self._step += amt

MANIFEST = [
    {
        "class": Hexazoom, 
        "controller": "strip", 
        "desc": "Wormhole via hexagon", 
        "display": "Random White Twinkling Leds", 
        "id": "WhiteTwinkle", 
        "params": [
            {
                "default": None, 
                "help": "Last pixel index to use. Leave empty to use max index.", 
                "id": "max_led", 
                "label": "Last Pixel", 
                "type": "int"
            }, 
            {
                "default": 2, 
                "help": "Fade up/down speed of the twinkle (best in range of 2-20) (100 max)", 
                "id": "speed", 
                "label": "Fade Speed", 
                "type": "int"
            }, 
            {
                "default": 80, 
                "help": "Density (or number) of the twinkling leds (best in range 40-80) (100 max)", 
                "id": "density", 
                "label": "Twinkling LED Density", 
                "type": "int"
            },
            {
                "default": 255, 
                "help": "Some leds twinkle better at less than full brightness. This also speeds up the twinkle rate. (255 max)", 
                "id": "max_bright", 
                "label": "LED Max Brightness", 
                "type": "int"
            }
        ], 
        "type": "animation"
    }
]