from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PySide2.QtUiTools import QUiLoader
from ui.mainwindow import Ui_MainWindow
# from source.ui.qtwidgets_testing.qt_creator.generated_python_files.MainWindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # start the event loop
    app.exec_()