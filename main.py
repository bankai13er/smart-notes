from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import *
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()