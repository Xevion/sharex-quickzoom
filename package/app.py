from PyQt5 import QtWidgets, QtCore, QtGui
from ui.mainwindow import Ui_MainWindow
from ui.aboutform import Ui_AboutForm
import sys
from PIL import Image, ImageQt

# Simple About Window class
class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_AboutForm()
        self.ui.setupUi(self)

# Custom GraphicsScene
class GraphicsScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsScene.__init__(self, parent)
        # Mysterious suff stuff that fixes it
        self.setSceneRect(-100, -100, 200, 200)
        # Dimensions
        self.x, self.y = 30, 30

    def mouseMoveEvent(self, event):
        self.clear()
        x = event.scenePos().x()
        y = event.scenePos().y()
        self.addRect(x-(self.x // 2), y - (self.y // 2), self.x, self.y, QtCore.Qt.black)
        # self.addRect(QtCore.QRectF(QtCore.QPointF(x, y), QtCore.QSizeF(10, 10)), QtCore.Qt.black)
        # self.addEllipse(x-2, y-2, 4, 4, QtCore.Qt.black, QtGui.QBrush(QtCore.Qt.black))

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.aboutui = AboutWindow()
        self.ui.setupUi(self)
        self.initUI()

        self.ui.scene = GraphicsScene()
        self.ui.graphicsView.setScene(self.ui.scene)
        print(dir(self.ui.scene))

        # self.ui.graphicsView = QtWidgets.QGraphicsView(self.ui.scene)
        # self.ui.graphicsView.setGeometry(QtCore.QRect(20, 10, 571, 400))
        # self.ui.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        # self.ui.graphicsView.setMouseTracking(True)
        # self.ui.graphicsView.setObjectName("graphicsView")

    
    def initUI(self):
        self.ui.graphicsView.viewport().installEventFilter(self)
        # About tab
        self.ui.actionAbout.triggered.connect(lambda : self.aboutui.show())
        self.show()
        self.pen = QtCore.Qt.black
        self.img = ImageQt.ImageQt(Image.open('ui/images/sharex.png'))
        
    def redraw(self, event):
        return
        self.ui.scene.clear()
        # Draw Rect
        import random
        r = QtCore.QRectF(QtCore.QPointF(event.x(), event.y()), QtCore.QSizeF(10, 10))
        self.ui.scene.addRect(r, self.pen)
        pixMap = QtGui.QPixmap.fromImage(self.img)
        self.ui.scene.addPixmap(pixMap)
    
    def eventFilter(self, source, e):
        if e.type() == QtCore.QEvent.MouseMove:
            if e.buttons() == QtCore.Qt.NoButton:
                self.redraw(e)
            elif e.buttons() == QtCore.Qt.LeftButton:
                pass
            elif e.buttons() == QtCore.Qt.RightButton:
                pass
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            if e.button() == QtCore.Qt.LeftButton:
                pass
            elif e.button() == QtCore.Qt.RightButton:
                pass
        return super(Window, self).eventFilter(source, e)

def run():
    app = QtWidgets.QApplication([])
    window = Window()
    sys.exit(app.exec_())

run()