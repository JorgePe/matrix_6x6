from matrix_6x6 import *

matrix = Matrix(Port.A, Port.B, Port.C, Port.D)
pause = 1000

matrix.clear()
wait(pause)

# show a static '1' in White over Black
matrix.show('1', 'N', 0, (Color.WHITE, Color.BLACK) )
wait(pause)

# show a '1' scrolling to Left in Yellow over Black
matrix.show('1', 'L', 250, (Color.YELLOW, Color.BLACK) )
wait(pause)

# show a '1' scrolling to right in Rede over Black
matrix.show('1', 'R', 250, (Color.RED, Color.BLACK) )
wait(pause)

# show the 10 digits, static, in White over Black
for c in '0123456789':
    matrix.show(c, 'N', 0, (Color.WHITE, Color.BLACK) )
    wait(200)

matrix.clear()
wait(pause)

# show a string scrolling to Left in several color combinations
colors = (
    (Color.WHITE, Color.BLACK),
    (Color.YELLOW, Color.BLACK),
    (Color.RED, Color.WHITE),
    (Color.ORANGE, Color.BLUE)
)
for color in colors:
    matrix.show('Python is awesome!', 'L', 50, color)
    wait(pause)

matrix.clear()
wait(pause)

# show a static smile, changing it's colors
for i in range(0,10):
    for color in (Color.WHITE, Color.RED, Color.GREEN, Color.ORANGE, Color.YELLOW):
        matrix.show('@', 'N', 0, (color, Color.BLACK))
        wait(250)

matrix.clear()
