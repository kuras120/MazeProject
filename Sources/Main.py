from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Sources.FileReader import *

class InitUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QMainWindow.resize(self, 650, 650)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black))

        reader = FileReader("TestFiles/FullMazeData.txt")
        reader.read()
        maze_map = reader.get_map()

        multiplier = 5

        for var in maze_map:
            print("BENIZ")
            if var.right_wall:
                painter.drawLine(int(var.x)*multiplier, int(var.y)*multiplier, int(var.x)*multiplier + multiplier, int(var.y)*multiplier)
            if var.buttom_wall:
                painter.drawLine(int(var.x)*multiplier, int(var.y)*multiplier, int(var.x)*multiplier, int(var.y)*multiplier + multiplier)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = InitUI()
    main_screen.setWindowTitle("Maze Project 1")
    main_screen.show()

    sys.exit(app.exec())
