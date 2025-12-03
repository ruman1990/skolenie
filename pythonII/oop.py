class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

#    def __eq__(self, other):
#        return (self.x) == (other.x)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        return abs(self.x) + abs(self.y)
    
bod = Point(1,1)
bod2 = Point(1,2)

print(bod == bod2)