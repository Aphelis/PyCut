# Form implementation generated from reading ui file 'g:\Alan\PyCut\dist\app\uic\mainwindow_large.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/crop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleName("")
        MainWindow.setStyleSheet("QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"    }\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 760))
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_3 = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 1000, 760))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(0, 760))
        self.scrollArea_3.setMaximumSize(QtCore.QSize(1000, 760))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 998, 758))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(740, 640, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(550, 385, 51, 173))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel_2)
        self.xValue = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.xValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.xValue.setObjectName("xValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.xValue)
        self.nameLabel_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.nameLabel_3.setFont(font)
        self.nameLabel_3.setObjectName("nameLabel_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel_3)
        self.yValue = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.yValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.yValue.setObjectName("yValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.yValue)
        self.nameLabel_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.nameLabel_4.setFont(font)
        self.nameLabel_4.setObjectName("nameLabel_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel_4)
        self.pixelValue = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.pixelValue.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pixelValue.setObjectName("pixelValue")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pixelValue)
        self.nameLabel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.nameLabel.setGeometry(QtCore.QRect(550, 345, 50, 29))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.nameLabel.setFont(font)
        self.nameLabel.setText("")
        self.nameLabel.setObjectName("nameLabel")
        self.contrastdoubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.scrollAreaWidgetContents)
        self.contrastdoubleSpinBox.setGeometry(QtCore.QRect(860, 620, 62, 20))
        self.contrastdoubleSpinBox.setDecimals(1)
        self.contrastdoubleSpinBox.setMaximum(2.0)
        self.contrastdoubleSpinBox.setSingleStep(0.1)
        self.contrastdoubleSpinBox.setProperty("value", 1.0)
        self.contrastdoubleSpinBox.setObjectName("contrastdoubleSpinBox")
        self.contrastSlider = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents)
        self.contrastSlider.setGeometry(QtCore.QRect(680, 620, 171, 20))
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(20)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setPageStep(1)
        self.contrastSlider.setProperty("value", 10)
        self.contrastSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.contrastSlider.setInvertedAppearance(False)
        self.contrastSlider.setInvertedControls(False)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.contrastSlider.setTickInterval(0)
        self.contrastSlider.setObjectName("contrastSlider")
        self.cutImageWidget = ImageWidget(parent=self.scrollAreaWidgetContents)
        self.cutImageWidget.setGeometry(QtCore.QRect(670, 355, 255, 255))
        self.cutImageWidget.setStyleSheet("QWidget {\n"
"  border: 2px solid #000000;\n"
"}")
        self.cutImageWidget.setObjectName("cutImageWidget")
        self.chooseButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.chooseButton.setGeometry(QtCore.QRect(620, 5, 93, 29))
        self.chooseButton.setStyleSheet("")
        self.chooseButton.setObjectName("chooseButton")
        self.splitter = QtWidgets.QSplitter(parent=self.scrollAreaWidgetContents)
        self.splitter.setGeometry(QtCore.QRect(0, -5, 545, 690))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ImageWidget = ImageWidget(parent=self.tab_3)
        self.ImageWidget.setGeometry(QtCore.QRect(0, 0, 540, 540))
        self.ImageWidget.setMinimumSize(QtCore.QSize(540, 540))
        self.ImageWidget.setStyleSheet("QWidget {\n"
"  border: 2px solid #000000;\n"
"}")
        self.ImageWidget.setObjectName("ImageWidget")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableView = QtWidgets.QTableView(parent=self.tab_4)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 540, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QtCore.QSize(540, 540))
        self.tableView.setLineWidth(1)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setIconSize(QtCore.QSize(0, 0))
        self.tableView.setTextElideMode(QtCore.Qt.TextElideMode.ElideRight)
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(28)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab_4, "")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.splitter)
        self.scrollArea.setMinimumSize(QtCore.QSize(540, 120))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea_2 = QtWidgets.QWidget()
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 543, 118))
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea.setWidget(self.scrollArea_2)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.scrollAreaWidgetContents)
        self.stackedWidget.setGeometry(QtCore.QRect(620, 45, 311, 311))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.page_1)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.upleftButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.upleftButton.setMinimumSize(QtCore.QSize(75, 75))
        self.upleftButton.setMaximumSize(QtCore.QSize(90, 90))
        self.upleftButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"    }\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"    }\n"
