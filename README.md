# matrix_6x6
A Pybricks (micropython) module to display text in a 6x6 LED matrix with Pybricks

## WARNING
This is a very early development and will probably keep changing it

## Usage
Using 4 Color LightMatrix devices in 4 ColorLightMatrix devices connected to
Ports A, B, C and D like this:

        D | C
        - - -
        B | A

Import everything from 'matrix_6x6' and initialize an object of class Matrix:

```
from matrix_6x6 import *

matrix = Matrix(Port.A, Port.B, Port.C, Port.D)
```

then to display a single character:
```
matrix.show('A', 'N', 100, (Color.WHITE, Color.BLACK) )
```
this will show a static 'A' for 100 ms with white ink (ON) pixels over black paper (OFF)

and to display a string:
```
matrix.show('Hello', 'L', 100, (Color.YELLOW, Color.BLACK) )
```
this will show 'Hello', scrolling each character to left with a pause of 100 ms between each
pixel rotation, using yellow pixels over black (OFF)

See 'matrix.py' for a few more examples

[![Displaying text with Technic Hub](http://img.youtube.com/vi/mf9VUIu9txE/0.jpg)](https://youtu.be/mf9VUIu9txE "Displaying text with Technic Hub")

It should work with any Pybricks supported LEGO hub with at least 4 ports (Technic Hub, Robot Inventor or SPIKE and maybe EV3 one day).

Any tuple with two [Pybricks colors](https://docs.pybricks.com/en/latest/parameters/color.html) is supported for ink and paper:
```
(Color.WHITE, Color.BLACK)
```

## Font
Currently only a basic "font" is available:
- digits 0..9
- uppercase letters A..Z
- 3 symbols: !, ? and a smile

Lowercase letters are replaced by their uppercase version and all other symbols are replaced by a space (an empty 6x6 sprite).

## TODO:
- reduce memory usage of the font representation [ALMOST DONE - using a list of 6 bytes instead of a list of 6 lists of 6 chars)
- implement a 6x3 class with just 2 ColorLightMatrix devices [ALMOST DONE]
- add more representations to the "font" - but do not expect much more to preserve memory... maybe a total of 48 sprites
- perhaps an option for user-defined sprites
- add some sort of "clustering" feature that extends the 6x6 matrix using several hubs and broadcast/observe methods

## FAQ:

Q: Is it possible to use a City Hub?

A: Yes. I am just finishing a new class with just 2 ColorLightMatrix in a 6x3 arrangement and a more compact font representation.
But don't expect much for static sprites, 6x3 isn't enough for letters.

Q: Is it possible to use a Move Hub?

A: Yes but with several limitations. I am just finishing a new class with just 2 ColorLightMatrix and a more compact font
representation and also just a subset of the font with 10 digits.

The Move Hub has not enough memory for more and even with just 10 digits you will have to be careful with the size of your variables.
  
Although I do like to use the Move Hub because it is unexpensive to find and already has 2 motors inside, I don't expect to use
it with memory-intensive and/or math functions.

Please see [Pybricks details on hubs](https://pybricks.com/learn/getting-started/what-do-you-need/) to better understand the
memory differences between the hubs

Q: Is it possible to use just 2 ColorLightMatrix devices?

A: It will be possible very soon, in a 6x3 arrangement; not much usefull for displaying static text but scrolling text works
almost decently, our brain can compensate quite well the lack of resolution.
