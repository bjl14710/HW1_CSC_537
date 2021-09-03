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

def crossSection(pt1,pt2,ptk):
    # comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
    return (pt2[0]-pt1[0])*(ptk[1]-pt1[1])-(pt2[1]-pt1[1])*(ptk[0]-pt1[0])

# def crossSection(pt1,ptk,pt2):
#     # comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
#     comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
#     return comp

def _det(a,b,c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

#loop through all pairs and find what is connected
def orderPairs(a):
    Size = len(a)
    # orderedPairs = [[],[]]
    orderedPairs = []
    orderedPairs.append(a[0])
    orderedPairs.append(a[1])
    holder = a[1]
    #first line segment is a[0],a[1]
    for i in range(2,Size-1):
        if a[i] == holder:
            orderedPairs.append(a[i+1])  
            holder = a[i+1]
            i=i+2
    return orderedPairs

# def removeDuplicates(a):
#     Size = len(a)
#     newPts = a
#     for i in range(len(newPts)):
#         for j in range(len(newPts)):
#             if a[i] == a[j]:
#                 newPts.pop(j)
#     return newPts

def BruteForceConvexHull(pts):
    #sorting by x to get farthest left point.
    # pts.sort(key = lambda pts:pts[0])
    convexHull = []
    # convexHull.append(min(pts))
    Size = len(pts)
    pts.sort(key = lambda pts:pts[0])
    holdList = []
    #loop through all segments and make a line between the two.
    # use the y=mx+b
    # m = None
    # convexHull.append(pts[0])
    cnt = 0
    valid = False
    for i in range(Size):
        for j in range(Size):
            if not (i == j):
                valid = True
                for p in pts:
                    if not (p == pts[j]) and not (p==pts[i]):
                        if _det(pts[i],pts[j],p) < 0:
                            valid = False
                if valid:
                    convexHull.append(pts[i])
                    convexHull.append(pts[j])
                    # holdList.append(convexHull[cnt])
                    cnt = cnt + 1
    
    # convexHull = orderPairs(convexHull)
    # convexHull = orderPairs(convexHull)
    # convexHull = list(set(convexHull))
    
    # for i in range(Size-1):
    #     for j in range(Size):
    #         ptCnt = 0
    #         for p in pts:
    #             if not p == pts[i] and not p == pts[j]:
    #                 if _det(pts[i],pts[j],p) < 0:
    #                     ptCnt = ptCnt + 1
    #                 if ptCnt == Size-2:
    #                     convexHull.append(pts[i])
    #                     convexHull.append(pts[j])

    
    
    
    
    # for i in range(Size):
    #     for j in range(Size):
    #         # if j == i and i >= len(pts) - 1:
    #         #     j = 0
    #         # elif j == i and i < len(pts):
    #         #     j = i + 1
    #         # if j >= len(pts):
    #         #     j = 0
    #         #find slope
    #         # m = slope(pts[i],pts[j])
    #         # #use slope to find line intersect
    #         # YIntersect = findYIntersect(pts[i], m)
    #         # #for every point that is not i or j
    #         # k = j + 1
    #         # if k >= len(pts):
    #         #     k = 0
    #         # bigger = tangentLineCompare(pts[i], pts[j], pts[k])
    #         #check that every point is checked even if we passed
    #         #it already.
    #         valid = None
    #         if i == j:
    #             valid = False
    #         lef = 0
    #         rit = 0
            
    #         for p in pts:
    #             if p != pts[j] and p != pts[i]:
    #                 if crossSection(pts[i], pts[j], p) == 0:
    #                     lef = lef + 1
    #                     rit = rit + 1
    #                 elif crossSection(pts[i], pts[j], p) < 0:
    #                     lef = lef + 1
    #                     valid = False
    #                 elif crossSection(pts[i], pts[j], p) > 0:
    #                     rit = rit + 1
    #                     valid = True
    #             if (rit >= Size-2) and valid and pts[j] not in convexHull:
    #                 convexHull.append(pts[i])
    #                 convexHull.append(pts[j])
    #         #convexHull.sort(key = lambda convexHull:convexHull[1])
            # 
    return convexHull




def printPoints(pts):
    xPts = []
    yPts = []
    xMinPts = []
    yMinPts = []
    for i in range(len(pts)):
        xPts.append(pts[i][0])
        yPts.append(pts[i][1])
    plt.scatter(xPts,yPts, marker='o')

print("the points for the convex hull through brute force is " + str(BruteForceConvexHull(randomPoints)))
convexHullPoints = BruteForceConvexHull(randomPoints)
# print("the points for the convex hull through brute force is " + str(orderPairs(convexHullPoints)))

complexityPoints = []
complexityPoints = BruteForceConvexHull(randomPoints)
xPts = []
yPts = []
for i in range(len(BruteForceConvexHull(randomPoints))):
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

