"""
'matrix_font.py' is a Pybricks module for displaying
text in a 2x2 arrangement of ColorLightMatrix devices
by JorgePe - https://github.com/JorgePe/matrix_6x6
"""

"""
  The 6x6 Font is formed by a group of sprites,
    a 6x6 grid of pixels were each pixel can
    be 'ink' (1) or 'paper (0)' 
    to reduce memory usage we store each line
    as an integer so a line like:
      0 1 0 0 0 1
    is stored as 17 (17d = 00010001b) 
  A function 'get_sprite' maps an ASCII
    character to it's sprite representation
    or to 'chr_null' (an empty sprite) if there
    isn't one
"""


sp = (000,000,000,000,000,000)

dg = (
    (012,018,018,018,018,012),
    (004,012,004,004,004,014),
    (012,018,002,012,016,030),
    (028,002,012,002,002,028),
    (018,018,018,014,002,002),
    (030,016,028,002,002,030),
    (014,016,028,018,018,014),
    (030,002,002,004,004,008),
    (012,018,012,018,018,012),
    (030,018,030,002,002,028)
)

lt = (
    (028,034,034,062,034,034),  # A
    (060,034,034,060,034,060),  # B
    (030,032,032,032,032,030),  # C
    (060,034,034,034,034,060),  # D
    (062,032,060,032,032,062),  # E
    (062,032,060,032,032,032),  # F
    (030,032,038,034,034,028),  # G
    (034,034,062,034,034,034),  # H
    (062,008,008,008,008,062),  # I
    (062,002,002,034,034,028),  # J
    (034,036,056,056,036,034),  # K
    (032,032,032,032,032,062),  # L
    (034,054,042,034,034,034),  # M
    (034,050,042,042,038,034),  # N
    (028,034,034,034,034,028),  # O
    (060,034,034,060,032,032),  # P
    (028,034,034,042,036,030),  # Q
    (060,034,034,060,036,034),  # R
    (062,032,032,028,002,062),  # S
    (062,008,008,008,008,008),  # T
    (034,034,034,034,034,028),  # U
    (034,034,034,020,020,008),  # V
    (034,034,034,042,054,034),  # W
    (034,020,008,020,034,034),  # X
    (034,034,020,008,008,008),  # Y
    (062,002,004,008,016,062)   # Z
)

ques = (012,018,018,004,000,004)
excl = (004,004,004,004,000,004)
smil = (051,051,000,033,063,030)


def gSprite(c):
    """
    returns a 6x6 representation of c (if supported)
    or sp (space)
    """
    c = c.upper()

    if ord(c) in range( ord('0'), ord('9')+1 ):
        return dg[int(c)]
    elif ord(c) in range(ord('A'), ord('Z')+1):
        return lt[ord(c)- 65]
    elif c == '?':
        return ques
    elif c == '!':
        return excl
    elif c == '@':
        return smil
    else:
        return sp