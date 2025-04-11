# matrix_6x6
A Pybricks (micropython) module to display text in a 6x6 LED matrix with Pybricks.

It grew up and has now two side modules:
- matrix_6x3 to display text in a 6x3 LED matrix (for those with only 2 ColorLightMatrix
  devices but also for those who want to use 2-port only hubs)
- matrix_6x3_mv specifically for the Move Hub

## WARNING
This is a very early development and I keep changing everything

## Usage

### 6x6 text with 4 ColorLightMatrix devices

Connect them to 4 available ports. With a Technic Hub I arrange them like this:

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

### 6x3 text with only 2 ColorLightMatrix devices

Connect them to 2 available ports. With a Technic Hub I arrange them like this:

      C
      -
      A
but several other combinations are possible.

With a City Hub:

      B
      -
      A

And with a Move Hub:

      D
      -
      C

Import everything from 'matrix_6x3' and initialize an object of class Matrix:

```
from matrix_6x3 import *

matrix = Matrix(Port.A, Port.C)
```

and then use the same methods as above.

If you want to use a Move Hub you have to import 'matrix_6x3_mv' instead:

```
from matrix_6x3 import *

matrix = Matrix(Port.C, Port.D)
```

For now it is exactly the same code, just using an inline font instead of importing it from
other module to preserve memory. See the examples in 'matrix_move.py' but don't expect much:
it is not possible to execute more than one of the larger ones, you will get 'MemoryError'.

[![matrix_6x6 module with Technic Hub](http://img.youtube.com/vi/ZamDMKZNOiE/0.jpg)](https://youtu.be/ZamDMKZNOiE "matrix_6x6 module with Technic Hub")

[![matrix_6x3 module with Technic Hub + City Hub](http://img.youtube.com/vi/CsZQkexFALg/0.jpg)](https://youtu.be/CsZQkexFALg "matrix_6x3 module with Technic Hub + City Hub")

[![matrix_6x3 module with Move Hub](http://img.youtube.com/vi/oaAVnZTQ7lE/0.jpg)](https://youtu.be/oaAVnZTQ7lE "matrix_6x3 module with Move Hub")


It should work with any Pybricks supported LEGO hub with at least 2 ports (Move Hub, City Hub, SPIKE Essentials,
Technic Hub, Robot Inventor or SPIKE and maybe EV3 one day with proper adapters).

Any tuple with two [Pybricks colors](https://docs.pybricks.com/en/latest/parameters/color.html) is supported for ink and paper:
```
(Color.WHITE, Color.BLACK)
```

## Font
Currently only a basic "font" is available:
- a space (an empty sprite)
- digits 0..9
- uppercase letters A..Z
- 3 symbols: !, ? and a smile

Lowercase letters are replaced by their uppercase version and all other symbols are replaced by a space.

## TODO:
- add more representations to the "font" - but do not expect much more to preserve memory... maybe a total of 48 sprites
- perhaps an option for user-defined sprites
- add some sort of "clustering" feature that extends the 6x6 matrix using several hubs and broadcast/observe methods

## FAQ:

Q: Is it possible to use a City Hub?

A: Yes. I just finishing a new class with just 2 ColorLightMatrix in a 6x3 arrangement and a more compact font representation.
But don't expect much for static sprites, 6x3 isn't enough for letters. If you want to display a letter, try displaying it with
an extra space and make it slide:

```
matrix.show(' A', 'L', 250, (Color.YELLOW, Color.BLACK) )
```

our brain will try to compensate for the lack of resolution

Q: Is it possible to use a Move Hub?

A: Yes but with several limitations. I just finished a new class with just 2 ColorLightMatrix and a more compact font
representation and it barely supports 10 digits and 26 letters, leaving no memory for anything else,
you will have to be VERY careful even with the size of your variables.
  
Although I do like to use the Move Hub because it is unexpensive to find and already has 2 motors inside, I don't expect to use
it with memory-intensive and/or math functions.

Please see [Pybricks details on hubs](https://pybricks.com/learn/getting-started/what-do-you-need/) to better understand the
memory differences between the hubs

Q: I have a Technic Hub or even a SPIKE but only have 2 ColorLightMatrix devices. Is it possible to use them?

A: Yes. Use 'matrix_6x3'. not much usefull for displaying static text but sliding text works
almost decently, our brain can compensate quite well the lack of resolution.

Q: I only have 1 [or 3] Color LightMatrix device. Is it possible to use just one [or three]?

A: Nope. Use plain Pybricks code.

Q: I have 6 ColorLightMatrix devices. Can I use them?

A: You're a damm rich guy aren't you? :D I am not 100% sure but I think you can import both modules and instanciate
4 CLMx in a 2x2 arrangement and the other 2 in a 2x1 arrangement. But you want a 3x2 arrangement, right? Nope. Not yet.

It should be easy to extend matrix_6x6 to matrix_6x9 but I don't have any 6-port hub available and I also don't have
6 CLMx so I cannot test it.

And to be honest, I don't see the point, I think 6x6 is enough resolution and the only
reason I see for increasing is for BIG displays and in that case you will never get past 6x9 until LEGO releases a
hub with more ports (I don't believe it will ever happen).

A better approach, if you have the money, is to use several hubs in a cluster. Like 4 Technic Hubs each with 4 CLMx.
I would like to do this but will require to have 4 more CLMx to test it and for the moment I don't want to spend
so much money on such a niche usage.
