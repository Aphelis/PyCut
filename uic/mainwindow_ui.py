# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDoubleSpinBox, QFormLayout,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QToolBar, QWidget)

from ImageWidget import ImageWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 760)
        icon = QIcon()
        icon.addFile(u"../icon/crop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"	}\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"	}")
        self.menuOpen = QAction(MainWindow)
        self.menuOpen.setObjectName(u"menuOpen")
        icon1 = QIcon()
        icon1.addFile(u"../icon/add-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuOpen.setIcon(icon1)
        self.menuSave = QAction(MainWindow)
        self.menuSave.setObjectName(u"menuSave")
        icon2 = QIcon()
        icon2.addFile(u"../icon/save-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuSave.setIcon(icon2)
        self.menuSaveAs = QAction(MainWindow)
        self.menuSaveAs.setObjectName(u"menuSaveAs")
        self.menuSOP = QAction(MainWindow)
        self.menuSOP.setObjectName(u"menuSOP")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chooseButton = QPushButton(self.centralwidget)
        self.chooseButton.setObjectName(u"chooseButton")
        self.chooseButton.setGeometry(QRect(620, 10, 93, 29))
        self.chooseButton.setStyleSheet(u"")
        self.cutImageWidget = ImageWidget(self.centralwidget)
        self.cutImageWidget.setObjectName(u"cutImageWidget")
        self.cutImageWidget.setGeometry(QRect(670, 360, 255, 255))
        self.cutImageWidget.setStyleSheet(u"QWidget {\n"
"  border: 2px solid #000000;\n"
"}")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(620, 50, 311, 311))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.layoutWidget = QWidget(self.page_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 301, 301))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.upleftButton = QPushButton(self.layoutWidget)
        self.upleftButton.setObjectName(u"upleftButton")
        self.upleftButton.setMinimumSize(QSize(75, 75))
        self.upleftButton.setMaximumSize(QSize(90, 90))
        self.upleftButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"	}\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"	}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../icon/up-left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upleftButton.setIcon(icon3)
        self.upleftButton.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.upleftButton, 0, 0, 1, 1)

        self.upButton = QPushButton(self.layoutWidget)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setMinimumSize(QSize(50, 50))
        self.upButton.setMaximumSize(QSize(75, 75))
        self.upButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon4 = QIcon()
        icon4.addFile(u"../icon/up-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upButton.setIcon(icon4)
        self.upButton.setIconSize(QSize(95, 95))

        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)

        self.uprightButton = QPushButton(self.layoutWidget)
        self.uprightButton.setObjectName(u"uprightButton")
        self.uprightButton.setMinimumSize(QSize(50, 50))
        self.uprightButton.setMaximumSize(QSize(75, 75))
        self.uprightButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon5 = QIcon()
        icon5.addFile(u"../icon/up-right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uprightButton.setIcon(icon5)
        self.uprightButton.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.uprightButton, 0, 2, 1, 1)

        self.leftButton = QPushButton(self.layoutWidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setMinimumSize(QSize(50, 50))
        self.leftButton.setMaximumSize(QSize(75, 75))
        self.leftButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon6 = QIcon()
        icon6.addFile(u"../icon/left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftButton.setIcon(icon6)
        self.leftButton.setIconSize(QSize(95, 95))

        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.autocutButton = QPushButton(self.layoutWidget)
        self.autocutButton.setObjectName(u"autocutButton")
        self.autocutButton.setMinimumSize(QSize(75, 75))
        self.autocutButton.setMaximumSize(QSize(75, 75))
        self.autocutButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    \n"
"    }")
        icon7 = QIcon()
        icon7.addFile(u"../icon/four-arrows.png", QSize(), QIcon.Normal, QIcon.Off)
        self.autocutButton.setIcon(icon7)
        self.autocutButton.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.autocutButton, 1, 1, 1, 1)

        self.rightButton = QPushButton(self.layoutWidget)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setMinimumSize(QSize(50, 50))
        self.rightButton.setMaximumSize(QSize(75, 75))
        self.rightButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon8 = QIcon()
        icon8.addFile(u"../icon/right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightButton.setIcon(icon8)
        self.rightButton.setIconSize(QSize(95, 95))

        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.downleftButton = QPushButton(self.layoutWidget)
        self.downleftButton.setObjectName(u"downleftButton")
        self.downleftButton.setMinimumSize(QSize(50, 50))
        self.downleftButton.setMaximumSize(QSize(75, 75))
        self.downleftButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"../icon/down-left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downleftButton.setIcon(icon9)
        self.downleftButton.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.downleftButton, 2, 0, 1, 1)

        self.downButton = QPushButton(self.layoutWidget)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setMinimumSize(QSize(50, 50))
        self.downButton.setMaximumSize(QSize(75, 75))
        self.downButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon10 = QIcon()
        icon10.addFile(u"../icon/down-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downButton.setIcon(icon10)
        self.downButton.setIconSize(QSize(95, 95))

        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)

        self.downrightButton = QPushButton(self.layoutWidget)
        self.downrightButton.setObjectName(u"downrightButton")
        self.downrightButton.setMinimumSize(QSize(50, 50))
        self.downrightButton.setMaximumSize(QSize(75, 75))
        self.downrightButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        icon11 = QIcon()
        icon11.addFile(u"../icon/down-right-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downrightButton.setIcon(icon11)
        self.downrightButton.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.downrightButton, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.layoutWidget1 = QWidget(self.page_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 301, 301))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.upleftButton_2 = QPushButton(self.layoutWidget1)
        self.upleftButton_2.setObjectName(u"upleftButton_2")
        self.upleftButton_2.setMinimumSize(QSize(75, 75))
        self.upleftButton_2.setMaximumSize(QSize(90, 90))
        self.upleftButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"	}\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"	}\n"
