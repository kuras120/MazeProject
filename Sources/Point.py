

class Point:
    """
    :type x: int
    :param x: parametr x
    :type y: int
    :param y: parametr y
    :type right_wall: bool
    :param right_wall: czy prawa sciana (od punktu) istnieje
    :type bottom_wall: bool
    :param bottom_wall: czy dolna sciana (od punktu) istnieje
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.right_wall = False
        self.bottom_wall = False

