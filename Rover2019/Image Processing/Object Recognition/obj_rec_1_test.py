import cv2
import numpy as np

def ORBDetector(new_image,template_image):
    image1=cv2.cvtColor(new_image,cv2.COLOR_BGR2GRAY)
    orb=cv2.ORB_create(1000)
    kp1,des1=orb.detectAndCompute(image1,None)
    print("kp1 ="+str(len(kp1)))

    kp2,des2=orb.detectAndCompute(template_image,None)
    print("kp2 ="+str(len(kp2)))

    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

    matches=bf.match(des1,des2)

    matches=sorted(matches,key=lambda val: val.distance)

    imageTest=cv2.drawKeypoints(new_image,kp1,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,outImage=new_image)
    cv2.imshow('Feature method : ORB',imageTest)
    '''
    cv2.waitKey()
    cv2.destroyAllWindows()
    '''
    return len(matches)

image_template=cv2.imread('test1.jpg',0)
'''
image_run=cv2.imread('test3 (3).jpg')
print(ORBDetector(image_run, image_template))
'''
cap=cv2.VideoCapture(0)

while True :
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    print(ORBDetector(frame, image_template))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()