# coding: utf-8
import cv2
import csv

f = open('opencv.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
cap = cv2.VideoCapture(0)
#カスケードファイルの読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


before = None
while True:
    #  OpenCVでWebカメラの画像を取り込む
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        #顔部分を四角で囲う
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        writer.writerow([x,y])

    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)
     # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()



#カスケードファイルと使って顔認証
