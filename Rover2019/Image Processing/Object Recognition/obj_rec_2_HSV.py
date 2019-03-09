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
    for c in cnts :
        area=cv2.contourArea(c)
        print(str(area)+"\n")
        if(area>5000):
            #box[0], box[1], box[2], box[3] = cv2.boundingRect(c)
            x1,y1,x2,y2=cv2.boundingRect(c)
            cv2.rectangle(color_image, (x1, y1), (x2, y2), (255,0,0), 2)
            '''
            minRect=cv2.minAreaRect(c)

            #box = cv2.BoxPoints(minRect)
            box=cv2.boxPoints(minRect)
            box = np.int0(box)
            '''
    return box

def drawings(input_image,x1,y1,x2,y2):
    #cv2.drawContours(input_image,[box],0,(0,0,255),2)
    x1=box[0]
    y1=box[1]
    x2=box[2]
    y2=box[3]
    cv2.rectangle(input_image, (x1, y1), (x2, y2), (255,0,0), 2)

cap = cv2.VideoCapture(0)
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

while(True):

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

    frame = cv2.bitwise_and(frame, frame, mask=mask)
    filteredMorph=morphing(frame)
    box=contoursAndArea(filteredMorph,frame)
    '''
    if len(box):
        drawings(frame,box)
    '''
    cv2.imshow('Filtered image',filteredMorph)
    #cv2.imshow('Edges',edged)
    cv2.imshow('image', frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 13 or k == 27:
        break

cap.release()
cv2.destroyAllWindows()