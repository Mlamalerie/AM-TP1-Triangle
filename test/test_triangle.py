import pytest
from Triangle import Point, Triangle
from itertools import combinations, permutations
import numpy as np

def point_is_valid(p : Point):
    for e in p:
        if not e:
            return False
        elif not isinstance(e,float) or isinstance(e,int):
            return False
    return True



"""
@pytest.fixture
def example1_triangle():
    p1 = Point(-3, 4)
    p2 = Point(1, 7)
    p3 = Point(-6, -5)
    return Triangle(p1,p2,p3)

@pytest.fixture
def success_triangle_examples(example1_triangle):
    generated_tri = []
    for _ in range(10):
        generated_tri.append(Triangle(*[Point(x="0", y=np.random.uniform(-20,20)) for _ in range(3)]))
    return [example1_triangle] + generated_tri
"""

def test_is_coherent():
    with pytest.raises(ZeroDivisionError):
        p1 = None
        p2 = Point(1, 7)
        p3 = Point(-6, -5)
        Triangle(p1, p2, p3)


    #assert (isinstance(tri.p1, int), f"number greater than 0 expected, got: {}")










    