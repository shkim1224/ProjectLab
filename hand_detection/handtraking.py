import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()  # mp.solutions.hands.Hands()라는 생성자를 이용하여 hands라는 객제(instance)를 생성함 Hands(default parameters....)
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
while True:
    _, img = cap.read()
    imgRGB = cv2.cvtColor(img,
                          cv2.COLOR_BGR2RGB)  # hands 객체는 RGB 형식을 사용함, 하지만 cap.read()에서는 BGR 타입의 데이터가 나옴, 출력되는 데이터의 순서가 다름
    results = hands.process(imgRGB)  # hands.process()에 imgRGB 영상을 사용함 결과는 results
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h,w,c = img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
                if id==4:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            # mpDraw.draw_landmarks(img, handLms)   # mp.solutions.drawing_utils.draw_landmarks()를 사용하여 손에 landmarks만 표시함
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # landmarks에 선을 연결함

    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    pTime = cTime

    cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
