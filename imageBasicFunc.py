import cv2
import numpy as np
img=cv2.imread("Resources/me.jpg")
img= cv2.resize(img,(640,500))

#convert it in gray scale
#cvtColor<- convert your color in dif color spaces
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",imgGray)

#blurring Image 
#(7,7)<- kernal size
#0<-sigma
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur image",imgBlur)

#edge detectors-> Canny
#last 2 numbers threshold threshold 
#imgCanny =cv2.Canny(img,100,100)
imgCanny =cv2.Canny(img,150,200)
cv2.imshow("Canny image",imgCanny)

#dilation
#rsolving gaps in edge detection
#by increasing thickness of edges

#user defined matrix 5x5 of ones(8 bits unsighed int)
#so each range from 0 to 255
kernal=np.ones((5,5),np.uint8)

#more iterations more thickness
imgDialation =cv2.dilate(imgCanny,kernal,iterations=1)
cv2.imshow("Dilated image",imgDialation)

#erotion
#opposite of dilation
imgErode =cv2.erode(imgDialation,kernal,iterations=1)
cv2.imshow("Eroded image",imgErode)

cv2.waitKey(0)