from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal, QEvent
from PyQt6.QtGui import QMouseEvent

class ClickableLabel(QLabel): 
    clicked=pyqtSignal(str)
    enter = pyqtSignal(QEvent)
    leave = pyqtSignal(QEvent)
    def __init__(self, text):
        super().__init__(text)
        self.text = text
    def mousePressEvent(self, ev):
        self.clicked.emit(self.text)
    def enterEvent(self, ev):
        self.setStyleSheet('QLabel {color: blue}')
    def leaveEvent(self, ev):
        self.setStyleSheet('QLabel {color: black}')