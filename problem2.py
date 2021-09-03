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
def distance(p1,p2):
    diffX = p1[0]-p2[0]
    diffY = p1[1]-p2[1]
    dist = sqrt(diffX*diffX + diffY*diffY)
    return dist

def shortestDistStrip(pts,dist):
    Size = len(pts)
    minimum = float('inf')
    global MinimumPoint1, MinimumPoint2, MinimumPoint3, MinimumPoint4
    List = []
    point1 = None
    point2 = None
    #look through set, check to see that the y values are of a certain distance less than dist.
    for i in range(Size):
        j = i + 1
        while j < Size and (pts[i][1]-pts[j][1] < dist):
            List.append(distance(pts[j],pts[i]))
            j = j + 1
            point1 = pts[i]
            if j < Size:
                point2 = pts[j]
    if len(List) > 0:
        minimum = min(List)
    if minimum < dist:
        MinimumPoint1 = point1
        MinimumPoint2 = point2
    return minimum

#from problem 1
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

def minimumBruteForceDist(pts):
    return distance(bruteForceSmallestDistance(pts)[0],bruteForceSmallestDistance(pts)[1])

def DnCShortestDistance(half,ySortedPts,n):
    Size = len(half)
    minimum = float('inf')
    minimumLeft = float('inf')
    minimumRight = float('inf')
    minimumStrip = float('inf')
    #initializing all the lists
    leftList = []
    rightList = []
    stripList = []
    

    if n <= 3:
        return minimumBruteForceDist(half)
    # need to sort by X first

    # need to find the middle x position
    mid = n // 2
    midPoint = half[mid]
    leftList = half[:mid]
    rightList = half[mid:]
    minimumLeft = DnCShortestDistance(leftList,ySortedPts,mid)
    minimumRight = DnCShortestDistance(rightList,ySortedPts,n-mid)
    minimum = min(minimumLeft, minimumRight)
    # finding the starting position of the middle section to look at. 
    
    beginSpanX = midPoint[0] - minimum
    endingSpanX = midPoint[0] + minimum
    #Use points sorted by y
    #check if it is in the span of x and y 
    ySortedPts.reverse()
    # need to find the points in the span.
    for strip in ySortedPts:
        if strip[0] <= endingSpanX and strip[0] >= beginSpanX:
            stripList.append(strip)
            #break free if we have our first 5 elements.
            
    minimumStrip = shortestDistStrip(stripList,minimum)
    minimum = min(minimum,minimumStrip)

    #print("The size of left and right respectfully are " + str(len(leftList)) +" " + str(len(rightList)))
    return minimum

def DivideAndConquerDistanceAlgorithm(pts):
    # this code is for sorting before passing to recursion
    pts.sort(key = lambda pts:pts[0])
    xPts = pts[:]
    pts.sort(key = lambda pts:pts[1])
    yPts = pts[:]
    minDist = DnCShortestDistance(xPts,yPts,len(xPts))
    return minDist


def timeDnCShortestDistance():
    times = []
    
    for x in range(0,300,10):
        start_time = time.time()
        list2 = DivideAndConquerDistanceAlgorithm(randomPoints[0:x])
        elapsed_time = time.time()-start_time
        times.append(elapsed_time)
    return times


print("The smallest distance by Divide and conquer is " + str(DivideAndConquerDistanceAlgorithm(points)))

complexityPoints = []
complexityPoints = timeDnCShortestDistance()
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
plt.plot(range(0,300,10),complexityPoints)
#plt.plot(range(2),complexityPoints)
plt.xlabel('size: N')
plt.ylabel('time(S)')
plt.title('Run Time for Divide and Conquer approach')
plt.show()

