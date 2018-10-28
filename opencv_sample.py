import cv2

cap = cv2.VideoCapture(0)

before = None
while True:
    #  OpenCVでWebカメラの画像を取り込む
    ret, frame = cap.read()

    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)
     # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()