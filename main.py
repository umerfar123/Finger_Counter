import cv2
import handtracking as ht
import os
import time

pTime = 0
cTime = 0

overlayImages=[]
folderPath='Finger_Images'
path=os.listdir(folderPath)
for i in path:
    image=cv2.imread(f'{folderPath}/{i}')
    overlayImages.append(image)

tracking=ht.handDetector()

cap=cv2.VideoCapture(0)

while True:
    #Capturing Video From your webcam frame by frame
    status,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    #passing each frame to handtracker to track hands plot the 21 joints
    image=tracking.findHands(frame)
    
    #passing the frame to get coordinates of each 21 points in a frame
    landList=tracking.findPosition(frame,draw=False)
    
    #checking how much fingers are open
    tip_ids=[4, 8, 12, 16, 20 ]
    fingers=[]
    if len(landList) != 0:
        #for thumb up checking
        if landList[tip_ids[0]][2:] > landList[tip_ids[0]-1][2:]:
            fingers.append(1)
        else:
            fingers.append(0)
        #for remaining fingers up checking
        for i in range(1,5):
            if landList[tip_ids[i]][2:] < landList[tip_ids[i]-2][2:]:
                fingers.append(1)
            else:
                fingers.append(0)
     
        total_fingers_up=fingers.count(1)        
     
        #calculating fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(image, str(int(fps)), (400,60), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
        
        #displaying predicted inside a rectangle
        cv2.rectangle(image,pt1=(60,360),pt2=(160,450),color=(0,255,0),thickness=-1)
        cv2.putText(image,text=str(total_fingers_up),org=(100,420),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(0,0,0),thickness=3)
        
        #cartoon image changer according to number
        image[0:200,0:200] = cv2.flip(overlayImages[total_fingers_up-1],1)
    
    #displaying the ploted image
    cv2.imshow("Finger Counter",image)
    
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()