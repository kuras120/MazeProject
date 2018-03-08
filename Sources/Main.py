from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class UiMainWindow(object):
    def setup_ui(self, QMainWindow):
        QMainWindow.resize(1024, 768)

class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red))
        painter.drawLine(200, 300, 250, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = MainScreen()
    main_screen.setWindowTitle("Maze Project 1")
    main_screen.show()
    sys.exit(app.exec())
