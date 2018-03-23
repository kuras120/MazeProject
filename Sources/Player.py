

class Player:
    def __init__(self):
        self.left = False
        self.right = False
        self.top = False
        self.buttom = False
        self.point = []
        self.rotation = 0

    def rotate_left(self):
        temp = self.left
        self.left = self.buttom
        self.buttom = self.right
        self.right = self.top
        self.top = temp

        self.rotation -= 1
        if self.rotation < 0:
            self.rotation = 3

        self.rotate_point()

    def rotate_right(self):
        temp = self.left
        self.left = self.top
        self.top = self.right
        self.right = self.buttom
        self.buttom = temp

        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0

        self.rotate_point()

    def rotate_point(self):
        if self.rotation == 1:
            self.point.x = int(self.point.x) + 1
        elif self.rotation == 2:
            self.point.y = int(self.point.y) + 1
        elif self.rotation == 3:
            self.point.x = int(self.point.x) - 1
        elif self.rotation == 0:
            self.point.x = int(self.point.x) - 1
            self.point.y = int(self.point.y) - 1
