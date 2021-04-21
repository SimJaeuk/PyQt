import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)
    
    def inquiry(self):
        BTC = pyupbit.get_current_price("KRW-BTC")
        ETH = pyupbit.get_current_price("KRW-ETH")
        self.lineEdit.setText(str(BTC))
        self.lineEdit_2.setText(str(ETH))
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()