from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main.lib.worker import Worker
import sys, os


class PopupDSTDS(QMainWindow):
    def __init__(self, dsm):
        super().__init__()
        
        self.setWindowTitle("Warning")
        self.dsm=dsm
        self.initUI()
        
    def initUI(self):
        message_box=QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setText("Missing Dedicated Server!")
        message_box.setInformativeText("Do you want to download it?")
        
        button_no=message_box.addButton(QMessageBox.No)
        button_yes=message_box.addButton(QMessageBox.Yes)
        
        button_yes.clicked.connect(self.click_yes_callback)
        button_no.clicked.connect(self.click_no_callback)
        
        self.setCentralWidget(message_box)
        
    def on_finish(self):
        self.close()
        self.dsm.enable_window()
        
    def update_progress(self, percent):
        self.percent_box.setText("{:3d}%".format(percent))

    def click_yes_callback(self):
        self.thread = QThread()
        self.size_thread = QThread()
        
        print(self.thread, self.size_thread)

        self.worker = Worker(self.dsm)
        self.worker.moveToThread(self.thread)
        self.size_worker = Worker(self.dsm)
        self.size_worker.moveToThread(self.size_thread)

        self.thread.started.connect(self.worker.get_dstds)
        self.size_thread.started.connect(self.size_worker.get_dstds_size)

        self.worker.finished.connect(self.thread.quit)
        self.size_worker.finished.connect(self.size_thread.quit)

        self.worker.finished.connect(self.worker.deleteLater)
        self.size_worker.finished.connect(self.size_worker.deleteLater)
        
        self.thread.finished.connect(self.thread.deleteLater)
        self.size_thread.finished.connect(self.size_thread.deleteLater)
        
        self.thread.finished.connect(self.on_finish)
        
        self.size_worker.progress.connect(self.update_progress)
        
        self.thread.start()
        self.size_thread.start()
        
        self.label_box=QLabel()
        self.label_box.setAlignment(Qt.AlignCenter)
        self.label_box.setText("Downloading Dedicated Server...")
        
        self.percent_box=QLabel()
        self.percent_box.setAlignment(Qt.AlignCenter)
        self.percent_box.setText("{:3d}%".format(0))
        
        self.gif_box=QLabel()
        self.gif_box.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(os.path.join('images', 'loading_small.gif'))
        self.gif_box.setMovie(self.movie)
        self.movie.start()
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.label_box,0,0)
        self.layout.addWidget(self.percent_box,1,0)
        self.layout.addWidget(self.gif_box,2,0)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def click_no_callback(self):
        self.dsm.load_popup_error("Don't Starve Together Dedicated Server is required. Terminating")
        self.close()
        
    def closeEvent(self, event):
        if not self.dsm.validator.check_for_steamcmd():
            self.click_no_callback()
        
