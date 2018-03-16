from Sources.Point import *

class FileReader:
    def __init__(self, filename):
        self.__filename = open(filename)
        self.__maze_map = []

    def read(self):
        file = self.__filename.read().split('\n')
        for var in file:
            point = Point()
            var = var.split()
            point.x = var[0]
            point.y = var[1]

            if var.__len__() == 3:
                if 'P' in var[2]:
                    point.right_wall = True
                if 'D' in var[2]:
                    point.buttom_wall = True

            self.__maze_map.append(point)

    def get_map(self):
        return self.__maze_map

    def print_map(self):
        for point in self.__maze_map:
            print("(" + point.x + "," + point.y + ") - P: " + str(point.right_wall) + " D: " + str(point.buttom_wall) + "\n")
