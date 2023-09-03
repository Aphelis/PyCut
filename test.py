import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QVBoxLayout, QStackedWidget

class InterchangeableGridLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Interchangeable GridLayout Example")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create two QGridLayouts
        self.grid_layout_1 = QGridLayout()
        self.grid_layout_2 = QGridLayout()

        # Add widgets to the first layout
        self.button1_1 = QPushButton("Button 1-1")
        self.button1_2 = QPushButton("Button 1-2")
        self.grid_layout_1.addWidget(self.button1_1, 0, 0)
        self.grid_layout_1.addWidget(self.button1_2, 0, 1)

        # Add widgets to the second layout
        self.button2_1 = QPushButton("Button 2-1")
        self.button2_2 = QPushButton("Button 2-2")
        self.grid_layout_2.addWidget(self.button2_1, 0, 0)
        self.grid_layout_2.addWidget(self.button2_2, 1, 0)

        # Create a QStackedWidget to hold the layouts
        self.stacked_widget = QStackedWidget(self.central_widget)
        self.stacked_widget.addWidget(QWidget())  # Placeholder for layout 0
        self.stacked_widget.addWidget(QWidget())  # Placeholder for layout 1

        # Set the layouts to the placeholder widgets in the QStackedWidget
        self.stacked_widget.widget(0).setLayout(self.grid_layout_1)
        self.stacked_widget.widget(1).setLayout(self.grid_layout_2)

        # Create a button to switch between layouts
        self.switch_button = QPushButton("Switch Layouts", self.central_widget)
        self.switch_button.clicked.connect(self.toggle_layouts)

        # Create a vertical layout to hold the QStackedWidget and the switch button
        self.vertical_layout = QVBoxLayout(self.central_widget)
        self.vertical_layout.addWidget(self.stacked_widget)
        self.vertical_layout.addWidget(self.switch_button)

        self.current_layout_index = 0  # Index of the currently displayed layout

    def toggle_layouts(self):
        self.current_layout_index = 1 - self.current_layout_index  # Toggle between 0 and 1
        self.stacked_widget.setCurrentIndex(self.current_layout_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InterchangeableGridLayoutExample()
    window.show()
    sys.exit(app.exec())