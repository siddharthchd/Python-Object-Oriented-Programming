import math

class Line:

    def __init__(self, coor1, coor2):

        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

    def slope(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())

