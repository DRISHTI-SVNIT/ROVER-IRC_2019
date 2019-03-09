from panorama import Stitcher
import argparse
import imutils
import cv2

imageA = cv2.imread("1.jpg")
imageB = cv2.imread("2.jpg")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
 
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
 
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)