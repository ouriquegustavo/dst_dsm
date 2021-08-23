from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class PopupSteamCMD(QMainWindow):
    def __init__(self, dsm):
        super().__init__()
        
        self.setWindowTitle("Warning")
        self.dsm=dsm
        self.initUI()
        
    def initUI(self):
        message_box=QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("Missing SteamCMD!")
        message_box.setInformativeText("Do you want to download it?")
        
        button_no=message_box.addButton(QMessageBox.No)
        button_yes=message_box.addButton(QMessageBox.Yes)
        
        button_yes.clicked.connect(self.click_yes_callback)
        button_no.clicked.connect(self.click_no_callback)
        
        self.setCentralWidget(message_box)
        
    def click_yes_callback(self):
        self.dsm.steamcmd.get_steamcmd()
        self.dsm.enable_window()
        self.close()

    def click_no_callback(self):
        self.dsm.load_popup_error("SteamCMD is required for Don't Starve Together Dedicated Server.")
        self.close()
        
    def closeEvent(self, event):
        if not self.dsm.steamcmd.check_for_steamcmd():
            self.click_no_callback()
        
