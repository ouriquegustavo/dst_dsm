from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
        
class GUINoCMD():
    def __init__(self, dsm):
        self.dsm=dsm
        self.gui={}
        self.app=QApplication([])
        self.layout=QWidget()
        #self.style='Fusion'
        #self.app.setStyle(QStyleFactory.create(self.style))

#        self.label=QLabel("My text")
#        self.layout.resize(600,600)
        
#        self.layout.addWidget(self.label)
        
        #self.button=QPushButton(self.window)
#        self.layout.addWidget(self.label)
        
#        self.layout.show()
        
        #self.load_steamcmd()
        #self.load_gui_main()
        #self.load_gui_nocmd()
        pass
        
        
    def clear_gui(self):
        for i in range(len(self.window.children())): 
            self.window.children()[i].deleteLater()
        
    def load_gui_main(self):
        if not 'main' in self.gui:
            self.gui['main']=GUIMain(self)
        self.gui['main'].show()
        return self.gui['main']
        
    def load_gui_nocmd(self):
        if not 'nocmd' in self.gui:
            self.gui['nocmd']=GUINoCMD(self)
        self.gui['nocmd'].show()
        return self.gui['nocmd']
        
    def load_steamcmd(self):
        self.steamcmd=SteamCMD(self)
