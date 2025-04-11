# Move Hub with 2x1
from matrix_6x3_mv import *
matrix = Matrix2x1(Port.C, Port.D)

matrix.clear()
wait(1000)

"""
# shows a static '1' in White over Black
matrix.show('1', 'N', 0, (Color.WHITE, Color.BLACK) )

# shows a '1' scrolling to Left in Yellow over Black
matrix.show('1', 'L', 250, (Color.YELLOW, Color.BLACK) )

# shows a '1' sliding right in Red over Black
matrix.show('1', 'R', 500, (Color.RED, Color.BLACK) )
"""

"""
# shows each of the 10 digits, sliding left, in White over Black
for c in '0123456789':
    matrix.show(' ' + c, 'L', 250, (Color.WHITE, Color.BLACK) )
"""

# shows each of the 26 letters, sliding left, in Red over Black
for c in range(ord('A'), ord('Z')+1):
    matrix.show(' ' + chr(c), 'L', 250, (Color.RED, Color.BLACK) )

"""
# shows a string, sliding left, in Yellow over Black
matrix.show(' Hello World! @', 'L', 250, (Color.YELLOW, Color.BLACK))
"""

matrix.clear()
