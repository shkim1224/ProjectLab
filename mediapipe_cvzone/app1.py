"""
이 프로그램을 수행하기 위해서는 가상환경(tensorflow1)에서 pip install cvzone 을 수행하여 cvzone 패키지를 인스톨해야 함
jupyter notebook을 사용하려면 python버전이 3.6 - 3.7 // 3.9에서는 동작않됨!!!
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
# anaconda3/envs/tensorflow2/Lib/site-packages/cvzone 폴더에 있는 HandTrackingModule.py(모쥴)에서 정의된 HandDetector클래스를 사용하겠다는 의미임
# pip install cvzone 하여 설치한 cvzone.HandTrackingModule.py에는 findPosition이라는 method가 없음
# https://www.analyticsvidhya.com/blog/2021/07/building-a-hand-tracking-system-using-opencv/
# 상기의 사이트에서 def findPostion(_) method를 카피하여 HandTrackingmodule.py에 복사

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
colorR = (255,0,255)
cx,cy,w,h = 100,100,200,200

detector = HandDetector(detectionCon=0.8)
while True:
    succ, img = cap.read()
    img = cv2.flip(img,1)
    _,img = detector.findHands(img)
    lmList = detector.findPosition(img)
    
    if lmList:
        point1 = lmList[8][1], lmList[8][2]  #( first, second) { } [  ]
        point2 = lmList[12][1], lmList[12][2]
        print(lmList)
        #print(point1, point2)
        len,_,_ = detector.findDistance(point1,point2,img)
        #print(len)
        cursor = lmList[8]
        #print(cursor)
        #print(img.shape)
        if len <100:
            
            if cx-w//2 < cursor[1] < cx+w//2 and cy-h//2 < cursor[2] < cy+h//2:
                colorR = (0,255,0)
                print(colorR)
                cx,cy=cursor[1] , cursor[2]
            else:
                colorR = (255,0,255)
            
    cv2.rectangle(img,(cx-w//2,cy-h//2),(cx+w//2,cy+h//2),colorR,cv2.FILLED)
    cv2.imshow("Image",img)
    
    cv2.waitKey(1)
    

