import cv2

img=cv2.imread("Resources/me.jpg")

#(height,width,depth)
print(f"Before resize {img.shape}")


#(width,height)
imgResize=cv2.resize(img,(300,200))

#(height,width,depth)
print(f"After resize {imgResize.shape}")

#streaching<- does not imporve the quality but increases no of pixels
#(width,height)
imgResizeMore=cv2.resize(imgResize,(1000,500))

#(height,width,depth)
print(f"After resize more {imgResizeMore.shape}")

cv2.imshow("Original",img)
cv2.imshow("After resize",imgResize)
cv2.imshow("After resize streach",imgResizeMore)

cv2.waitKey(0)