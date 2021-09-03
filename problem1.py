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
randomPoints  = [(randint(0, 100),randint(0, 100)) for i in range(500)]

#this algorithm runs the distance formula on two points.
def distance(a,b):
    diffX = a[0]-b[0]
    diffY = a[1]-b[1]
    dist = sqrt(diffX*diffX + diffY*diffY)
    return dist

'''
This problem involves using a Brute-Force approach to finding 
the closest distance between two points in a graph.:
'''
def bruteForceSmallestDistance(pts):
     minimum = float('inf')
     point1 = [0,0]
     point2 = [0,0]
     ArrSize = len(pts)
     for i in range(ArrSize):
         for j in range(i+1,ArrSize):
             if distance(pts[i],pts[j]) < minimum:
                minimum = distance(pts[i],pts[j])
                point1 = pts[i]
                point2 = pts[j]
     return point1, point2

def timeBruteForceSmallestDistance():
    times = []
    for x in range(0,300,10):
        start_time = time.time()
        list2 = bruteForceSmallestDistance(randomPoints[0:x])
        elapsed_time = time.time()-start_time
        times.append(elapsed_time)
    
    return times




def printPoints(pts):
    xPts = []
    yPts = []
    xMinPts = []
    yMinPts = []
    for i in range(len(points)):
        xPts.append(points[i][0])
        yPts.append(points[i][1])
    plt.scatter(xPts,yPts, marker='o')


PointsOfShortestDistance = bruteForceSmallestDistance(points)
print("The points of the smallest distance by brute force is " + str(bruteForceSmallestDistance(points)))
print("The smallest distance by brute force is " + str(distance(PointsOfShortestDistance[0],PointsOfShortestDistance[1])))
complexityPoints = []
complexityPoints = timeBruteForceSmallestDistance()
printPoints(points)
xPts = []
yPts = []
xPts = bruteForceSmallestDistance(points)[0]
yPts = bruteForceSmallestDistance(points)[1]
plt.plot(xPts,yPts)
plt.show()

#graphing the time it takes to run the code.
plt.plot(range(0,300,10),complexityPoints)
plt.xlabel('size: N')
plt.ylabel('time(S)')
plt.title('Run Time for Brute Force Approach')
plt.show()



printPoints(points)
xPts = []
yPts = []
xPts = DivideAndConquerDistanceAlgorithm(points)[0]
yPts = DivideAndConquerDistanceAlgorithm(points)[1]
plt.plot(xPts,yPts)

