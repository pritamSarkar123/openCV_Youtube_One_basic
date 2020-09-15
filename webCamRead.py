import cv2

#0<-default camera id
# otherwise provide another ID
cap=cv2.VideoCapture(0)
cap.set(3,640) #width id 3
cap.set(4,480) #height id 4
cap.set(10,100) #brightness id 10

#Now need to show it 
#Video is sequence of Images
while True:
    success,img=cap.read()
    #done succesfully?(bool),captured image=...
    cv2.imshow("Video",img)
    
    #adding delay and loop breaker key
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break