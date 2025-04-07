# matrix_6x6
A Pybricks (micropython) module to display text in a 6x6 LED matrix with Pybricks

## WARNING
This is a very early development and will probably keep changing it

## Usage
Using 4 Color LightMatrix devices in a 2x2 array to display 6x6 text

```
from pybricks.pupdevices ColorLightMatrix

matrixA = ColorLightMatrix(Port.A)
matrixB = ColorLightMatrix(Port.B)
matrixC = ColorLightMatrix(Port.C)
matrixD = ColorLightMatrix(Port.D)

matrix = (matrixA, matrixB, matrixC, matrixD)
```

To display a single character:
```
showchar(matrix, 'A', (Color.WHITE, Color.BLACK) )
```
this will show 'A' with white ink (ON) pixels over black paper (OFF)

To display a string:
```
slideshow(matrix, 'Hello', 'L', 100, (Color.YELLOW, Color.BLACK) )
```
this will show 'Hello', scrolling each character to left with a pause of 100 ms between each
character, using yellow pixels over black (OFF)

[![Displaying text with Technic Hub](http://img.youtube.com/vi/mf9VUIu9txE/0.jpg)](https://youtu.be/mf9VUIu9txE "Displaying text with Technic Hub")

It should work with any Pybricks supported LEGO hub with at least 4 ports (Technic Hub, Robot Inventor or SPIKE and maybe EV3 one day).

Any tuple with two [Pybricks colors](https://docs.pybricks.com/en/latest/parameters/color.html) is supported for ink and paper:
```
(Color.WHITE, Color.BLACK)
```
