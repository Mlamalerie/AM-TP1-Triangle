

"""
class Point:

    def __init__(self,x : float,y : float):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%.1f, %.1f)" % (self.x,self.y)
"""
class Triangle:
    def __init__(self, a : float,b : float,c : float):
        self.a = a
        self.b = b
        self.c = c

    def get_segments(self):
        return [self.a,self.b,self.c]

    def __str__(self):
        return "Triangle(" + ', '.join([str(p) for p in self.get_points()]) + ")"