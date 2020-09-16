import cv2

img=cv2.imread("Resources/rez_me.jpg")

print(f"Before cropping {img.shape}")

#[rows,cols] or [height,weight]
imgCropped=img[0:200,0:200]

print(f"After cropping {imgCropped.shape}")

cv2.imshow("Original",img)
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)
