import cv2
import numpy as np
#create a matrix filled with 0(blacks)
#(height,width,depth)
imgBlack=np.zeros((512,512))

#color image (RGB) initialy all R=0,G=0,B=0
#means black
imgColor0=np.zeros((512,512,3),np.uint8)

#Entire Blue color
#Blue=255,0,0
#Green=0,255,0
#Red=0,0,255
###imgColor0[:]=255,0,0

#Partial colored
###imgColor0[200:300,100:300]=255,0,0

#Lines
#(image,start(c,r),end(c,r),(B,G,R),thickness)
###cv2.line(imgColor0,(0,0),(300,300),(0,255,0),3)
cv2.line(imgColor0,(0,0),(imgColor0.shape[1],imgColor0.shape[0]),(0,255,0),3)

#Rectangle
#(image,start(c,r),(width,height),(B,G,R),thickness/OR/cv2.FILLED)
###cv2.rectangle(imgColor0,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.rectangle(imgColor0,(0,0),(250,350),(0,0,255),2)

#Circle
#(center(c,r),radius,(B,G,R),thickness/OR/cv2.FILLED)
cv2.circle(imgColor0,(400,50),30,(255,255,0),5)
###cv2.circle(imgColor0,(400,50),30,(255,255,0),cv2.FILLED)





cv2.imshow("Image Colot R,G,B=0",imgColor0)
cv2.imshow("Image Black",imgBlack)
cv2.waitKey(0)