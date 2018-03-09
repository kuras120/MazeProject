from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class InitUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QMainWindow.resize(self, 800, 600)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red))
        painter.drawRect(100, 100, 600, 400)
        painter.drawLine(200, 300, 250, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = InitUI()
    main_screen.setWindowTitle("Maze Project 1")
    main_screen.show()
    sys.exit(app.exec())
