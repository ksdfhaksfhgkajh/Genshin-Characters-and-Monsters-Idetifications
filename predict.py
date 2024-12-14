import time
import cv2
import numpy as np
from PIL import Image
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from yolo_ui import Ui_MainWindow
from yolo import YOLO
import os
import win32gui, win32ui, win32con, win32api


def convert_cv_to_qt_image(cv_img):
    """Convert an OpenCV image to a QImage for PyQt display."""
    qt_img_buf = cv2.cvtColor(cv_img, cv2.COLOR_BGR2BGRA)
    qt_img = QtGui.QImage(qt_img_buf.data, qt_img_buf.shape[1], qt_img_buf.shape[0], QtGui.QImage.Format_RGB32)
    return qt_img


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # Signal to emit string output

    def write(self, text):
        self.textWritten.emit(str(text))


class DetailUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)

        # These boolean variables are used to control loops in different detection modes
        self.close_screen_detection_loop = False
        self.close_video_detection_loop = False
        self.close_camera_detection_loop = False

        self.setWindowTitle('Intelligent Detection System')

        # Connect buttons to their respective functions
        self.image_detection_button.clicked.connect(self.open_image_file)
        self.real_time_detection_button.clicked.connect(self.start_screen_detection)
        self.video_detection_button.clicked.connect(self.open_video_file)
        self.camera_detection_button.clicked.connect(self.open_camera_stream)
        self.switch_model_button.clicked.connect(self.switch_model)
        self.exit_button.clicked.connect(self.close_application)

        # Redirect stdout and stderr to the log text browser
        sys.stdout = EmittingStr(textWritten=self.update_log_output)
        sys.stderr = EmittingStr(textWritten=self.update_log_output)

        self.yolo = YOLO('best_logs/p_best_epoch_weights.pth', 'model_data/p_classes.txt')
        print("loaded model is for pedestrian detection\n")

    def update_log_output(self, text):
        cursor = self.log_text_browser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.log_text_browser.setTextCursor(cursor)
        self.log_text_browser.ensureCursorVisible()

    def close_application(self):
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True
        self.close()

    def grab_screen(self, region=None):
        hwin = win32gui.GetDesktopWindow()

        if region:
            left, top, x2, y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
        else:
            width = int(win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) / 2)
            height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        hwindc = win32gui.GetWindowDC(hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (height, width, 4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        return img

    def start_screen_detection(self):
        # Stop all other loops, then restart screen detection
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True

        self.close_screen_detection_loop = False
        while not self.close_screen_detection_loop:
            frame = self.grab_screen()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Resize the frame for faster detection
            frame = cv2.resize(frame, (960, 540))
            # Convert to Image for YOLO
            frame = Image.fromarray(np.uint8(frame))
            # Detect objects
            frame = np.array(self.yolo.detect_image(frame))
            # Convert back to BGR for OpenCV
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            qt_img = convert_cv_to_qt_image(frame)
            self.result_frame.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            self.result_frame.setScaledContents(True)
            self.result_frame.show()

            c = cv2.waitKey(1) & 0xff
            if c == 27:  # Press 'Esc' to quit detection
                break
        cv2.destroyAllWindows()

    def open_image_file(self):
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True

        img_name, img_type = QFileDialog.getOpenFileName(self, "Open Image", "", "*.jpg;;*.png;;All Files(*)")
        if img_name == '':
            return

        image = Image.open(img_name)
        r_image = self.yolo.detect_image(image, crop=crop, count=count)
        # Temporary save detection result
        r_image.save('./imgs/predicted_img.jpg')
        display_img = './imgs/predicted_img.jpg'
        self.result_frame.setPixmap(QPixmap(display_img))
        self.result_frame.setScaledContents(True)
        if os.path.exists(display_img):
            os.remove(display_img)

    def open_video_file(self):
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True

        self.close_video_detection_loop = False
        video_name, video_type = QFileDialog.getOpenFileName(self, "Open Video", "", "*.mp4;;*.mkv;;All Files(*)")
        if video_name == '':
            return

        capture = cv2.VideoCapture(video_name)
        fps = 0.0
        while not self.close_video_detection_loop:
            t1 = time.time()
            ref, frame = capture.read()
            if not ref:
                break
            # BGR->RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(np.uint8(frame))
            frame = np.array(self.yolo.detect_image(frame))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            fps = (fps + (1. / (time.time() - t1))) / 2
            print("fps= %.2f" % (fps))
            frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            qt_img = convert_cv_to_qt_image(frame)
            self.result_frame.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            self.result_frame.setScaledContents(True)
            self.result_frame.show()
            cv2.waitKey(int(1000 / fps))
        cv2.destroyAllWindows()

    def open_camera_stream(self):
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True

        self.close_camera_detection_loop = False
        capture = cv2.VideoCapture(video_path)
        fps = 0.0
        while not self.close_camera_detection_loop:
            t1 = time.time()
            ref, frame = capture.read()
            if not ref:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(np.uint8(frame))
            frame = np.array(self.yolo.detect_image(frame))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            fps = (fps + (1. / (time.time() - t1))) / 2
            print("fps= %.2f" % (fps))
            frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            qt_img = convert_cv_to_qt_image(frame)
            self.result_frame.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            self.result_frame.setScaledContents(True)
            self.result_frame.show()
            cv2.waitKey(int(1000 / fps))
        cv2.destroyAllWindows()

    def switch_model(self):
        self.close_screen_detection_loop = True
        self.close_video_detection_loop = True
        self.close_camera_detection_loop = True

        if self.yolo.model_path == 'best_logs/p_best_epoch_weights.pth':
            print("switching to gen_model\n")
            self.yolo = YOLO('best_logs/gen_best_epoch_weights.pth', 'model_data/gen_classes.txt')
            print("_________done_________\n")
            print("switched to gen_model\n")
        elif self.yolo.model_path == 'best_logs/gen_best_epoch_weights.pth':
            print("switching to p_model\n")
            self.yolo = YOLO('best_logs/p_best_epoch_weights.pth', 'model_data/p_classes.txt')
            print("_________done_________\n")
            print("switched to p_model\n")


if __name__ == "__main__":


    # Additional settings as per original code
    crop = False
    count = False
    video_path = 0
    simplify = True

    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    sys.exit(app.exec_())
