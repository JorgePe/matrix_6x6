from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor, ColorLightMatrix
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from matrix_6x6 import *

hub = TechnicHub()

# The 4 ColorLightMatrix arrangement:

# D | C
# - - -
# B | A

matrixA = ColorLightMatrix(Port.A)
matrixB = ColorLightMatrix(Port.B)
matrixC = ColorLightMatrix(Port.C)
matrixD = ColorLightMatrix(Port.D)

matrix = (matrixA, matrixB, matrixC, matrixD)

pixels_off=[Color.BLACK]*9

# each char is represented by a 6x6 array



def clear(mtx):
    for m in mtx:
        m.on(pixels_off)


def get_colored_pixels(l, colors):
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



def split(sprite):
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


def show(mtx, sprite, colors):
    """
    mtx is a tupple with 4 ColorLightMatrix
    sprite is a 6x6 array (a list of 6 lists of 6 values)
    forming a 6x6 grid of pixels (0/1)
    """

    # split sprite in 4 patterns
    (patternA, patternB, patternC, patternD) = split(sprite)

    # display each pattern on each ColorLightMatrix
    for (m,p) in zip(mtx, (patternA, patternB, patternC, patternD)):
        m.on(get_colored_pixels(p, colors) )


def showchar(mtx, c, colors):
    """
    displays a char c in a mtx
    mtx is a tupple with 4 ColorLightMatrix
    colors is a tupple with (ink, paper) color values
    """

    sprite = get_representation(c)
    show(mtx, sprite, colors)


def slideshow(mtx, s, direction, pause, colors ):
    """
    display a string s scrolling it to Left/Right
    with a pause between each char in the string
    mtx is a tupple with 4 ColorLightMatrix
    direction = 'L' or 'R'
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
        # for direction 'Left' the empty char is at the end
        index = 0
    else:
        # for direction 'Right' the empty char is at the beginning
        # so will start filling the grid at column 6
        index = 6

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
    else:
        # start the sliding window from right
        # and decrease position
        start = size*6
        end = -1
        incr = -1

    for i in range(start, end, incr):
        for line in range(0,6):
            for col in range(0,6):
                block[line][col] = grid[line][col+i]

        # split block in 4 patterns
        (patternA, patternB, patternC, patternD) = split(block)

        # display each pattern on each ColorLightMatrix
        for (m,p) in zip(mtx, (patternA, patternB, patternC, patternD)):
            m.on(get_colored_pixels(p, colors) )

        wait(pause)



clear(matrix)
wait(1000)

for c in '0123456789':
    showchar(matrix, c, (Color.WHITE, Color.BLACK))
    wait(200)

clear(matrix)    
wait(1000)

colors = (
    (Color.WHITE, Color.BLACK),
    (Color.YELLOW, Color.BLACK),
    (Color.RED, Color.WHITE),
    (Color.GREEN, Color.WHITE),
    (Color.WHITE, Color.BLUE)
)
for c in colors:
    slideshow(matrix, 'Python is awesome!', 'L', 50, c)
    wait(1000)

clear(matrix)

for i in range(0,10):
    for c in (Color.WHITE, Color.RED, Color.GREEN, Color.ORANGE, Color.YELLOW):
        showchar(matrix, '@', (c, Color.BLACK))
        wait(250)

clear(matrix)