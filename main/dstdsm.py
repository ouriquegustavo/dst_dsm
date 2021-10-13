from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from main.lib.validator import Validator
from main.window.main_window import MainWindow
from main.window.popup_steamcmd import PopupSteamCMD
from main.window.popup_dstds import PopupDSTDS
from main.window.popup_error import PopupError
import os
import sys

class DSTDSM():
    def __init__(self):
        self.platform=sys.platform
        self.arch=sys.maxsize > 0x100000000
        self.path_steamcmd="steamcmd"
        self.path_worlds="worlds"
        self.path_dstds="dedicated_server"
        self.app=QApplication([])
        self.style='Fusion'
        self.app.setStyle(QStyleFactory.create(self.style))
        
        self.validator=Validator(self)
        
        self.load_window()
        self.disable_window()
        if not self.validator.check_for_steamcmd():
            self.load_popup_steamcmd()
        elif not self.validator.check_for_dstds():
            self.load_popup_dstds()
        else:
            self.enable_window()
        
    def clear_gui(self):
        for i in range(len(self.window.children())): 
            self.window.children()[i].deleteLater()
            
    def load_window(self):
        self.window=MainWindow(self)
        self.window.show()
        
    def load_popup_steamcmd(self):
        self.popup_steamcmd=PopupSteamCMD(self)
        self.popup_steamcmd.show()
        
    def load_popup_dstds(self):
        self.popup_dstds=PopupDSTDS(self)
        self.popup_dstds.show()
        
    def load_popup_error(self, message):
        self.popup_error=PopupError(self,message)
        self.popup_error.show()
        
    def disable_window(self):
        self.window.setEnabled(False)
        
    def enable_window(self):
        self.window.setEnabled(True)
        
    def close_all_windows(self):
        self.app.closeAllWindows()        
        
    def load_steamcmd(self):
        self.steamcmd=SteamCMD(self)
