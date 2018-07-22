import cv2 
import numpy as np 
img = cv2.imread('result.png',0)
print (img.shape) 
ret,thresh = cv2.threshold(img,127,255,0)
contours = cv2.findContours(thresh, 1, 2) 
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[1500]
x,y,w,h = cv2.boundingRect(cnt) 
print(x, y, w, h) 
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
crop_img = img[y:y+h, x:x+w] 
cv2.imshow("Crop", crop_img) 
cv2.waitKey(0)
