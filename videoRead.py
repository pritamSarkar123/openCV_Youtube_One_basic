import cv2

cap=cv2.VideoCapture("Resources/ravana.mp4")

#Now need to show it 
#Video is sequence of Images
while True:
    success,img=cap.read()
    #done succesfully?(bool),captured image=...
    cv2.imshow("Video",img)
    
    #adding delay and loop breaker key
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break