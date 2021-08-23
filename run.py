from PyQt5.QtWidgets import QApplication
from main.dstdsm import DSTDSM
import sys

if __name__ == "__main__":
    
    dstdsm=DSTDSM()
    sys.exit(dstdsm.app.exec_()) 
