import pandas as pd
import cv2
import urllib.request
import numpy as np
import os
from datetime import datetime
import face_recognition

curr_path=os.getcwd()
path = os.path.join(curr_path,"image_folder")
url = 'http://<replace_with_ESP32_IP_Address>:81/stream'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''

images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    file=pd.read_csv(os.path.join(curr_path,"Attendance.csv"))
    if name not in list(file.name):
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        entry = {"name": [f"{name}"],
                 "time": [f"{dtString}"]}
        entry = pd.DataFrame(entry, columns=["name", "time"])
        file = pd.concat([file, entry], ignore_index=True, axis=0)
        if "Unnamed: 0" in file.columns:
            file.drop(['Unnamed: 0'], inplace=True, axis=1)
        file.to_csv(os.path.join(curr_path,"Attendance.csv"))
encodeListKnown = findEncodings(images)
print('Encoding Complete')


while True:

    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
