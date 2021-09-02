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

# return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def crossSection(pt1,pt2,ptk):
    # comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
    return (pt2[0]-pt1[0])*(ptk[1]-pt1[1])-(pt2[1]-pt1[1])*(ptk[0]-pt1[0])

def andrewsScan(pts):
    #sort by x 
    Size = len(pts)
    if Size <= 1:
        return pts
    pts.sort(key = lambda pts:pts[0])
    convexHull = []
    pListUH = []
    pListLH = []
    #build lower hall
    for p in pts:
        while len(pListLH) >= 2 and crossSection(pListLH[-2], pListLH[-1], p) <= 0:
            pListLH.pop()
        pListLH.append(p)
    #build upper hall
    for p in reversed(pts):
        while len(pListUH) >= 2 and crossSection(pListUH[-2], pListUH[-1], p) <= 0:
            pListUH.pop()
        pListUH.append(p)

    #build uH
    #find the upper hull
    # for i in range(2,Size-1):
    #     pListUH.append(pts[i])
    #     while len(pListUH) >= 2 and crossSection(pts[i], pts[i-1], pts[i-2]) > 0:
    #         pListUH.pop()
    
    # pListLH = [pts[Size-1],pts[Size-2]]
    # for i in range(Size-3,0,-1):
    #     pListLH.append(pts[i])
    #     while len(pListLH) >= 2 and crossSection(pts[i],pts[i-1], pts[i-2]) < 0:
    #         pListLH.pop()
    for i in range(0,len(pListUH)):
        convexHull.append(pListUH[i])
    for j in range(len(pListLH)):
        convexHull.append(pListLH[j])    
    return convexHull

#print the problem



print("the points for the convex hull through Andrews Scan is " + str(andrewsScan(points)))


complexityPoints = []
complexityPoints = andrewsScan(points)
xPts = []
yPts = []
for i in range(len(andrewsScan(points))):
    xPts.append(complexityPoints[i][0])
    yPts.append(complexityPoints[i][1])
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
plt.plot(xPts,yPts)


xPts = []
yPts = []
xMinPts = []
yMinPts = []
for i in range(len(points)):
    xPts.append(points[i][0])
    yPts.append(points[i][1])
plt.scatter(xPts,yPts, marker='o')
plt.plot(xMinPts,yMinPts)

#plt.plot(range(2),complexityPoints)

plt.xlabel('x points')
plt.ylabel('y points')
plt.title('convex hull andrews scan')
plt.show()




