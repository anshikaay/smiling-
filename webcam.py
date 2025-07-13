import cv2;

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        smiles=smile_cascade.detectMultiScale(roi_gray,scaleFactor=1.7, minNeighbors=20)
        if len(smiles)>0:
            text="Smiling Cutie"
            color=(0,255,0)
        else:
            text="Not Smiling?"
            color=(0,0,255)
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,color,2)

        cv2.imshow("Smile Detetector",frame)

        if cv2.waitKey(1) & 0xFF== ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
        