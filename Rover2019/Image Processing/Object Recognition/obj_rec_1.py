import cv2
import numpy as np

image=cv2.imread('test1.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

orb=cv2.ORB_create(1000)

keypoints=orb.detect(gray,None)

keypoints,descriptors=orb.compute(gray,keypoints)
print("keypoints ="+str(len(keypoints)))

imageTest=cv2.drawKeypoints(image,keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,outImage=image)

cv2.imshow('Feature method : ORB',imageTest)
cv2.waitKey()
cv2.destroyAllWindows()
