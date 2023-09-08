import sys
import os
import cv2
import numpy as np
import webbrowser
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QFileDialog, QTableWidget,
    QDialogButtonBox, QComboBox, QTableWidgetItem,
    QTabWidget, QPushButton, QWidget, QMessageBox,
    QLabel, QScrollArea, QVBoxLayout, QHBoxLayout,
    QStackedWidget, QLineEdit, QTableView, QSlider,
    QDoubleSpinBox
)
from PyQt6.QtGui import QAction, QCloseEvent, QImage, QPixmap, QMouseEvent
from PyQt6.QtCore import Qt, QThreadPool, pyqtSignal, QEvent

from PyQt6 import uic, QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from module.Worker import Worker
from module.ClickableLabel import ClickableLabel
from ImageWidget import ImageWidget
from module.image_processing import *
from module.TableModel import TableModel

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass
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
        self.contrast = 1
        #Check Parameter
        self.chooseButton_checked = False
        self.findImage_check = False
        self.current_layout_index = 0
        #scrollArea
        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.setWidgetResizable(True)
        #Table
        self.table = self.findChild(QTableView, "tableView")
        #Slider
        self.contrastSlider = self.findChild(QSlider, "contrastSlider")
        self.contrastSlider.valueChanged.connect(self.contrastValueChange)
        self.contrastSlider.valueChanged.connect(lambda value: self.contrastdoubleSpinBox.setValue(value / 10.0))
        #DoubleSpinbox
        self.contrastdoubleSpinBox =self.findChild(QDoubleSpinBox, "contrastdoubleSpinBox")
        self.contrastdoubleSpinBox.valueChanged.connect(lambda value: self.contrastSlider.setValue(int(value * 10)))
        #Auto Cut
        self.autocutButton = self.findChild(QPushButton, "autocutButton")
        self.autocutButton.clicked.connect(self.autofindButton_clicked)
        #Choose Button
        self.chooseButton = self.findChild(QPushButton, "chooseButton")
        self.chooseButton.clicked.connect(self.chooseButton_clicked)
        #Label
        self.nameLabel = self.findChild(QLabel, "nameLabel")
        #QLineEdit
        self.xValue = self.findChild(QLineEdit, "xValue")
        self.yValue = self.findChild(QLineEdit, "yValue")
        self.pixelValue = self.findChild(QLineEdit, "pixelValue")
        self.xValue.setReadOnly(True)
        self.yValue.setReadOnly(True)
        self.pixelValue.setReadOnly(True)
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
        self.rightButton_2.clicked.connect(self.rightButonButton_clicked)
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
        self.menuSave.setEnabled(False)
        self.menuSaveAs = self.findChild(QAction, "menuSaveAs")
        self.menuSaveAs.setShortcut('Ctrl+Shift+S')
        self.menuSaveAs.triggered.connect(self.SaveAs)
        self.menuSaveAs.setEnabled(False)
        #Help
        self.menuSOP = self.findChild(QAction, "menuSOP")
        self.menuSOP.triggered.connect(self.SOP)
    def Open(self):
        try:
            
            paths = QFileDialog.getOpenFileNames(self, 
                                                caption="Open Picture...",
                                                filter = """All(*.*);;PNG Images (*.png);;
                                                            PNG Images (*.png);;BMP Images (*.bmp);;
                                                            BMP Images (*.bmp);;TIFF Images (*.tiff);;
                                                            WebP Images (*.webp);;Icon Images (*.ico)
                                                            """)[0]
            if paths: #Check paths is not None
                self.clear()
            for path in paths:
                raw_data = np.fromfile(path, dtype=np.uint8)
                img = cv2.imdecode(raw_data, cv2.IMREAD_COLOR)
                # img = cv2.imread(path, cv2.IMREAD_COLOR)
                file = os.path.basename(path)
                file_name = os.path.splitext(file)
                file_name ="0" + str(int(file_name[0])-1)
                MainWindow.customImg.update({file_name: img})
            MainWindow.key = file_name
            self.refeshImage()
            self.set_layout()
        except:
            pass
    def Save(self):
            if self.dir:
                pass
            else:
                self.SaveAs()
                self.menuSaveAs.setEnabled(True)
            keys = MainWindow.customImg.keys()
            for key in keys:
                image = MainWindow.customImg[key][self.y2:self.y1, self.x1:self.x2]
                
                file_name = self.dir + "/" + key + ".JPG"
                is_success, im_buf_arr = cv2.imencode(".jpg", image)
                if is_success:
                    im_buf_arr.tofile(file_name)
                else:
                    pass
    def SaveAs(self):
        self.dir = QFileDialog.getExistingDirectory(self,
                                                    caption = "Open Directory"
                                                    # directory= r"./image"
                                                    )
        
        self.Save()
    def SOP(self):
        webbrowser.open_new(r'documents\SOP.pdf')
    def refeshImage(self):
        try:
            if not self.findImage_check:
                image = MainWindow.customImg[MainWindow.key]
            else:
                image = MainWindow.customImg[MainWindow.key]
                image, cutImage = cropImage(image, self.x1, self.y2, self.x2, self.y1)
                cutImage = self.contrastCheck(cutImage)
                graycutimage = grayImg(cutImage) 
                self.model = TableModel(graycutimage)
                self.table.setModel(self.model)
                cutImage = cv2.resize(cutImage, dsize=(255, 255), interpolation=cv2.INTER_AREA)
                self.cutImageWidget.set_image(cutImage)
                self.xValue.setText(str(self.x1))
                self.yValue.setText(str(self.y2))
                self.pixelValue.setText(str(self.x2-self.x1))
            image = cv2.resize(image, None, fx=2.1, fy=2.1, interpolation=cv2.INTER_AREA)
            self.imgWidget.set_image(image)
            self.nameLabel.setText(MainWindow.key)
        except KeyError:
            pass
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
        self.xValue.setReadOnly(False)
        self.yValue.setReadOnly(False)
        self.pixelValue.setReadOnly(False)
        self.menuSave.setEnabled(True)
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
        # self.findImage_check = False
        self.chooseButton_checked = False
        self.menuSave.setEnabled(False)
    def chooseButton_clicked(self):
        buttonText = ["Enlarge ", "Shrink"]
        self.current_layout_index = 1 - self.current_layout_index  # Toggle between 0 and 1
        self.stackedWidget.setCurrentIndex(self.current_layout_index)
        self.chooseButton.setText(buttonText[self.current_layout_index])
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
        self.y2 += 1;self.x1 += 1
        self.refeshImage()
    def uprightButonButton_2_clicked(self):
        self.y2 += 1;self.x2 -= 1
        self.refeshImage()
    def downleftButonButton_2_clicked(self):
        self.y1 -= 1;self.x1 += 1
        self.refeshImage()
    def downrightButonButton_2_clicked(self):
        self.y1 -= 1;self.x2 -= 1
        self.refeshImage()
    def cv2_to_qimage(self, cv_image):
        height, width, channels = cv_image.shape
        bytes_per_line = channels * width
        return QImage(cv_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
    def contrastCheck(self, img):
        if self.contrast == 1:
            return img
        elif self.contrast < 1:
            return lowContrastImg(img, self.contrast)
        elif self.contrast > 1:
            return highContrastImg(img, self.contrast)
    def contrastValueChange(self, value):
        self.contrast = value / 10
        self.refeshImage()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_W:
            self.upButonButton_clicked()
        elif event.key() == QtCore.Qt.Key.Key_S:
            self.downButonButton_clicked()
        elif event.key() == QtCore.Qt.Key.Key_A:
            self.leftButonButton_clicked()
        elif event.key() == QtCore.Qt.Key.Key_D:
            self.rightButonButton_clicked()
        else:
            QMainWindow.keyPressEvent(self, event)
    def closeEvent(self, event: QCloseEvent):
        super().closeEvent(event) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()