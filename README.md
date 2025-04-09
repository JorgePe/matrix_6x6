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
- add more representations to the "font" - but do not expect much more, according to my tests the Technic Hub have only
  enough memory for ~64 sprites and only if using short strings, so maybe a total of 48 sprites...
- reduce memory usage of the font representation (considering a list of 6 bytes instead of a list of 6 lists of 6 chars
  but will require some intermediate functions)
- perhaps an option for 1 or 2 user-defined sprites
- add some sort of "clustering" feature that extends the 6x6 matrix using several hubs and broadcast/observe methods

## FAQ:

Q: Is it possible to use a City Hub or even a BOOST Move Hub?

A: Not really. Both hubs have only 2 free ports (A and B on City Hub, C and D on Move Hub) and I tried a version of my module
with just two ColorLightMatrix in a 6x3 arrangement:
- the Move Hub has not enough memory, had to reduce variable and function
names and use a font with just 10 sprites (digits) to achieve installation... and when the code runs it fails with a memory
error
- the City Hub did worked with the above cripled version so I tried the whole font... not enough memory; the best I could use was
  a 10 digit + 22 letters font
  
Although I do like to use the Move Hub because it is unexpensive to find and already has 2 motors inside, I don't expect to use
it with memory-intensive and/or math functions. I also don't like use the City Hub - it's expensive and has not enough performance
to justify it in my projects, except for it's small size. I prefer to use the Technic Hub: is much more powerfull and I can still
can buy it for a small cost.

Please see [Pybricks details on hubs](https://pybricks.com/learn/getting-started/what-do-you-need/) to better understand the
memory differences between the hubs


