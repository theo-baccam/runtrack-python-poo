class Point:
    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input

    def afficherLesPoints(self):
        coordinate = [self.x, self.y]
        return coordinate

    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    def changerX(self, increment):
        self.x += increment

    def changerY(self, increment):
        self.y += increment