"\n"
"")
        self.upleftButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/up-left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.upleftButton.setIcon(icon1)
        self.upleftButton.setIconSize(QtCore.QSize(60, 60))
        self.upleftButton.setObjectName("upleftButton")
        self.gridLayout.addWidget(self.upleftButton, 0, 0, 1, 1)
        self.upButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.upButton.setMinimumSize(QtCore.QSize(50, 50))
        self.upButton.setMaximumSize(QtCore.QSize(75, 75))
        self.upButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.upButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/up-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.upButton.setIcon(icon2)
        self.upButton.setIconSize(QtCore.QSize(95, 95))
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)
        self.uprightButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.uprightButton.setMinimumSize(QtCore.QSize(50, 50))
        self.uprightButton.setMaximumSize(QtCore.QSize(75, 75))
        self.uprightButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.uprightButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/up-right-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.uprightButton.setIcon(icon3)
        self.uprightButton.setIconSize(QtCore.QSize(60, 60))
        self.uprightButton.setObjectName("uprightButton")
        self.gridLayout.addWidget(self.uprightButton, 0, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.leftButton.setMinimumSize(QtCore.QSize(50, 50))
        self.leftButton.setMaximumSize(QtCore.QSize(75, 75))
        self.leftButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.leftButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.leftButton.setIcon(icon4)
        self.leftButton.setIconSize(QtCore.QSize(95, 95))
        self.leftButton.setObjectName("leftButton")
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)
        self.autocutButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.autocutButton.setMinimumSize(QtCore.QSize(75, 75))
        self.autocutButton.setMaximumSize(QtCore.QSize(75, 75))
        self.autocutButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    \n"
"    }")
        self.autocutButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/four-arrows.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.autocutButton.setIcon(icon5)
        self.autocutButton.setIconSize(QtCore.QSize(80, 80))
        self.autocutButton.setObjectName("autocutButton")
        self.gridLayout.addWidget(self.autocutButton, 1, 1, 1, 1)
        self.rightButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.rightButton.setMinimumSize(QtCore.QSize(50, 50))
        self.rightButton.setMaximumSize(QtCore.QSize(75, 75))
        self.rightButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.rightButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/right-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightButton.setIcon(icon6)
        self.rightButton.setIconSize(QtCore.QSize(95, 95))
        self.rightButton.setObjectName("rightButton")
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)
        self.downleftButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.downleftButton.setMinimumSize(QtCore.QSize(50, 50))
        self.downleftButton.setMaximumSize(QtCore.QSize(75, 75))
        self.downleftButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"")
        self.downleftButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/down-left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.downleftButton.setIcon(icon7)
        self.downleftButton.setIconSize(QtCore.QSize(60, 60))
        self.downleftButton.setObjectName("downleftButton")
        self.gridLayout.addWidget(self.downleftButton, 2, 0, 1, 1)
        self.downButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.downButton.setMinimumSize(QtCore.QSize(50, 50))
        self.downButton.setMaximumSize(QtCore.QSize(75, 75))
        self.downButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/down-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.downButton.setIcon(icon8)
        self.downButton.setIconSize(QtCore.QSize(95, 95))
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)
        self.downrightButton = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.downrightButton.setMinimumSize(QtCore.QSize(50, 50))
        self.downrightButton.setMaximumSize(QtCore.QSize(75, 75))
        self.downrightButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downrightButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/down-right-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.downrightButton.setIcon(icon9)
        self.downrightButton.setIconSize(QtCore.QSize(60, 60))
        self.downrightButton.setObjectName("downrightButton")
        self.gridLayout.addWidget(self.downrightButton, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.page_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.upleftButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.upleftButton_2.setMinimumSize(QtCore.QSize(75, 75))
        self.upleftButton_2.setMaximumSize(QtCore.QSize(90, 90))
        self.upleftButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"QPushButton::hover {\n"
"    background: #D3D3D3;\n"
"    }\n"
"    \n"
"QPushButton::pressed{\n"
"    background: #C3C3C3;\n"
"    color: purple;\n"
"    }\n"
"\n"
"")
        self.upleftButton_2.setText("")
        self.upleftButton_2.setIcon(icon9)
        self.upleftButton_2.setIconSize(QtCore.QSize(60, 60))
        self.upleftButton_2.setObjectName("upleftButton_2")
        self.gridLayout_2.addWidget(self.upleftButton_2, 0, 0, 1, 1)
        self.upButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.upButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.upButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.upButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.upButton_2.setText("")
        self.upButton_2.setIcon(icon2)
        self.upButton_2.setIconSize(QtCore.QSize(95, 95))
        self.upButton_2.setObjectName("upButton_2")
        self.gridLayout_2.addWidget(self.upButton_2, 0, 1, 1, 1)
        self.uprightButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.uprightButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.uprightButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.uprightButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.uprightButton_2.setText("")
        self.uprightButton_2.setIcon(icon7)
        self.uprightButton_2.setIconSize(QtCore.QSize(60, 60))
        self.uprightButton_2.setObjectName("uprightButton_2")
        self.gridLayout_2.addWidget(self.uprightButton_2, 0, 2, 1, 1)
        self.leftButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.leftButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.leftButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.leftButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.leftButton_2.setText("")
        self.leftButton_2.setIcon(icon4)
        self.leftButton_2.setIconSize(QtCore.QSize(95, 95))
        self.leftButton_2.setObjectName("leftButton_2")
        self.gridLayout_2.addWidget(self.leftButton_2, 1, 0, 1, 1)
        self.autocutButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.autocutButton_2.setMinimumSize(QtCore.QSize(75, 75))
        self.autocutButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.autocutButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    \n"
