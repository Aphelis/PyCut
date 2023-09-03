import sys
import os
import cv2
import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QFileDialog, QTableWidget,
    QDialogButtonBox, QComboBox, QTableWidgetItem,
    QTabWidget, QPushButton, QWidget, QMessageBox,
    QLabel, QScrollArea, QVBoxLayout, QHBoxLayout,
    QStackedWidget
)
from PyQt6.QtGui import QAction, QCloseEvent, QImage, QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, QThreadPool, pyqtSignal, QEvent

from PyQt6 import uic, QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from module.Worker import Worker
from module.ClickableLabel import ClickableLabel
from ImageWidget import ImageWidget
from module.image_processing import HoughCirclesImg, cropImage

Ui_MainWindow, QtBaseClass = uic.loadUiType("uic/mainwindow.ui")
class MainWindow(QMainWindow, Ui_MainWindow):
    customImg = {}
    key = ""
    showImg = None
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("PiCut")
        #Image Widget
        self.imgWidget = self.findChild(ImageWidget, "ImageWidget")
        self.cutImageWidget = self.findChild(ImageWidget, "cutImageWidget")
        #Parameter
        self.x1 = 0;self.y1 = 0;self.x2 = 0;self.y2 = 0
        self.dir = ""
        #Check Parameter
        self.chooseButton_checked = False
        self.findImage_check = False
        self.current_layout_index = 0
        #scrollArea
        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.setWidgetResizable(True)
        #Auto Cut
        self.autocutButton = self.findChild(QPushButton, "autocutButton")
        self.autocutButton.clicked.connect(self.autofindButton_clicked)
        #Choose Button
        self.chooseButton = self.findChild(QPushButton, "chooseButton")
        self.chooseButton.clicked.connect(self.chooseButton_clicked)
        #Button
        #Up
        self.upButton = self.findChild(QPushButton, "upButton")
        self.upButton.clicked.connect(self.upButonButton_clicked)
        #Down
        self.downButton = self.findChild(QPushButton, "downButton")
        self.downButton.clicked.connect(self.downButonButton_clicked)
        #Left
        self.leftButton = self.findChild(QPushButton, "leftButton")
        self.leftButton.clicked.connect(self.leftButonButton_clicked)
        #Right
        self.rightButton = self.findChild(QPushButton, "rightButton")
        self.rightButton.clicked.connect(self.rightButonButton_clicked)
        #Up_Left
        self.upleftButton = self.findChild(QPushButton, "upleftButton")
        self.upleftButton.clicked.connect(self.upleftButonButton_clicked)
        #Up_Right
        self.uprightButton = self.findChild(QPushButton, "uprightButton")
        self.uprightButton.clicked.connect(self.uprightButonButton_clicked)
        #Down_Left
        self.downleftButton = self.findChild(QPushButton, "downleftButton")
        self.downleftButton.clicked.connect(self.downleftButonButton_clicked)
        #Down_Right
        self.downrightButton = self.findChild(QPushButton, "downrightButton")
        self.downrightButton.clicked.connect(self.downrightButonButton_clicked)
        #Zoom out Button 
        #Up
        self.upButton_2 = self.findChild(QPushButton, "upButton_2")
        self.upButton_2.clicked.connect(self.upButonButton_clicked)
        #Down
        self.downButton_2 = self.findChild(QPushButton, "downButton_2")
        self.downButton_2.clicked.connect(self.downButonButton_clicked)
        #Left
        self.leftButton_2 = self.findChild(QPushButton, "leftButton_2")
        self.leftButton_2.clicked.connect(self.leftButonButton_clicked)
        #Right
        self.rightButton_2 = self.findChild(QPushButton, "rightButton_2")
        self.rightButton.clicked.connect(self.rightButonButton_clicked)
        #Up_Left
        self.upleftButton_2 = self.findChild(QPushButton, "upleftButton_2")
        self.upleftButton_2.clicked.connect(self.upleftButonButton_2_clicked)
        #Up_Right
        self.uprightButton_2 = self.findChild(QPushButton, "uprightButton_2")
        self.uprightButton_2.clicked.connect(self.uprightButonButton_2_clicked)
        #Down_Left
        self.downleftButton_2 = self.findChild(QPushButton, "downleftButton_2")
        self.downleftButton_2.clicked.connect(self.downleftButonButton_2_clicked)
        #Down_Right
        self.downrightButton_2 = self.findChild(QPushButton, "downrightButton_2")
        self.downrightButton_2.clicked.connect(self.downrightButonButton_2_clicked)
        # Create a QStackedWidget to hold the layouts
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        #File
        self.menuOpen = self.findChild(QAction, "menuOpen")
        self.menuOpen.setShortcut('Ctrl+O')
        self.menuOpen.triggered.connect(self.Open)
        self.menuSave = self.findChild(QAction, "menuSave")
        self.menuSave.setShortcut('Ctrl+S')
        self.menuSave.triggered.connect(self.Save)
        self.menuSaveAs = self.findChild(QAction, "menuSaveAs")
        self.menuSaveAs.setShortcut('Ctrl+Shift+S')
        self.menuSaveAs.triggered.connect(self.SaveAs)
        self.menuSaveAs.setEnabled(False)
    def Open(self):
        self.clear()
        paths = QFileDialog.getOpenFileNames(self, 
                                            caption="Open Picture...",
                                            directory= r"./image" , 
                                            filter = """All(*.*);;PNG Images (*.png);;
                                                        PNG Images (*.png);;BMP Images (*.bmp);;
                                                        BMP Images (*.bmp);;TIFF Images (*.tiff);;
                                                        WebP Images (*.webp);;Icon Images (*.ico)
                                                        """)[0]
        for path in paths:
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            file = os.path.basename(path)
            file_name = os.path.splitext(file)
            MainWindow.customImg.update({file_name[0]: img})
        MainWindow.key = file_name[0]
        self.refeshImage()
        self.set_layout()
    def Save(self):
        if self.dir:
            pass
        else:
            self.SaveAs()
            self.menuSaveAs.setEnabled(True)
        keys = MainWindow.customImg.keys()
        for key in keys:
            image = MainWindow.customImg[key][self.y2:self.y1, self.x1:self.x2]
            file_name = self.dir+ "/" + key + ".JPG"
            cv2.imwrite(file_name, image)
    def SaveAs(self):
        self.dir = QFileDialog.getExistingDirectory(self,
                                                    caption = "Open Directory"
                                                    # directory= r"./image"
                                                    )
        self.Save()
    def refeshImage(self):
        if not self.findImage_check:
            image = MainWindow.customImg[MainWindow.key]
        else:
            image = MainWindow.customImg[MainWindow.key]
            image, cutImage = cropImage(image, self.x1, self.y2, self.x2, self.y1)
            cutImage = cv2.resize(cutImage, dsize=(255, 255), interpolation=cv2.INTER_AREA)
            self.cutImageWidget.set_image(cutImage)
        image = cv2.resize(image, None, fx=2.1, fy=2.1, interpolation=cv2.INTER_AREA)
        self.imgWidget.set_image(image)
    def set_layout(self):
        keys = MainWindow.customImg.keys()
        # Create a QVBoxLayout to hold the labels
        layout = QHBoxLayout()
        # Create multiple QLabel widgets with different content
        for key in keys:
            # Create a QLabel for the pixmap
            label = ClickableLabel(key)
            label.setToolTip(key)
            label.clicked.connect(self.imgLabel_clicked)
            img = cv2.resize(MainWindow.customImg[key], None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
            img = QPixmap.fromImage(self.cv2_to_qimage(img))
            label.setPixmap(img)
            layout.addWidget(label)
        # Create a QWidget to act as the content of the scroll area
        scroll_content = QWidget(self)
        scroll_content.setLayout(layout)
        # Create a QScrollArea and set its content widget
        self.scrollArea.setWidget(scroll_content)
    def imgLabel_clicked(self, label_text):
        img = MainWindow.customImg[label_text]
        MainWindow.key = label_text
        self.refeshImage() 
    def autofindButton_clicked(self):
        self.x1, self.y1, self.x2, self.y2 = HoughCirclesImg(MainWindow.customImg[MainWindow.key])
        self.findImage_check = True
        self.refeshImage()
    def clear(self):
        # Get the QScrollArea's container widget
        container_widget = self.scrollArea.widget()
        if container_widget.layout() is not None:
            # Remove all child widgets from the container widget
            while container_widget.layout().count() > 0:
                item = container_widget.layout().takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            MainWindow.customImg.clear()
            MainWindow.key = ""
        self.findImage_check = False
        self.chooseButton_checked = False
    def chooseButton_clicked(self):
        self.current_layout_index = 1 - self.current_layout_index  # Toggle between 0 and 1
        self.stackedWidget.setCurrentIndex(self.current_layout_index)
    def upButonButton_clicked(self):
        self.y2 -= 1;self.y1 -= 1
        self.refeshImage()
    def downButonButton_clicked(self):
        self.y1 += 1;self.y2 += 1
        self.refeshImage()
    def leftButonButton_clicked(self):
        self.x2 -= 1;self.x1 -= 1
        self.refeshImage()
    def rightButonButton_clicked(self):
        self.x1 += 1;self.x2 += 1
        self.refeshImage()
    def upleftButonButton_clicked(self):
        self.y2 -= 1;self.x1 -= 1
        self.refeshImage()
    def uprightButonButton_clicked(self):
        self.y2 -= 1;self.x2 += 1
        self.refeshImage()
    def downleftButonButton_clicked(self):
        self.y1 += 1;self.x1 -= 1
        self.refeshImage()
    def downrightButonButton_clicked(self):
        self.y1 += 1;self.x2 += 1
        self.refeshImage()
    def upleftButonButton_2_clicked(self):
        self.y2 += 1;self.x1 -= 1
        self.refeshImage()
    def uprightButonButton_2_clicked(self):
        self.y2 += 1;self.x2 -= 1
        self.refeshImage()
    def downleftButonButton_2_clicked(self):
        self.y1 -= 1;self.x1 += 1
        self.refeshImage()
    def downrightButonButton_2_clicked(self):
        self.y1 -= 1;self.x2 += 1
        self.refeshImage()
    def cv2_to_qimage(self, cv_image):
        height, width, channels = cv_image.shape
        bytes_per_line = channels * width
        return QImage(cv_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
    def closeEvent(self, event: QCloseEvent):
        super().closeEvent(event) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()