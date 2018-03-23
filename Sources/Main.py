from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Sources.FileReader import *
from Sources.WallFollower import *

class InitUI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QMainWindow.resize(self, 900, 900)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black))

        reader = FileReader("TestFiles/FullMazeData.txt")
        reader.read()
        maze_map = reader.get_map()
        #reader.print_map()

        algorithm = WallFollower(maze_map)
        algorithm.refactor_map()
        #algorithm.print_coords()
        algorithm.fill_interaction()
        #algorithm.print_interactions()
        #algorithm.calculate_path()
        #algorithm.print_output()

        multiplier = 5
        move = 100

        for var in maze_map:
            if var.right_wall:
                painter.drawLine(move + int(var.x)*multiplier, move + int(var.y)*multiplier, move + int(var.x)*multiplier + multiplier, move + int(var.y)*multiplier)
            if var.buttom_wall:
                painter.drawLine(move + int(var.x)*multiplier, move + int(var.y)*multiplier, move + int(var.x)*multiplier, move + int(var.y)*multiplier + multiplier)

        var = maze_map[maze_map.__len__()-1]
        painter.drawLine(move, move + int(var.y)*multiplier + multiplier, move + int(var.x)*multiplier, move + int(var.y)*multiplier + multiplier)
        painter.drawLine(move + int(var.x)*multiplier + multiplier, move, move + int(var.x)*multiplier + multiplier, move + int(var.y)*multiplier)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = InitUI()
    main_screen.setWindowTitle("Maze Project 1")
    main_screen.show()

    sys.exit(app.exec())
