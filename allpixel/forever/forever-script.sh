#!/bin/bash
/usr/bin/forever start -a --spinSleepTime 1000 -t -c /usr/bin/python /home/ssm/light-modules/allpixel/animations.py --ledcount 169 --animation yellowtwinkle