"    }")
        self.autocutButton_2.setText("")
        self.autocutButton_2.setIcon(icon5)
        self.autocutButton_2.setIconSize(QtCore.QSize(80, 80))
        self.autocutButton_2.setObjectName("autocutButton_2")
        self.gridLayout_2.addWidget(self.autocutButton_2, 1, 1, 1, 1)
        self.rightButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.rightButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.rightButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.rightButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.rightButton_2.setText("")
        self.rightButton_2.setIcon(icon6)
        self.rightButton_2.setIconSize(QtCore.QSize(95, 95))
        self.rightButton_2.setObjectName("rightButton_2")
        self.gridLayout_2.addWidget(self.rightButton_2, 1, 2, 1, 1)
        self.downleftButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.downleftButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.downleftButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.downleftButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }\n"
"")
        self.downleftButton_2.setText("")
        self.downleftButton_2.setIcon(icon3)
        self.downleftButton_2.setIconSize(QtCore.QSize(60, 60))
        self.downleftButton_2.setObjectName("downleftButton_2")
        self.gridLayout_2.addWidget(self.downleftButton_2, 2, 0, 1, 1)
        self.downButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.downButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.downButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.downButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downButton_2.setText("")
        self.downButton_2.setIcon(icon8)
        self.downButton_2.setIconSize(QtCore.QSize(95, 95))
        self.downButton_2.setObjectName("downButton_2")
        self.gridLayout_2.addWidget(self.downButton_2, 2, 1, 1, 1)
        self.downrightButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.downrightButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.downrightButton_2.setMaximumSize(QtCore.QSize(75, 75))
        self.downrightButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #000000;\n"
"    border-radius: 37px;\n"
"    }")
        self.downrightButton_2.setText("")
        self.downrightButton_2.setIcon(icon1)
        self.downrightButton_2.setIconSize(QtCore.QSize(60, 60))
        self.downrightButton_2.setObjectName("downrightButton_2")
        self.gridLayout_2.addWidget(self.downrightButton_2, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuOpen = QtGui.QAction(parent=MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/add-image.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuOpen.setIcon(icon10)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtGui.QAction(parent=MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("g:\\Alan\\PyCut\\dist\\app\\uic\\../icon/save-image.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuSave.setIcon(icon11)
        self.menuSave.setObjectName("menuSave")
        self.menuSaveAs = QtGui.QAction(parent=MainWindow)
        self.menuSaveAs.setObjectName("menuSaveAs")
        self.menuSOP = QtGui.QAction(parent=MainWindow)
        self.menuSOP.setObjectName("menuSOP")
        self.menuFile.addAction(self.menuOpen)
        self.menuFile.addAction(self.menuSave)
        self.menuFile.addAction(self.menuSaveAs)
        self.menuHelp.addAction(self.menuSOP)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.menuOpen)
        self.toolBar.addAction(self.menuSave)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PiCut"))
        self.label.setText(_translate("MainWindow", "Contrast"))
        self.nameLabel_2.setText(_translate("MainWindow", "x"))
        self.xValue.setText(_translate("MainWindow", "0"))
        self.nameLabel_3.setText(_translate("MainWindow", "y"))
        self.yValue.setText(_translate("MainWindow", "0"))
        self.nameLabel_4.setText(_translate("MainWindow", "Pixel"))
        self.pixelValue.setText(_translate("MainWindow", "0"))
        self.chooseButton.setText(_translate("MainWindow", "Enlarge "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Color"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuOpen.setText(_translate("MainWindow", "Open.."))
        self.menuSave.setText(_translate("MainWindow", "Save ..."))
        self.menuSave.setToolTip(_translate("MainWindow", "Save.."))
        self.menuSaveAs.setText(_translate("MainWindow", "Save As..."))
        self.menuSOP.setText(_translate("MainWindow", "SOP"))
from ImageWidget import ImageWidget