"\n"
"")
        self.upleftButton_2.setIcon(icon11)
        self.upleftButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.upleftButton_2, 0, 0, 1, 1)

        self.upButton_2 = QPushButton(self.layoutWidget1)
        self.upButton_2.setObjectName(u"upButton_2")
        self.upButton_2.setMinimumSize(QSize(50, 50))
        self.upButton_2.setMaximumSize(QSize(75, 75))
        self.upButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.upButton_2.setIcon(icon4)
        self.upButton_2.setIconSize(QSize(95, 95))

        self.gridLayout_2.addWidget(self.upButton_2, 0, 1, 1, 1)

        self.uprightButton_2 = QPushButton(self.layoutWidget1)
        self.uprightButton_2.setObjectName(u"uprightButton_2")
        self.uprightButton_2.setMinimumSize(QSize(50, 50))
        self.uprightButton_2.setMaximumSize(QSize(75, 75))
        self.uprightButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.uprightButton_2.setIcon(icon9)
        self.uprightButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.uprightButton_2, 0, 2, 1, 1)

        self.leftButton_2 = QPushButton(self.layoutWidget1)
        self.leftButton_2.setObjectName(u"leftButton_2")
        self.leftButton_2.setMinimumSize(QSize(50, 50))
        self.leftButton_2.setMaximumSize(QSize(75, 75))
        self.leftButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.leftButton_2.setIcon(icon6)
        self.leftButton_2.setIconSize(QSize(95, 95))

        self.gridLayout_2.addWidget(self.leftButton_2, 1, 0, 1, 1)

        self.autocutButton_2 = QPushButton(self.layoutWidget1)
        self.autocutButton_2.setObjectName(u"autocutButton_2")
        self.autocutButton_2.setMinimumSize(QSize(75, 75))
        self.autocutButton_2.setMaximumSize(QSize(75, 75))
        self.autocutButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    \n"
