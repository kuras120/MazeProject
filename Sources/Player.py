from copy import deepcopy


class Player:
    """
    :type left: bool
    :param left: lewa strona bota
    :type right: bool
    :param right: prawa strona bota
    :type top: bool
    :param top: gorna strona bota
    :type bottom: bool
    :param bottom: dolna strona bota
    :type point: tuple
    :param point: punkt odniesienia na mapie
    :type rotation: int
    :param rotation: punkt rotacja bota na danej pozycji
    :return: none
    """
    def __init__(self):
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False
        self.point = []
        self.rotation = 0


    def rotate_right(self, rotation):
        """
        :return none
        Obracanie bota (do ruchow w bok i powrotow)\n
        0: skierowany w prawo; 1: skierowany w dol; 2: skierowany w lewo; 3: skierowany w gore
        """
        while self.rotation != rotation:
            self.rotate()

    def revert_rotation(self):
        """
        :return none
        Powrot do stanu przed rotacja (nieuzywane)
        """
        while self.rotation != 0:
            self.rotate()

    def rotate_point(self):
        """
        :return: none
        Rotacja punktu odniesienia (nie trzeba tego robic, wystarczy ze rotuje sciany w postaci booli)
        """
        if self.rotation == 1:
            self.point.x = int(self.point.x) + 1
        elif self.rotation == 2:
            self.point.y = int(self.point.y) + 1
        elif self.rotation == 3:
            self.point.y = int(self.point.y) + 1
        elif self.rotation == 0:
            self.point.x = int(self.point.x) - 1
            self.point.y = int(self.point.y) - 1

    def rotate(self):
        """
        :return: none
        Rotacja booli - czy mozliwe jest przejscie w danym kierunku)
        Wymagane aby przy obrocie bota nie tracil orientacji w terenie
        """
        temp = self.left
        self.left = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = temp

        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0

        '''
        Nie uzywac
        '''
        #self.rotate_point()
