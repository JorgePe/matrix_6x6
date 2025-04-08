"""
'matrix_6x6.py' is a Pybricks module for displaying
text in a 2x3 arragement of ColorLightMatrix devices
by JorgePe - https://github.com/JorgePe/matrix_6x6
"""

from pybricks.pupdevices import ColorLightMatrix
from pybricks.parameters import Color, Port
from pybricks.tools import wait


class Matrix:
    def __init__(self, port1, port2, port3, port4):
        self.ports = (port1, port2, port3, port4)
        self.clmatrix1 = ColorLightMatrix(port1)
        self.clmatrix2 = ColorLightMatrix(port2)
        self.clmatrix3 = ColorLightMatrix(port3)
        self.clmatrix4 = ColorLightMatrix(port4)
        self.clm_array = (self.clmatrix1, self.clmatrix2, self.clmatrix3, self.clmatrix4)

    pixels_off=[Color.BLACK]*9

    def clear(self):
        for clmatrix in self.clm_array:
            clmatrix.on(self.pixels_off)

    def get_colored_pixels(self, l, colors):
        # l is a list of 9 pixel values (0/1)
        # returns a list of 9 color values
        # as used in ColorLightMatrix class
        # (ink, paper) are color values for ON/OFF

        (ink, paper) = colors
        colored_pixels = []
        for i in l:
            if i == 1:
                colored_pixels.append(ink)
            else:
                colored_pixels.append(paper)
        return colored_pixels

    def split(self, sprite):
        """
        splits a 6x6 sprite in 4 patterns of 3x3 pixels
        using this arrangement
        D | C
        - - -
        B | A
        each pattern is a list of 12 pixels (0/1, not colors)
        """
        patternD = sprite[0][0:3] + sprite[1][0:3] + sprite[2][0:3]
        patternC = sprite[0][3:6] + sprite[1][3:6] + sprite[2][3:6]
        patternB = sprite[3][0:3] + sprite[4][0:3] + sprite[5][0:3]
        patternA = sprite[3][3:6] + sprite[4][3:6] + sprite[5][3:6]

        return( (patternA, patternB, patternC, patternD) )

    def show(self, s, direction, pause, colors ):
        """
        displays a string (s) scrolling it to Left/Right/None
        with a pause between each scrolling movement

        s can also be a single char

        direction = 'L' or 'R' or 'N'
        pause in ms
        colors is a tupple with (ink, paper) color values
        """

        size = len(s)

        # create a grid of pixels
        # to store the sprites that represent each
        # char in the string and an extra empty char
        # before/after last char (depending on direction)

        width = 6*(size+1)
        heigth = 6
        grid = [[0 for x in range(width)] for y in range(heigth)] 

        if direction == 'L':
            # to scroll 'Left' add empty char at the end
            index = 0
        elif direction == 'R':
            # to scroll 'Right' add empty char at the beginning
            # so will start filling the grid at column 6
            index = 6
        elif direction == 'N':
            # do not scroll
            index = 0
        else:
            return

        for i in range(0,size):
            # gets each char 6x6 representation
            # and insert in the grid
            sprite = get_representation(s[i])
            for line in range(0,6):
                for col in range(0,6):
                    grid[line][index + col + 6*i] = sprite[line][col]

        # uses a sliding window to display
        # a 6x6 subset block of the whole grid
        block = chr_null
        if direction == 'L':
            # start the sliding window from left
            # and increase position
            start = 0
            end = size*6+1
            incr = 1
        elif direction == 'R':
            # start the sliding window from right
            # and decrease position
            start = size*6
            end = -1
            incr = -1
        else:
            # no sliding window
            start = 0
            end = 1
            incr = 1

        for i in range(start, end, incr):
            for line in range(0,6):
                for col in range(0,6):
                    block[line][col] = grid[line][col+i]

            # split block in 4 patterns
            (patternA, patternB, patternC, patternD) = self.split(block)

            # display each pattern on each ColorLightMatrix
            for (clmatrix, pattern) in zip(self.clm_array, (patternA, patternB, patternC, patternD)):
                clmatrix.on(self.get_colored_pixels(pattern, colors) )

            wait(pause)

"""
  The 6x6 Font is formed by a group of sprites,
    each represented by a list of lists forming
    a 6x6 array with just 1 or 0 as values:
      1 = 'ink' 
      0 = 'paper'
  A function 'get_representation' maps an ASCII
    character to it's sprite representation
    or to 'chr_null' (an empty sprite) if there
    isn't one
"""

chr_null = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

chr_0 = [
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,0]
]

