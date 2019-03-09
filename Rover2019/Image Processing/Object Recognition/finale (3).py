import numpy as np
import cv2

def callback(x):
    pass

#cv2.namedWindow(windowname,None)
cap=cv2.VideoCapture(0)
cv2.namedWindow('image1')
cv2.namedWindow('image2')
cv2.namedWindow('image3')

if cap.isOpened() :
    ret,frame=cap.read()
   #for blue
    ilowH = 0
    ihighH = 255
    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255

    # create trackbars for color change
    cv2.createTrackbar('lowH1', 'image1', ilowH, 179, callback)
    cv2.createTrackbar('highH1', 'image1', ihighH, 179, callback)

    cv2.createTrackbar('lowS1', 'image1', ilowS, 255, callback)
    cv2.createTrackbar('highS1', 'image1', ihighS, 255, callback)

    cv2.createTrackbar('lowV1', 'image1', ilowV, 255, callback)
    cv2.createTrackbar('highV1', 'image1', ihighV, 255, callback)

     #for green
    ilowH = 0
    ihighH = 255
    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255

    # create trackbars for color change
    cv2.createTrackbar('lowH2', 'image2', ilowH, 179, callback)
    cv2.createTrackbar('highH2', 'image2', ihighH, 179, callback)

    cv2.createTrackbar('lowS2', 'image2', ilowS, 255, callback)
    cv2.createTrackbar('highS2', 'image2', ihighS, 255, callback)

    cv2.createTrackbar('lowV2', 'image2', ilowV, 255, callback)
    cv2.createTrackbar('highV2', 'image2', ihighV, 255, callback)

    #for red
    ilowH = 0
    ihighH = 255
    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255

    # create trackbars for color change
    cv2.createTrackbar('lowH3', 'image3', ilowH, 179, callback)
    cv2.createTrackbar('highH3', 'image3', ihighH, 179, callback)

    cv2.createTrackbar('lowS3', 'image3', ilowS, 255, callback)
    cv2.createTrackbar('highS3', 'image3', ihighS, 255, callback)

    cv2.createTrackbar('lowV3', 'image3', ilowV, 255, callback)
    cv2.createTrackbar('highV3', 'image3', ihighV, 255, callback)




else:
    ret=False

while ret:
    ret,frame=cap.read()
    ilowH1 = cv2.getTrackbarPos('lowH1', 'image1')
    ihighH1 = cv2.getTrackbarPos('highH1', 'image1')
    ilowS1 = cv2.getTrackbarPos('lowS1', 'image1')
    ihighS1 = cv2.getTrackbarPos('highS1', 'image1')
    ilowV1 = cv2.getTrackbarPos('lowV1', 'image1')
    ihighV1 = cv2.getTrackbarPos('highV1', 'image1')

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low1=np.array([ilowH1,ilowS1,ilowV1])
    high1=np.array([ihighH1,ihighS1,ihighV1])

    img_mask1=cv2.inRange(hsv,low1,high1)

    output1=cv2.bitwise_and(frame,frame,mask=img_mask1)

    #gray = cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)
    edged1 = cv2.Canny(output1, 30, 200)
    k, contours1, hierarchy = cv2.findContours(edged1.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours1:
        area1 = cv2.contourArea(c)
        print(str(area1) + "\n")
        if (area1 > 1000):
            # box[0], box[1], box[2], box[3] = cv2.boundingRect(c)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            t=int(((2*x+w)/2))
            m=int((y+h/2))
            cv2.putText(frame,'blue',(t,m),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2,cv2.LINE_AA)


    cv2.imshow("image1",output1)
    ilowH2 = cv2.getTrackbarPos('lowH2', 'image2')
    ihighH2 = cv2.getTrackbarPos('highH2', 'image2')
    ilowS2 = cv2.getTrackbarPos('lowS2', 'image2')
    ihighS2 = cv2.getTrackbarPos('highS2', 'image2')
    ilowV2 = cv2.getTrackbarPos('lowV2', 'image2')
    ihighV2 = cv2.getTrackbarPos('highV2', 'image2')

    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low2 = np.array([ilowH2, ilowS2, ilowV2])
    high2 = np.array([ihighH2, ihighS2, ihighV2])

    img_mask2 = cv2.inRange(hsv, low2, high2)

    output2 = cv2.bitwise_and(frame, frame, mask=img_mask2)
    cv2.imshow("image2",output2)
    edged2 = cv2.Canny(output2, 30, 200)
    k, contours2, hierarchy = cv2.findContours(edged2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours2:
        area2 = cv2.contourArea(c)
        print(str(area2) + "\n")
        if (area2 > 1000):
            # box[0], box[1], box[2], box[3] = cv2.boundingRect(c)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            t = int(((2 * x + w) / 2))
            m = int((y + h / 2))
            cv2.putText(frame, 'red', (t, m), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

    ilowH3 = cv2.getTrackbarPos('lowH3', 'image3')
    ihighH3 = cv2.getTrackbarPos('highH3', 'image3')
    ilowS3 = cv2.getTrackbarPos('lowS3', 'image3')
    ihighS3 = cv2.getTrackbarPos('highS3', 'image3')
    ilowV3 = cv2.getTrackbarPos('lowV3', 'image3')
    ihighV3 = cv2.getTrackbarPos('highV3', 'image3')

   # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low3 = np.array([ilowH3, ilowS3, ilowV3])
    high3 = np.array([ihighH3, ihighS3, ihighV3])

    img_mask3 = cv2.inRange(hsv, low3, high3)

    output3 = cv2.bitwise_and(frame, frame, mask=img_mask3)
    edged3 = cv2.Canny(output3, 30, 200)
    k, contours3, hierarchy = cv2.findContours(edged3.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours3:
        area3 = cv2.contourArea(c)
        print(str(area3) + "\n")
        if (area3 > 1000):
            # box[0], box[1], box[2], box[3] = cv2.boundingRect(c)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            t = int(((2 * x + w) / 2))
            m = int((y + h / 2))
            cv2.putText(frame, 'yellow', (t, m), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("image3",output3)
    #cv2.imshow("draw2",output2)
    cv2.imshow("draw",frame)

  #  cv2.imshow("track",output)
    if(cv2.waitKey(1)==27):
        break

cv2.destroyAllWindows()
cap.release()