"    }")
        self.autocutButton_2.setIcon(icon7)
        self.autocutButton_2.setIconSize(QSize(80, 80))

        self.gridLayout_2.addWidget(self.autocutButton_2, 1, 1, 1, 1)

        self.rightButton_2 = QPushButton(self.layoutWidget1)
        self.rightButton_2.setObjectName(u"rightButton_2")
        self.rightButton_2.setMinimumSize(QSize(50, 50))
        self.rightButton_2.setMaximumSize(QSize(75, 75))
        self.rightButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.rightButton_2.setIcon(icon8)
        self.rightButton_2.setIconSize(QSize(95, 95))

        self.gridLayout_2.addWidget(self.rightButton_2, 1, 2, 1, 1)

        self.downleftButton_2 = QPushButton(self.layoutWidget1)
        self.downleftButton_2.setObjectName(u"downleftButton_2")
        self.downleftButton_2.setMinimumSize(QSize(50, 50))
        self.downleftButton_2.setMaximumSize(QSize(75, 75))
        self.downleftButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"")
        self.downleftButton_2.setIcon(icon5)
        self.downleftButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.downleftButton_2, 2, 0, 1, 1)

        self.downButton_2 = QPushButton(self.layoutWidget1)
        self.downButton_2.setObjectName(u"downButton_2")
        self.downButton_2.setMinimumSize(QSize(50, 50))
        self.downButton_2.setMaximumSize(QSize(75, 75))
        self.downButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downButton_2.setIcon(icon10)
        self.downButton_2.setIconSize(QSize(95, 95))

        self.gridLayout_2.addWidget(self.downButton_2, 2, 1, 1, 1)

        self.downrightButton_2 = QPushButton(self.layoutWidget1)
        self.downrightButton_2.setObjectName(u"downrightButton_2")
        self.downrightButton_2.setMinimumSize(QSize(50, 50))
        self.downrightButton_2.setMaximumSize(QSize(75, 75))
        self.downrightButton_2.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downrightButton_2.setIcon(icon3)
        self.downrightButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.downrightButton_2, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(550, 350, 50, 29))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(550, 390, 51, 173))
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel_2 = QLabel(self.layoutWidget2)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel_2)

        self.xValue = QLineEdit(self.layoutWidget2)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.xValue)

        self.nameLabel_3 = QLabel(self.layoutWidget2)
        self.nameLabel_3.setObjectName(u"nameLabel_3")
        self.nameLabel_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nameLabel_3)

        self.yValue = QLineEdit(self.layoutWidget2)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.yValue)

        self.nameLabel_4 = QLabel(self.layoutWidget2)
        self.nameLabel_4.setObjectName(u"nameLabel_4")
        self.nameLabel_4.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nameLabel_4)

        self.pixelValue = QLineEdit(self.layoutWidget2)
        self.pixelValue.setObjectName(u"pixelValue")
        self.pixelValue.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pixelValue)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 545, 690))
        self.splitter.setOrientation(Qt.Vertical)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.ImageWidget = ImageWidget(self.tab_3)
        self.ImageWidget.setObjectName(u"ImageWidget")
        self.ImageWidget.setGeometry(QRect(0, 0, 540, 540))
        self.ImageWidget.setMinimumSize(QSize(540, 540))
        self.ImageWidget.setStyleSheet(u"QWidget {\n"
"  border: 2px solid #000000;\n"
"}")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableView = QTableView(self.tab_4)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 540, 540))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QSize(540, 540))
        self.tableView.setLineWidth(1)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setIconSize(QSize(0, 0))
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setSortingEnabled(False)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(28)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_4, "")
        self.splitter.addWidget(self.tabWidget)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(540, 120))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_2 = QWidget()
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 543, 118))
        self.scrollArea.setWidget(self.scrollArea_2)
        self.splitter.addWidget(self.scrollArea)
        self.contrastdoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.contrastdoubleSpinBox.setObjectName(u"contrastdoubleSpinBox")
        self.contrastdoubleSpinBox.setGeometry(QRect(860, 625, 62, 20))
        self.contrastdoubleSpinBox.setDecimals(1)
        self.contrastdoubleSpinBox.setMaximum(2.000000000000000)
        self.contrastdoubleSpinBox.setSingleStep(0.100000000000000)
        self.contrastdoubleSpinBox.setValue(1.000000000000000)
        self.contrastSlider = QSlider(self.centralwidget)
        self.contrastSlider.setObjectName(u"contrastSlider")
        self.contrastSlider.setGeometry(QRect(680, 625, 171, 20))
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(20)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setPageStep(1)
        self.contrastSlider.setValue(10)
        self.contrastSlider.setOrientation(Qt.Horizontal)
        self.contrastSlider.setInvertedAppearance(False)
        self.contrastSlider.setInvertedControls(False)
        self.contrastSlider.setTickPosition(QSlider.TicksAbove)
        self.contrastSlider.setTickInterval(0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, 645, 51, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuOpen)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addAction(self.menuSaveAs)
        self.menuHelp.addAction(self.menuSOP)
        self.toolBar.addAction(self.menuOpen)
        self.toolBar.addAction(self.menuSave)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PiCut", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.menuOpen.setText(QCoreApplication.translate("MainWindow", u"Open..", None))
        self.menuSave.setText(QCoreApplication.translate("MainWindow", u"Save ...", None))
#if QT_CONFIG(tooltip)
        self.menuSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save..", None))
#endif // QT_CONFIG(tooltip)
        self.menuSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.menuSOP.setText(QCoreApplication.translate("MainWindow", u"SOP", None))
        self.chooseButton.setText(QCoreApplication.translate("MainWindow", u"Enlarge ", None))
        self.upleftButton.setText("")
        self.upButton.setText("")
        self.uprightButton.setText("")
        self.leftButton.setText("")
        self.autocutButton.setText("")
        self.rightButton.setText("")
        self.downleftButton.setText("")
        self.downButton.setText("")
        self.downrightButton.setText("")
        self.upleftButton_2.setText("")
        self.upButton_2.setText("")
        self.uprightButton_2.setText("")
        self.leftButton_2.setText("")
        self.autocutButton_2.setText("")
        self.rightButton_2.setText("")
        self.downleftButton_2.setText("")
        self.downButton_2.setText("")
        self.downrightButton_2.setText("")
        self.nameLabel.setText("")
        self.nameLabel_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.xValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.nameLabel_3.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.yValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.nameLabel_4.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.pixelValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Color", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

