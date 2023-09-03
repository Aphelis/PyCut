from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor, QPen, QMouseEvent, QImage
from PyQt6.QtCore import Qt, QRect
import cv2 

class ImageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_path = ""
        self.cv_image = None
        self.qt_image = None
        self.start_pos = None
        self.current_rect = None

    def set_image(self, cv_image):
        self.qt_image = self.cv2_to_qimage(cv_image)
        self.repaint()

    def cv2_to_qimage(self, cv_image):
        height, width, channels = cv_image.shape
        bytes_per_line = channels * width
        return QImage(cv_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.pos()
            self.current_rect = QRect(self.start_pos, self.start_pos)
            self.update()
    def mouseMoveEvent(self, event):
        if self.start_pos is not None:
            self.current_rect.setBottomRight(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = None
            self.update()

    def paintEvent(self, event):
        if self.qt_image is not None:
            painter = QPainter(self)
            painter.drawImage(0, 0, self.qt_image)

            # if self.current_rect:
            #     pen = QPen(QColor(255, 0, 0), 1)
            #     painter.setPen(pen)
            #     painter.drawRect(self.current_rect)