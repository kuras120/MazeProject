from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Sources.FileReader import *
from Sources.WallFollower import *

class InitUI(QMainWindow):
    """
    Klasa odpowiedzialna za GUI
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QMainWindow.resize(self, 1000, 1000)

    def paintEvent(self, a0: QtGui.QPaintEvent):
        """
        :param a0: rodzaj eventu (rysowanie)
        :return: none
        Rysuje labirynt oraz sciezke przejscia bota przez niego
        """
        reader = FileReader("TestFiles/FullMazeData.txt")
        reader.read()
        maze_map = reader.get_map()

        algorithm = WallFollower(maze_map)
        algorithm.refactor_map()
        algorithm.fill_interaction()
        algorithm.calculate_path()
        algorithm.print_output()
        output = algorithm.get_output()

        multiplier = 7
        move = 50

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.black))

        '''
        Rysowanie labiryntu
        '''
        for var in maze_map:
            if var.right_wall:
                painter.drawLine(move + int(var.x)*multiplier, move + int(var.y)*multiplier, move + int(var.x)*multiplier + multiplier, move + int(var.y)*multiplier)
            if var.bottom_wall:
                painter.drawLine(move + int(var.x)*multiplier, move + int(var.y)*multiplier, move + int(var.x)*multiplier, move + int(var.y)*multiplier + multiplier)

        var = maze_map[maze_map.__len__()-1]
        painter.drawLine(move, move + int(var.y)*multiplier + multiplier, move + int(var.x)*multiplier, move + int(var.y)*multiplier + multiplier)
        painter.drawLine(move + int(var.x)*multiplier + multiplier, move, move + int(var.x)*multiplier + multiplier, move + int(var.y)*multiplier)

        painter.setBrush(QtGui.QBrush(QtCore.Qt.green))

        '''
        Rysowanie sciezki przejscia
        '''
        for i in range(1, output.__len__()):
            painter.drawRect(move + int(output[i-1].x) * multiplier, move + int(output[i-1].y) * multiplier, 4, 4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = InitUI()
    main_screen.setWindowTitle("Maze Project 1")
    main_screen.show()

    sys.exit(app.exec())
