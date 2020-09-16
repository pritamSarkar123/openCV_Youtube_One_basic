# computer vission
## link:-https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=72s

### Intro to images
no of pix in width x no of pix in height
VGA=640x480
HD=1280x720
FHD=1920x1080
4K=3840x2160

black and white:- 
 1. binary image(2 levels)
 2. 6 levels
 3. 16 levels
 4. 8 bit value,resolution of 256 (0-255),to specify intensity of shades of gray
color images:-
 1. 3 color intensity values(each 8 bits) RGB,for each pixel boxes

so colored vga=640x480x3
640 <- columns
480 <- rows
3 <- depth
### installation
## Chapter 1
### Imread
    imageRead.py
### Video capture
    videoRead.py
### webcam
    webCamRead.py
## Chapter 2
### basic finctions
    imageBasicFunc.py
## Chapter 3
### Resizing 
    (0,0)-------640-------->X
    |
    |  "axis"
    |
    480
    |
    v-------------------->(640,480)
    Y
height==rows width ==cols
here:-( row no,column no)
but using numpy we access:-[row no,col no]
img.shape->(height,width,depth)
    imageResize.py
### Cropping
    imgCrop.py

## Chapter 4
### Shapes and texts
    imgShapes.py


