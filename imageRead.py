import cv2

img=cv2.imread("Resources/me.jpg")
#img=cv2.imread("Resources/me.jpg",0) <-black and white
#img=cv2.imread("Resources/me.jpg",1) <-colored
#img=cv2.imread("Resources/me.jpg",-1) <-transparency factor
#img is an image object

#(width,height)
new_img=cv2.resize(img,(500,500))

cv2.imshow("Output",new_img)

#adding some delay
#0 <- infinite delay, when we press x then close only
#____<- delay in miliseconds

cv2.waitKey(0)

cv2.imwrite("Resources/rez_me.jpg",new_img)