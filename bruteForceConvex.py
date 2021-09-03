import numpy as np
import pandas as pd
import time
from random import randint
from math import sqrt
import matplotlib.pyplot as plt
from typing import List, Union, Iterable

### global section.

#start with the points


#test points 
points = [(0,0),(4,2),(6,3),(5,7),(3,100),(1,104),(7,90),(31,22),(123,33),(-5,20)]

#random points for complexity measurement
randomPoints  = [(randint(0, 100),randint(0, 100)) for i in range(100)]

class point:
    def __init__(self,x,y):
        self.x, self.y = float(x), float(y)

# def _construct_points(pts):
#     for p in pts:
def _construct_points(pts: Union[List[point], List[List[float]], Iterable[List[float]]]
) -> List[point]:
    val: List[point] = []
    if pts:
        for p in pts:
            val.append(p)
    return val

def _validate(pts):
    points = []
    if not hasattr(pts, "__iter__"):
        raise ValueError(
            f"expected an iterable but got a non iterable type {pts}"
        )
    if not points:
        raise ValueError(f"Expected a list of points but got {pts}")

    
    points.append(Point(p[0], p[1]))
    
    return points


def _det(a,b,c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def convexHullBruteForce(pts):
    pts.sort(key = lambda pts:pts[0])
    points = pts#_construct_points(pts)
    Size = len(points)
    convex_set = set()
    convex_set = []
    
    for i in range(Size - 1):
        for j in range(i+1, Size):
            point_on_left = point_on_right = False
            partOfHull = True
            for k in range(Size):
                if k!=i and k!=j:
                    det = _det(pts[i],pts[j],pts[k])

                    if det > 0:
                        point_on_left = True
                    elif det < 0:
                        point_on_right = True
            
                if point_on_right and point_on_left:
                    partOfHull = False
                    break
            if partOfHull:
                convex_set.append(pts[i])
                convex_set.append(pts[j])
    
    return sorted(convex_set)


def printPoints(pts):
    xPts = []
    yPts = []
    xMinPts = []
    yMinPts = []
    for i in range(len(pts)):
        xPts.append(pts[i][0])
        yPts.append(pts[i][1])
    plt.scatter(xPts,yPts, marker='o')



def main():
    results_bf = convexHullBruteForce(points)
    print("the points for the convex hull through brute force is " + str(convexHullBruteForce(randomPoints)))
    convexHullPoints = convexHullBruteForce(points)
    # print("the points for the convex hull through brute force is " + str(orderPairs(convexHullPoints)))

    complexityPoints = []
    complexityPoints = convexHullBruteForce(points)
    xPts = []
    yPts = []
    for val in complexityPoints:
        print(val)
    
    for i in range(len(convexHullBruteForce(points))):
        xPts.append(complexityPoints[i][0])
        yPts.append(complexityPoints[i][1])
    #complexityPoints = [0,0]
    #complexityPoints[1] = timeDnCShortestDistance()
    printPoints(points)
    # xPts.append(xPts[0])
    # yPts.append(yPts[0])
    plt.plot(xPts,yPts)
    #plt.plot(range(2),complexityPoints)

    plt.xlabel('x points')
    plt.ylabel('y points')
    plt.title('convex hull brute force')
    plt.show()


if __name__ == "__main__":
    main()


