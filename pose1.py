import mediapipe as mp
import cv2
import warnings
import time

warnings.filterwarnings("ignore")

mpPose=mp.solutions.pose
pose=mpPose.Pose()


ptime=0
count=0
cj=0 #count judge
p=20
# 582 144
# 247 336
file_name='img/ywqz5.mp4'
def get_coordinate():
    cap = cv2.VideoCapture(file_name)
    lx, ly, hx, hy = 999, 999, 0, 0
    while True:
        success, img = cap.read()
        # print(results[0].pose_landmarks)
        if not success:
            print("视频结束")
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results[0].pose_landmarks:
            h, w, c = img.shape
            cx = int(results[0].pose_landmarks.landmark[8].x * w)
            cy = int(results[0].pose_landmarks.landmark[8].y * h)
            cv2.circle(img, (cx, cy), 2, (0, 0, 255), -1)
            # print('cx', 'cy', cx, cy)
            if lx > cx:
                lx = cx
                ly = cy
            elif hx < cx:
                hx, hy = cx, cy
    cap.release()
    return lx,ly,hx,hy


lx, ly, hx, hy = get_coordinate()
cap=cv2.VideoCapture(file_name)
while True:
    success, img = cap.read()
    # print(results[0].pose_landmarks)
    if not success:
        print("视频结束")
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results[0].pose_landmarks:
        h,w,c=img.shape
        print('h,w',h,w)
        cx = int(results[0].pose_landmarks.landmark[8].x * w)
        cy = int(results[0].pose_landmarks.landmark[8].y * h)
        cv2.circle(img, (cx, cy), 2, (0, 0, 255), -1)
        # print('cx', 'cy', cx, cy)
        if lx-p<cx<lx+p and ly-p<cy<ly+p:
            cj=1
        if cj==1 and hx-p<cx<hx+p and hy-p<cy<hy+p:
            cj=0
            count+=1

    cTime=time.time()
    fps=1/(cTime-ptime)
    ptime=cTime
    cv2.putText(img,str(count),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
        (255,0,0),3)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break

