from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main.lib.worker import Worker
import sys, os


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
        
    def on_finish(self):
        self.close()
        if not self.dsm.validator.check_for_dstds():
            self.dsm.load_popup_dstds()
        else:
            self.dsm.enable_window()
        
    def click_yes_callback(self):
        self.thread = QThread()
        self.worker = Worker(self.dsm)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.get_steamcmd)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.on_finish)
        self.thread.start()
        label_box=QLabel()
        label_box.setAlignment(Qt.AlignCenter)
        label_box.setText("Downloading SteamCMD...")
        
        gif_box=QLabel()
        gif_box.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(os.path.join('images', 'loading_small.gif'))
        gif_box.setMovie(self.movie)
        self.movie.start()
        
        layout = QGridLayout()
        layout.addWidget(label_box,0,0)
        layout.addWidget(gif_box,1,0)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        

    def click_no_callback(self):
        self.dsm.load_popup_error("SteamCMD is required for Don't Starve Together Dedicated Server.")
        self.close()
        
    def closeEvent(self, event):
        if not self.dsm.validator.check_for_steamcmd():
            self.click_no_callback()
        
