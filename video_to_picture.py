import  cv2

video_path = 'video/4k.MOV'
vid_cap = cv2.VideoCapture(video_path)  # 读入视频文件
i = 1
c = 625  # 该常量用来调整数据集的开始命名位置
if vid_cap.isOpened():
    ret, frame = vid_cap.read()
else:
    ret = False
fps = vid_cap.get(cv2.CAP_PROP_FPS)
timeF = 33  # 视频帧频率
print(fps)
while ret:
    ret, frame = vid_cap.read()

    if (i % timeF == 0):  # 每隔timeF帧进行存储操作
        image = cv2.resize(frame, (640, 480))
        cv2.imwrite('save_image/' + str("%05d" % c) + ".jpg", image)
        c = c+1
    i = i+1
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow('video', frame)
    cv2.waitKey(1)
vid_cap.release()