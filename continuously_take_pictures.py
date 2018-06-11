import os
import sys
import threading
import time
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.timer_camera = QTimer()  # 需要定时器刷新摄像头界面
        self.cap = cv2.VideoCapture()
        self.cap_num = 0
        self.set_ui()  # 初始化UI界面
        self.slot_init()  # 初始化信号槽
        self.btn_flag = 0  # 开关变量
        self.input_flag = 0
        self.photo_flag = 0
        self.count = 0

    def set_ui(self):
        # 布局设置
        self.layout_main = QHBoxLayout()  # 整体框架是水平布局
        self.layout_button = QVBoxLayout()  # 按键布局是垂直布局

        # 按钮设置
        self.btn_open_cam = QPushButton('打开相机')
        self.btn_photo = QPushButton('拍照')
        self.btn_photo_1 = QPushButton('连续拍照')
        self.btn_quit = QPushButton('退出')

        # 显示视频
        self.label_show_camera = QLabel()
        self.label_move = QLabel()
        self.label_move.setFixedSize(100, 200)
        # 显示文本框
        self.text = QTextEdit(self)

        self.label_show_camera.setFixedSize(700, 550)
        self.label_show_camera.setAutoFillBackground(False)

        # 布局
        self.layout_button.addWidget(self.btn_open_cam)
        self.layout_button.addWidget(self.btn_photo)
        self.layout_button.addWidget(self.btn_photo_1)
        self.layout_button.addWidget(self.btn_quit)
        self.layout_button.addWidget(self.label_move)
        self.layout_button.addWidget(self.text)

        self.layout_main.addLayout(self.layout_button)
        self.layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.layout_main)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("数据集制作软件")

    # 信号槽设置
    def slot_init(self):
        self.btn_open_cam.clicked.connect(self.btn_open_cam_click)
        self.btn_photo.clicked.connect(self.photo_face)
        self.btn_photo_1.clicked.connect(self.photo_continue)
        self.timer_camera.timeout.connect(self.show_camera)
        self.btn_quit.clicked.connect(self.close)

    def btn_open_cam_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.cap_num)
            if flag == False:
                msg = QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确", buttons=QMessageBox.Ok,
                                          defaultButton=QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_camera.start(30)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
                self.btn_open_cam.setText(u'关闭相机')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.btn_open_cam.setText(u'打开相机')

    def show_camera(self):
        if self.btn_flag == 0:
            ret, self.image = self.cap.read()
            #print(self.image.shape)
            show = cv2.resize(self.image, (640, 480))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
            # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
            # int height, Format format, QImageCleanupFunction cleanupFunction = 0, void *cleanupInfo = 0)
            self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.label_show_camera.setPixmap(QPixmap.fromImage(self.showImage))

    def photo_face(self):
        photo_save_path = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'save_image/')
        self.showImage.save(photo_save_path + str("%05d" % self.count)+ ".jpg")
        self.count = self.count + 1

    def photo_thread(self):

        print('thread %s is running...' % threading.current_thread().name)
        for i in range(0, 11):
            self.btn_photo.click()
    def photo_continue(self):
        t = threading.Thread(target=self.photo_thread, name='Photo_Thread')
        t.start()
        t.join()


    def closeEvent(self, QCloseEvent):

        reply = QMessageBox.question(self, u"Warning", "Are you sure quit ?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.cap.release()
            self.timer_camera.stop()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())