chr_1 = [
    [0,0,0,1,0,0],
    [0,0,1,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,1,1,1,0]
]

chr_2 = [
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,1,1,0,0],
    [0,1,0,0,0,0],
    [0,1,1,1,1,0]
]

chr_3 = [
    [0,1,1,1,0,0],
    [0,0,0,0,1,0],
    [0,0,1,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_4 = [
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0]
]

chr_5 = [
    [0,1,1,1,1,0],
    [0,1,0,0,0,0],
    [0,1,1,1,0,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,1,1,1,1,0]
]

chr_6 = [
    [0,0,1,1,1,0],
    [0,1,0,0,0,0],
    [0,1,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,1,0]
]

chr_7 = [
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,1,0,0,0]
]

chr_8 = [  
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,1,0,0]
]

chr_9 = [
    [0,1,1,1,1,0],
    [0,1,0,0,1,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_A = [
    [0,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0]
]

chr_B = [
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,0]
]

chr_C = [
    [0,1,1,1,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,1,1,1,1,0]
]

chr_D = [
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,0]
]

chr_E = [
    [1,1,1,1,1,0],
    [1,0,0,0,0,0],
    [1,1,1,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,1,1,1,1,0]
]

chr_F = [
    [1,1,1,1,1,0],
    [1,0,0,0,0,0],
    [1,1,1,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0]
]

chr_G = [
    [0,1,1,1,1,0],
    [1,0,0,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_H = [
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0]
]

chr_I = [
    [1,1,1,1,1,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [1,1,1,1,1,0]
]

chr_J = [
    [1,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_K = [
    [1,0,0,0,1,0],
    [1,0,0,1,0,0],
    [1,1,1,0,0,0],
    [1,1,1,0,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,0]
]

chr_L = [
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [1,1,1,1,1,0]
]

chr_M = [
    [1,0,0,0,1,0],
    [1,1,0,1,1,0],
    [1,0,1,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0]
]

chr_N = [
    [1,0,0,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,0,1,0],
    [1,0,1,0,1,0],
    [1,0,0,1,1,0],
    [1,0,0,0,1,0]
]

chr_O = [
    [0,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_P = [
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0]
]

chr_Q = [
    [0,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,1,0,1,0],
    [1,0,0,1,0,0],
    [0,1,1,1,1,0]
]

chr_R = [
    [1,1,1,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,1,1,1,0,0],
    [1,0,0,1,0,0],
    [1,0,0,0,1,0]
]

chr_S = [
    [1,1,1,1,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,1,1,1,0,0],
    [0,0,0,0,1,0],
    [1,1,1,1,1,0]
]

chr_T = [
    [1,1,1,1,1,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0]
]

chr_U = [
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
]

chr_V = [
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,0,1,0,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0]
]

chr_W = [
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [1,0,1,0,1,0],
    [1,1,0,1,1,0],
    [1,0,0,0,1,0]
]

chr_X = [
    [1,0,0,0,1,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0],
    [0,1,0,1,0,0],
    [1,0,0,0,1,0],
    [1,0,0,0,1,0]
]

chr_Y = [
    [1,0,0,0,1,0],
    [1,0,0,0,1,0],
    [0,1,0,1,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0]
]

chr_Z = [
    [1,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,1,1,0]
]

chr_question = [
    [0,0,1,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,1,0,0]
]

chr_exclam = [
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,1,0,0]
]

chr_smile = [
    [1,1,0,0,1,1],
    [1,1,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [1,1,1,1,1,1],
    [0,1,1,1,1,0]
]

digits = [chr_0, chr_1, chr_2, chr_3, chr_4, chr_5, chr_6, chr_7, chr_8, chr_9]

letters = [
    chr_A, chr_B, chr_C, chr_D, chr_E, chr_F,
    chr_G, chr_H, chr_I, chr_J, chr_K, chr_L,
    chr_M, chr_N, chr_O, chr_P, chr_Q, chr_R,
    chr_S, chr_T, chr_U, chr_V, chr_W, chr_X,
    chr_Y, chr_Z
]

def get_representation(c):
    """
    returns 6x6 representation of c (if supported)
    or chr_null
    """
    if c in '0123456789':
        return digits[int(c)]
    elif ord(c) in range(ord('A'), ord('Z')+1):
        return letters[ord(c)- 65]
    elif ord(c) in range(ord('a'), ord('z')+1):
        return letters[ord(c)- 97]
    elif c == '?':
        return chr_question
    elif c == '!':
        return chr_exclam
    elif c == '@':
        return chr_smile
    else:
        return chr_null