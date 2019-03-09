import cv2
import numpy as np

def callback(x):
    pass

def morphing(input_image):
    gray=cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    _,thresh=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    threshErode=cv2.erode(thresh,kernel,iterations=1)
    threshDilate=cv2.dilate(threshErode,kernel,iterations=2)
    return threshDilate

def contoursAndArea(input_image,color_image):
    edged = cv2.Canny(input_image, 30, 200)
    _,cnts,_ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    box=[]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"]>250 :
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(color_image, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(color_image, center, 5, (0, 0, 255), -1)
                cv2.putText(color_image, "("+str(int(x))+","+str(int(y))+")",(int(x+radius),int(y+radius)),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)


cap = cv2.VideoCapture('http://192.168.43.9:8081/?action=stream')
cv2.namedWindow('image')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)

while(cap.isOpened()):

    ret, frame = cap.read()
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    #frame = cv2.bitwise_and(frame, frame, mask=mask)
    frame1 = cv2.bitwise_and(frame, frame, mask=mask)
    filteredMorph=morphing(frame1)
    box=contoursAndArea(filteredMorph,frame)
    '''
    if len(box):
        drawings(frame,box)
    '''
    #cv2.imshow('Filtered image',filteredMorph)
    #cv2.imshow('Edges',edged)
    cv2.imshow('Filtered image',frame1)
    cv2.imshow('image', frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 13 or k == 27:
        break

cap.release()
cv2.destroyAllWindows()