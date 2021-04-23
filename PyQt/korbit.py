import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit
import pykorbit

form_class = uic.loadUiType("PyQt/untitled.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)
    
    # def btn_clicked(self):
    #     print("버튼 클릭")
    
    def inquiry(self):
        BTC = pykorbit.get_current_price("BTC")
        ETH = pykorbit.get_current_price("ETH")
        self.lineEdit.setText(str(BTC))
        self.lineEdit_2.setText(str(ETH))
        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()