import os

import mediapipe as mp
import cv2
import warnings
import main

warnings.filterwarnings("ignore")

mpPose=mp.solutions.pose
pose=mpPose.Pose()

file_name='img/ywqz1.mp4'
# file_name='img/fwc1.mp4'

def get_coordinate():
    cap = cv2.VideoCapture(file_name)
    lx, ly, hx, hy = 999, 999, 0, 0

    filename_with_extension = os.path.basename(file_name)
    name, _ = os.path.splitext(filename_with_extension)

    lx, ly, hx, hy=main.get_file(name)
    if lx==0:
        lx, ly, hx, hy = 999, 999, 0, 0
    else:
        return int(lx), int(ly), int(hx), int(hy)

    while True:
        success, img = cap.read()
        # print(results[0].pose_landmarks)
        if not success:
            print("视频结束")
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        # print(results)
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
    # print(lx,ly,hx,hy)
    main.write_file_information(name,lx,ly,hx,hy)
    return lx,ly,hx,hy

def detection():
    count = 0
    count_not_standard = 0
    cj = 0  # cj=0 到达最高点  cj=1 到达最低点
    p = 50
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
            # print('h,w',h,w)
            cx = int(results[0].pose_landmarks.landmark[8].x * w)
            cy = int(results[0].pose_landmarks.landmark[8].y * h)
            cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)
            # print('cx', 'cy', cx, cy)
            if cj==0 and lx-p<cx<lx+p and ly-p<cy<ly+p: #到达最低点
                cj=1
            elif cj==1 and hx-p<cx<hx+p and hy-p<cy<hy+p: #到达最高点
                cj=0
                count+=1
            elif cj==1 and lx<cx<lx and ly<cy<ly: #未到达最高点但第二次到达最低点
                count_not_standard+=1
                cj=1
            # elif cj==0 and hx<cx<hx and hy<cy<hy: #为到达最低点但第二次到达最高点
            #     count_not_standard+=1
            #     cj=1

            cx = int(results[0].pose_landmarks.landmark[26].x * w)
            cy = int(results[0].pose_landmarks.landmark[26].y * h)
            cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)
        # cTime=time.time()
        # fps=1/(cTime-ptime)
        # ptime=cTime
        cv2.putText(img,str(count),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
            (255,0,0),3)
        # print(count_not_standard)

        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

    # 存储视频结果
    main.write_results(1,file_name, count, count_not_standard)

# def fuc_detection():


detection()

