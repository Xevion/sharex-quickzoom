from PyQt5 import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow
from ui.aboutform import Ui_AboutForm
import sys

class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_AboutForm()
        self.ui.setupUi(self)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.aboutui = AboutWindow()
        self.ui.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.ui.graphicsView.viewport().installEventFilter(self)
        # About tab
        self.ui.actionAbout.triggered.connect(lambda : self.aboutui.show())
        self.show()
    
    def eventFilter(self, source, e):
        if e.type() == QtCore.QEvent.MouseMove:
            if e.buttons() == QtCore.Qt.NoButton:
                pass
            elif e.buttons() == QtCore.Qt.LeftButton:
                pass
            elif e.buttons() == QtCore.Qt.RightButton:
                pass
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            if e.button() == QtCore.Qt.LeftButton:
                print(f'Left Click at ({e.x()}, {e.y()})')
            elif e.button() == QtCore.Qt.RightButton:
                print(f'Right Click at ({e.x()}, {e.y()})')
        return super(Window, self).eventFilter(source, e)

def run():
    app = QtWidgets.QApplication([])
    window = Window()
    sys.exit(app.exec_())

run()