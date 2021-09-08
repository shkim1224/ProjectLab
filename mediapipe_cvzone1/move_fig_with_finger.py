import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.65)
#img1 = cv2.imread("F:/2021_2_lecture/ProjectLab2/mediapipe_cvzone1/ImageJPG/1.jpg")
img1 = cv2.imread("F:/2021_2_lecture/ProjectLab2/mediapipe_cvzone1/ImageJPG/1.png",cv2.IMREAD_UNCHANGED)  # png 파일을 그대로 읽어들이라는 명령
ox,oy = 100,100 # image starting point


while True:
    succ, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img ,flipType=False)
    h,w,_ = img1.shape  # 영상을 어레이로 표시할 때 index는 y가 먼저 나옴
    #print(h,w)
    
    if hands:
        lmList = hands[0]['lmList']   # right hand
        #cursor = lmList[8]   # tip of the index finger
        length, info, img = detector.findDistance(lmList[8],lmList[12],img)  # tip of middle finger
        #print(length)
        if length < 60:
            cursor = lmList[8]
            # check if in region
            if ox < cursor[0] < ox+w and oy < cursor[1] < oy+h:  #lmList[0] -> x,  lmList[1] -> y
                # print("inside of image")
                ox,oy = cursor[0]-w//2, cursor[1]-h//2
      
    try:
        # draw jpg Images
        #img[oy:oy+h, ox:ox+w] = img1  # img1을 오리지널 영상에 오버레이 => img[y, x] : 순서 주의!! y comes first
        # draw for png images
        img = cvzone.overlayPNG(img,img1,[ox,oy])
       
        
    except:
        pass
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
    