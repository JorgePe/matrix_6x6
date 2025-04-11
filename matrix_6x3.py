"""
'matrix_6x3.py' is a Pybricks module for displaying
text in a 2x1 arrangement of ColorLightMatrix devices
by JorgePe - https://github.com/JorgePe/matrix_6x6

most variable names are short to reduce memory usage
"""

from pybricks.pupdevices import ColorLightMatrix
from pybricks.parameters import Color, Port
from pybricks.tools import wait

from matrix_font import *


"""
    using this arrangement:
     2
     -
     1
    (each number denotes a ColorLightMatrix device)
"""

class Matrix2x1:

    def __init__(self, port0, port1):
#        self.clmatrix1 = ColorLightMatrix(port0)
#        self.clmatrix2 = ColorLightMatrix(port1)
#        self.clm_array = (self.clmatrix1, self.clmatrix2)
        self.clm0 = ColorLightMatrix(port0)
        self.clm1 = ColorLightMatrix(port1)    

    def clear(self):
        """
        turns off all LEDs in the 2x1 arrangement
        """
        self.clm0.off()
        self.clm1.off()            

    def gLeds(self, l, c):
        """
        l: a list of 9 values (0/1)
        s: a tuple of 2 colors (ink, paper)
        returns a list of 9 color values
        as used in ColorLightMatrix class
        """

        (ink, pap) = c
        leds = []
        for i in l:
            if i == 1:
                leds.append(ink)
            else:
                leds.append(pap)
        return leds

    def sprite(self, s, c):
        """
        s: a list of 6 integers representing a 6x6 sprite
        c: a tuple of 2 colors (ink, paper)
        """

        """
        sprite is meant for a 2x2 ColorLightMatrix arrangement
            UL | UR
            -------
            BL | BR        
        since we only have a 2x1 arrangement:
         - extract UR and BR parts
         - convert each to a list of 9 values (1/0)
         - replace 1/0 by ink/paper colors
         - display each part on each ColorLightMatrix
        """

        ur = [ s[0] & 0x07 , s[1] & 0x07 , s[2] & 0x07 ]
        br = [ s[3] & 0x07 , s[4] & 0x07 , s[5] & 0x07 ]

        # converts each value to its 3-bit binary representation
        # split in a list of 3
        # then combines the 3 lists in one list of 9
        lUp = [int(x) for x in '{:03b}'.format(ur[0])] + \
            [int(x) for x in '{:03b}'.format(ur[1])] + \
            [int(x) for x in '{:03b}'.format(ur[2])]

        lBt = [int(x) for x in '{:03b}'.format(br[0])] + \
            [int(x) for x in '{:03b}'.format(br[1])] + \
            [int(x) for x in '{:03b}'.format(br[2])]

        self.clm0.on(self.gLeds(lBt, c))
        self.clm1.on(self.gLeds(lUp, c))


    def show(self, s, d, p, cls ):
        """
        s: a string or a char
        d: direction
        p: pause in ms
        cls: a tuple of 2 colors (ink, paper)

        shows the sprites for s
        sliding to Left/Right/None
        with a pause between each motion
        """

        if d == 'N':
            # just show first char of the string 
            self.sprite(gSprite(s[0]), cls)
        else:
            # create a grid for storing the representations
            # of the char we are going to show and of the next one

            # using a list of 6 integers and bitwise operations
            grid = [0 for y in range(6)]

            if len(s) == 1:
            # if just one char add a space to allow sliding
                s = s[0] + ' '
          
            for i in range(0, len(s)-1):
                # for each character in string and the next one
                # get representation and insert in grid
                s1 = gSprite(s[i])
                s2 = gSprite(s[i+1])

                # 'Left': first char at left and second char at right
                # 'Right': put first char at right and second char at left

                for l in range(0,6):
                    # for each line in grid
                    # insert a bitwise combination of the two sprites
                    if d == 'L':
                        # to slide left
                        # shift firts sprite leftmost and second sprite after
                        grid[l] = (s1[l] << 11) | (s2[l] << 5)
                    else:
                        # to slide right
                        # shift second sprite to be at left of the first
                        grid[l] = s1[l] | (s2[l] << 6)

                # sliding window
                # get a 6x6 block sample of the grid to be shown
                for column in range(0,6,):
                    block = [0,0,0,0,0,0]

                    for l in range(0,6):
                        if d == 'L':
                            block[l] = ((grid[l] << column) & 0xFC00) >> 10
                        else:
                            block[l] = ((grid[l] >> column) & 0x003F)

                    self.sprite(block, cls)
                    wait(p)
