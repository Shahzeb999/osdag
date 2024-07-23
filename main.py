
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QPushButton, QLabel
from PyQt5.QtCore import Qt
from OCC.Display.backend import load_backend
from OCC.Display.qtDisplay import qtViewer3d
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from prism_calculator import PrismCalculator
import sqlite3

load_backend("qt-pyqt5")

class PrismViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Rectangular Prism Viewer")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Left panel for controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self.prism_selector = QComboBox()
        self.prism_selector.currentIndexChanged.connect(self.update_prism_info)
        left_layout.addWidget(QLabel("Select Prism:"))
        left_layout.addWidget(self.prism_selector)

        self.surface_area_label = QLabel("Surface Area: ")
        self.volume_label = QLabel("Volume: ")
        left_layout.addWidget(self.surface_area_label)
        left_layout.addWidget(self.volume_label)

        self.visualize_button = QPushButton("Visualize 3D Model")
        self.visualize_button.clicked.connect(self.visualize_prism)
        left_layout.addWidget(self.visualize_button)

        left_layout.addStretch()

        # Right panel for 3D viewer
        self.viewer = qtViewer3d(self)
        self.viewer.InitDriver()

        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(self.viewer, 3)

        self.load_prisms_from_db()

    def load_prisms_from_db(self):
        conn = sqlite3.connect('prisms.db')
        cursor = conn.cursor()
        cursor.execute("SELECT designation FROM prisms")
        prisms = cursor.fetchall()
        conn.close()

        self.prism_selector.addItems([prism[0] for prism in prisms])

    def update_prism_info(self):
        designation = self.prism_selector.currentText()
        conn = sqlite3.connect('prisms.db')
        cursor = conn.cursor()
        cursor.execute("SELECT length, width, height FROM prisms WHERE designation = ?", (designation,))
        prism_data = cursor.fetchone()
        conn.close()

        if prism_data:
            length, width, height = prism_data
            surface_area = PrismCalculator.calculate_surface_area(length, width, height)
            volume = PrismCalculator.calculate_volume(length, width, height)

            self.surface_area_label.setText(f"Surface Area: {surface_area:.2f}")
            self.volume_label.setText(f"Volume: {volume:.2f}")

    def visualize_prism(self):
        designation = self.prism_selector.currentText()
        conn = sqlite3.connect('prisms.db')
        cursor = conn.cursor()
        cursor.execute("SELECT length, width, height FROM prisms WHERE designation = ?", (designation,))
        prism_data = cursor.fetchone()
        conn.close()

        if prism_data:
            length, width, height = prism_data
            box = BRepPrimAPI_MakeBox(length, width, height).Shape()
            self.viewer.DisplayShape(box, update=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PrismViewer()
    viewer.show()
    sys.exit(app.exec_())
