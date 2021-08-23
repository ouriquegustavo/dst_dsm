from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from main.gui_main import GUIMain
from main.gui_nocmd import GUINoCMD
from main.steamcmd import SteamCMD
from main.window import Window
from main.popup_steamcmd import PopupSteamCMD
from main.popup_error import PopupError
import os
import sys

class DSTDSM():
    def __init__(self):
        self.platform=sys.platform
        self.path_steamcmd="steamcmd_{}".format(self.platform)
        self.path_worlds="worlds"
        self.path_dstds="dedicated_server"
        self.windows={}
        self.app=QApplication([])
        self.style='Fusion'
        self.app.setStyle(QStyleFactory.create(self.style))
        
        self.steamcmd=SteamCMD(self)
        
        self.load_window()
        self.disable_window()
        if not self.steamcmd.check_for_steamcmd():
            self.load_popup_steamcmd()
        else:
            self.enable_window()
        
    def clear_gui(self):
        for i in range(len(self.window.children())): 
            self.window.children()[i].deleteLater()
            
    def load_window(self):
        self.window=Window(self)
        self.windows['window']=self.window
        self.window.show()
        
    def load_popup_steamcmd(self):
        self.popup_steamcmd=PopupSteamCMD(self)
        self.popup_steamcmd.show()
        
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
