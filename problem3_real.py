import numpy as np
import pandas as pd
import time
from random import randint
from math import sqrt
import matplotlib.pyplot as plt

### global section.

#test points 
points = [(0,0),(4,2),(6,3),(5,7),(3,100),(1,104),(7,90),(31,22),(123,33),(-5,20)]

#random points for complexity measurement
randomPoints  = [(randint(0, 100),randint(0, 100)) for i in range(100)]

def SideOfLine(a,b,c):
    return (c[0]-a[0]) * (b[1]-a[1]) - (c[1]-a[1]) * (b[0]-a[0])

def convexHull(pts):
    answer = []
    OnRight = True
    for i in range(len(pts)):
        for j in range(len(pts)):
            if not (i == j):
                pt_I = pts[i]
                pt_J = pts[j]

                OnRight = True
                for k in range(len(pts)):
                    if not(k==i) and not(k==j):
                        d = SideOfLine(pt_I,pt_J,pts[k])
                        if d < 0:
                            OnRight = False
                            break
                if(OnRight):
                    answer.append(pt_I)
                    answer.append(pt_J)
    return answer
                        











def printPoints(pts):
    xPts = []
    yPts = []
    xMinPts = []
    yMinPts = []
    for i in range(len(pts)):
        xPts.append(pts[i][0])
        yPts.append(pts[i][1])
    plt.scatter(xPts,yPts, marker='o')

print("the points for the convex hull through brute force is " + str(convexHull(randomPoints)))
convexHullPoints = convexHull(randomPoints)
# print("the points for the convex hull through brute force is " + str(orderPairs(convexHullPoints)))

complexityPoints = []
complexityPoints = convexHull(randomPoints)
xPts = []
yPts = []
for i in range(len(convexHull(randomPoints))):
    xPts.append(complexityPoints[i][0])
    yPts.append(complexityPoints[i][1])
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
printPoints(randomPoints)
xPts.append(xPts[0])
yPts.append(yPts[0])
plt.plot(xPts,yPts)
#plt.plot(range(2),complexityPoints)

plt.xlabel('x points')
plt.ylabel('y points')
plt.title('convex hull brute force')
plt.show()

