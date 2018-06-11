
# 工程文件说明

![](http://ow7va355d.bkt.clouddn.com/project.png)
　　工程环境 pyqt5 opencv3 python3

## video_to_picture.py


　　该工程文件是提取视频中的帧，将视频按一定是时间间隔提取图片，视频存放在video文件夹中
提取的图片保存在save_image文件夹下，并以 00000.jpg  00001.jpg ...方式命名,图片保存大小为 640X480。


## continuously_take_pictures.py

　　该工程文件，实现功能是打开摄像头，并且能够实现连续拍照，命名方式能够在源工程文件下修改。


## test_camera.py

　　该工程文件用来测试摄像头，cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)　可以设置摄像头的分辨率。


## photo_resize.py

　　该工程文件用来批量将图片，缩放到一定尺寸。