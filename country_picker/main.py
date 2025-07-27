"""
Main window for country_picker.
"""
import sys
from typing import Optional
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QLabel,
)
from country_picker.api import get_country_names

# --- Worker for background tasks ---
class Worker(QObject):
    """
    Worker object to perform tasks in a separate thread.
    Fetches country data without freezing the GUI.
    """
    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def run(self):
        """Fetches country data and emits a signal with the result."""
        try:
            countries = get_country_names()
            self.finished.emit(countries)
        except Exception as e:
            self.error.emit(str(e))

class MainWindow(QMainWindow):
    """
    The main application window.
    """
    def __init__(self, preselected_country: Optional[str] = None):
        super().__init__()

        # Store the country to pre-select
        self.preselected_country = preselected_country

        self.setWindowTitle("Country Picker")
        self.setGeometry(100, 100, 400, 100) # x, y, width, height

        # Central Widget and Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Widgets
        self.country_combo = QComboBox()
        self.country_combo.setPlaceholderText("Loading countries...")
        self.country_combo.setEnabled(False) # Disable until populated

        self.result_label = QLabel("Selected: None")

        # Add widgets to layout
        layout.addWidget(self.country_combo)
        layout.addWidget(self.result_label)

        self.country_combo.currentIndexChanged.connect(self.update_selection_label)

        # Setup threading for loading countries
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.populate_combobox)
        self.worker.error.connect(self.on_load_error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def populate_combobox(self, countries: list):
        """
        Slot to populate the combobox and set the pre-selected country.
        """
        if not countries:
            self.result_label.setText("Error: Could not load countries.")
            self.country_combo.setPlaceholderText("Failed to load")
            return

        self.country_combo.addItems(countries)
        self.country_combo.setEnabled(True)
        self.country_combo.setPlaceholderText("Select a country")
        self.country_combo.setCurrentIndex(-1)

        # --- Handle pre-selection ---
        if self.preselected_country:
            # Find index for the preselected country (case-insensitive)
            # (Increases user friendliness eg. switzerland just works)
            try:
                # Create a lowercase list to find index
                countries_lower = [c.lower() for c in countries]
                idx = countries_lower.index(self.preselected_country.lower())
                self.country_combo.setCurrentIndex(idx)
            except ValueError:
                # Country name not in list
                print(f"Warning: Country '{self.preselected_country}' not found.")

    def on_load_error(self, error_msg: str):
        """Slot to handle errors from the worker thread."""
        print(f"An error occurred in the worker thread: {error_msg}")
        self.result_label.setText("Error: Could not load countries.")
        self.country_combo.setPlaceholderText("Failed to load")

    def update_selection_label(self, index: int):
        """
        Slot to update the label when the combobox selection changes.
        """
        if index != -1:
            country_name = self.country_combo.currentText()
            self.result_label.setText(f"Selected: {country_name}")

def run(selected_country: Optional[str] = None):
    """Initializes and runs the QApplication."""
    app = QApplication(sys.argv)
    # Pass argument to MainWindow
    window = MainWindow(preselected_country=selected_country)
    window.show()
    sys.exit(app.exec())