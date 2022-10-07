# A Python program to print all
# combinations of a given length
from itertools import permutations, combinations
from Triangle import Point, Triangle


p1 = Point(-3,4)
p2 = Point(1,7)
p3 = Point(-6,-5)
for c in permutations([1, 2, 3,None,None,None], 3):
    print(Triangle(**c))
