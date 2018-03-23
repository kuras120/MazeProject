from Sources.Point import *


class FileReader:
    """
    :type filename: object
    :param filename: zczytanie zawartosci pliku
    :type maze_map: tuple
    :param maze_map: wczytanie listy punktow do tworzenia labiryntu
    :return: none
    """
    def __init__(self, filename):
        self.__filename = open(filename)
        self.__maze_map = []

    def read(self):
        """
        :return: none
        Wczytanie zawartosci pliku i dodanie do listy
        """
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
                    point.bottom_wall = True

            self.__maze_map.append(point)

    def get_map(self):
        """
        :return maze_map: mapa punktow labiryntu
        """
        return self.__maze_map

    def print_map(self):
        """
        :return: none
        """
        for point in self.__maze_map:
            print("(" + point.x + "," + point.y + ") - P: " + str(point.right_wall) + " D: " + str(point.bottom_wall) + "\n")
