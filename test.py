from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QDoubleSpinBox, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QSlider and QDoubleSpinBox Connection")
        self.setGeometry(100, 100, 400, 100)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        slider = QSlider(Qt.Orientation.Horizontal)
        spin_box = QDoubleSpinBox()

        # Connect the valueChanged signal of the slider to update the spin box
        slider.valueChanged.connect(lambda value: spin_box.setValue(value / 10.0))

        # Connect the valueChanged signal of the spin box to update the slider
        spin_box.valueChanged.connect(lambda value: slider.setValue(int(value * 10)))

        layout.addWidget(slider)
        layout.addWidget(spin_box)

        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
