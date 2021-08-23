from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class PopupError(QMainWindow):
    def __init__(self, dsm, message):
        super().__init__()
        
        self.setWindowTitle("Error")
        self.dsm=dsm
        self.message=message

        self.initUI()

    def initUI(self):
        message_box=QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText("Error")
        message_box.setInformativeText(self.message)
        message_box.buttonClicked.connect(self.click_callback)
        self.setCentralWidget(message_box)
        
    def click_callback(self):
        self.dsm.close_all_windows()
        
    def closeEvent(self, event):
        self.dsm.close_all_windows()
