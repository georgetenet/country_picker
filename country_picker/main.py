"""
Main window for country_picker.
"""
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QLabel,
)

class MainWindow(QMainWindow):
    """
    Contains combobox for country selection and a label to display
    user's choice.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Country Picker")
        self.setGeometry(100, 100, 400, 100) # x, y, width, height

        # Central Widget and Layout=
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Widgets
        self.country_combo = QComboBox()
        self.country_combo.setPlaceholderText("Loading countries...")
        self.country_combo.setEnabled(False) # Disable untill populated

        self.result_label = QLabel("Selected: None")

        # Add widgets to layout
        layout.addWidget(self.country_combo)
        layout.addWidget(self.result_label)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
