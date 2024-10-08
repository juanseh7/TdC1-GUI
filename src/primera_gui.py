import sys
from src.ui.primera_gui import *
from src.csv import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLineEdit

class MyButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)
        self.clicked.connect(lambda: self.select_file(self.parent()))  # Connect the click event to the select_file method
        self.setFixedSize(170, 71)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            file_path = url.toLocalFile()
            line_edit = self.parent().findChild(QLineEdit, "fileLineEdit")
            if line_edit:
                line_edit.setText(file_path)

    def select_file(self, parent):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(parent, "Select File", "", "All Files (*);;CSV Files (*.csv)", options=options)
        if file_path:
            line_edit = parent.findChild(QLineEdit, "fileLineEdit")
            if line_edit:
                line_edit.setText(file_path)

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI
        self.initUI()

    def initUI(self):
        # Replace the existing button with the new one to support drag-and-drop
        self.selectFileButton = MyButton("Select or Drop File Here", self)
        self.selectFileButton.move(90, 39)  # Adjust the position if needed

        self.selectV1Multiplier.setValue(1.0)
        self.selectV2Multiplier.setValue(1.0)
        self.selectV3Multiplier.setValue(1.0)
        self.selectV4Multiplier.setValue(1.0)

        # Connect the confirm button to the confirm function
        self.confirmButton.clicked.connect(self.confirm)

    # def select_file(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.ReadOnly
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;CSV Files (*.csv)", options=options)
    #     if file_path:
    #         self.selectFileButton.setText(file_path)  # Display the file path on the button

    def confirm(self):
        file_path = self.fileLineEdit.text()

        v1Port = self.selectV1Port.value()
        v2Port = self.selectV2Port.value()
        v3Port = self.selectV3Port.value()
        v4Port = self.selectV4Port.value()

        v1Offset = self.selectV1Offset.value()
        v2Offset = self.selectV2Offset.value()
        v3Offset = self.selectV3Offset.value()
        v4Offset = self.selectV4Offset.value()

        v1Multiplier = self.selectV1Multiplier.value()
        v2Multiplier = self.selectV2Multiplier.value()
        v3Multiplier = self.selectV3Multiplier.value()
        v4Multiplier = self.selectV4Multiplier.value()

        graph_csv(file_path, v1Port, v2Port, v3Port, v4Port, v1Offset, v2Offset, v3Offset, v4Offset, v1Multiplier, v2Multiplier, v3Multiplier, v4Multiplier)
        # Add your confirmation logic here (e.g., process the file and number)