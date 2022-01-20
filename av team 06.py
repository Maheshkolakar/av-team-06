import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                print("warning")
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                 # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            cv2.rectangle(img, (20, 250), (148, 200), (0,255,0), cv2.FILLED)
            cv2.putText(img, str("WARNING"), (18,240),cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 4)
    else:
            cv2.rectangle(img, (20, 250), (160, 200), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str("NO-HAND"), (18, 240), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 4)
            print("No - Hand is Detected")
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
