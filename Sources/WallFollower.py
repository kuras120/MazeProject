from Sources.Player import *


class WallFollower:
    """
    :type map: tuple
    :param map: lista z punktami mapy
    :type refactored_map: tuple
    :param refactored_map: dwuwymiarowa lista (wyszukwianie punktow po [x][y]
    :type player_interaction: tuple
    :param player_interaction: lista mozliwosci poruszania sie bota (uwzglednione punkty z mapy)
    :type output: tuple
    :param output: punkty przez ktore przeszedl bot (potrzebne do rysowania sciezki)
    :type temp_rotation: int
    :param temp_rotation: okresla w ktora strone obrocony jest bot w danym momencie
    :type go_x,go_y: int
    :param go_x,go_y: okreslaja przesuniecie w zaleznosci od obrotu bota
    :return: none
    """
    def __init__(self, maze_map):
        self.__map = deepcopy(maze_map)
        self.__refactored_map = []
        self.__player_interaction = []
        self.__output = []
        self.__temp_rotation = 0
        self.__go_x = 0
        self.__go_y = 0

    def refactor_map(self):
        """
        :return: none
        Zmiana na strukture dwuwymiarowa
        """
        for i in range(128):
            temp = []
            for j in range(128):
                temp.append(self.__map[i * 128 + j])

            self.__refactored_map.append(temp)

    def print_coords(self):
        for elem in self.__refactored_map:
            for elem1 in elem:
                print("x: " + elem1.x + " y: " + elem1.y + " right wall: " + str(elem1.right_wall))

    def fill_interaction(self):
        """
        :return: none
        Tworzenie mapy mozliwych ruchow dla bota (playera) - kazdy zawiera punkt odniesienia na mapie [wspol x][wspol y]
        Zawsze lewy gorny rog bota;
        """
        for i in range(128):
            temp = []
            for j in range(128):
                player = Player()
                player.point = self.__refactored_map[i][j]
                player.left = self.__refactored_map[i][j].right_wall
                player.bottom = self.__refactored_map[i][j].bottom_wall
                if j == 127 and not i == 127:
                    player.right = True
                    player.top = self.__refactored_map[i + 1][j].bottom_wall
                elif i == 127 and not j == 127:
                    player.top = True
                    player.right = self.__refactored_map[i][j + 1].right_wall
                elif i == 127 and j == 127:
                    player.top = True
                    player.right = True
                else:
                    player.top = self.__refactored_map[i + 1][j].bottom_wall
                    player.right = self.__refactored_map[i][j + 1].right_wall

                temp.append(player)
            self.__player_interaction.append(temp)

    def print_interactions(self):
        """
        :return: none
        """
        for i in range(128):
            for j in range(128):
                print("j: " + str(j))
                print("i: " + str(i))
                print("player left: " + str(self.__player_interaction[i][j].left) + " top: " + str(
                    self.__player_interaction[i][j].top) +
                      " right: " + str(self.__player_interaction[i][j].right) + " bottom: " + str(
                    self.__player_interaction[i][j].bottom))

    def calculate_path(self):
        """
        :return: none
        Wyliczenie calej sciezki przejscia przez bota\n
        Warunek konca to dotarcie do punktu (127 127)
        """
        k = 0
        temp = self.__player_interaction[0][0]  # poczatkowe polozenie
        while int(temp.point.x) != 127 or int(temp.point.y) != 127:
            temp.rotate_right(self.__temp_rotation) # rotacja poczatkowa do obliczen w danej chwili
            if not temp.left:
                self.rotation_add(3)
                temp.rotate_right(self.__temp_rotation)
                if not temp.top:
                    self.calculate_move(self.__temp_rotation)
                    temp = self.__player_interaction[int(temp.point.x) + self.__go_x][int(temp.point.y) + self.__go_y]
                    self.__output.append(temp.point)
            elif not temp.top:
                self.rotation_add(0)
                temp.rotate_right(self.__temp_rotation)
                self.calculate_move(self.__temp_rotation)
                temp = self.__player_interaction[int(temp.point.x) + self.__go_x][int(temp.point.y) + self.__go_y]
                self.__output.append(temp.point)
            elif not temp.right:
                self.rotation_add(1)
                temp.rotate_right(self.__temp_rotation)
                if not temp.top:
                    self.calculate_move(self.__temp_rotation)
                    temp = self.__player_interaction[int(temp.point.x) + self.__go_x][int(temp.point.y) + self.__go_y]
                    self.__output.append(temp.point)
            elif not temp.bottom:
                self.rotation_add(2)
                temp.rotate_right(self.__temp_rotation)
                if not temp.top:
                    self.calculate_move(self.__temp_rotation)
                    temp = self.__player_interaction[int(temp.point.x) + self.__go_x][int(temp.point.y) + self.__go_y]
                    self.__output.append(temp.point)
            k += 1

    def get_output(self):
        """
        :return output: lista punktow do rysowania sciezki
        """
        return self.__output

    def print_output(self):
        """
        :return: none
        """
        print("---------------------------------------")
        for elem in self.__output:
            print("x: " + str(elem.x) + " y: " + str(elem.y))

    def rotation_add(self, value):
        """
        :type value: int
        :param value: Definiuje o jaka wartosc ma sie przesunac bot
        :return none
        Dodanie rotacji o dana wartosc (jesli juz jest przesuniety to przesuwa dalej\n
        Jesli rotacja > 3 to zaczyna od nowa, czyli rotuje w 4 kierunkach
        """
        self.__temp_rotation += value
        if self.__temp_rotation > 3:
            self.__temp_rotation -= 4

    def calculate_move(self, rotation):
        """
        :type rotation: int
        :param rotation: obrot potrzebny do wyliczenia przemieszczenia
        :return: none
        Kalkulacja ruchu w danym kierunku biorac pod uwage obrot
        """
        if rotation == 3:
            self.__go_x = 0
            self.__go_y = -1
        if rotation == 2:
            self.__go_x = -1
            self.__go_y = 0
        if rotation == 1:
            self.__go_x = 0
            self.__go_y = 1
        if rotation == 0:
            self.__go_x = 1
            self.__go_y = 0

