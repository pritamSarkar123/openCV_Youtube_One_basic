import cv2
import numpy as np
imgBlack=np.zeros((512,512))
imgColor0=np.zeros((512,512,3),np.uint8)
cv2.line(imgColor0,(0,0),(imgColor0.shape[1],imgColor0.shape[0]),(0,255,0),3)
cv2.rectangle(imgColor0,(0,0),(250,350),(0,0,255),2)
cv2.circle(imgColor0,(400,50),30,(255,255,0),5)


#text
#(image,"Text",starting point(w,h),style,scale(can be decimal),color(BGR),thickness)
cv2.putText(imgColor0,"Pritam",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)


cv2.imshow("Image Colot R,G,B=0",imgColor0)
cv2.imshow("Image Black",imgBlack)
cv2.waitKey(0)
