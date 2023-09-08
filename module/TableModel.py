from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets, QtCore, QtGui
import numpy as np

colors = ["#034D6D","#06567A","#095D87","#0D6493","#116B9E","#1771A9","#1C77B3","#227DBD","#2982C6","#3391C9","#3E9FCC","#48ACCF","#52B8D2","#5CC3D5","#67CED8","#71D7DB","#7BDEDB","#86E0D9"]
class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # Note: self._data[index.row()][index.column()] will also work
            value = self._data[index.row(), index.column()]
            return str(value)
        elif role == Qt.ItemDataRole.BackgroundRole:
            value = self._data[index.row(), index.column()]
            if isinstance(value, (int, float)):
                value = int(value/15)
                return QtGui.QColor(colors[value])
            elif isinstance(value, np.uint8):
                value = int(int(value)/15)
                return QtGui.QColor(colors[value])

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]