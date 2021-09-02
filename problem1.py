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

#this algorithm runs the distance formula on two points.
def distance(a,b):
    diffX = a[0]-b[0]
    diffY = a[1]-b[1]
    #print("diff x is " + str(diffX * diffX))
    #print("diff y is " + str(diffY * diffY))
    dist = sqrt(diffX*diffX + diffY*diffY)
    return dist

# minimum distance should be (4,2) to (6,3) or 
# sqrt (5) or about 2.23606

###problem 1

'''
This problem involves using a Brute-Force approach to finding 
the closest distance between two points in a graph.:
'''
def bruteForceSmallestDistance(pts):
     #take one point then compare to all other points
     # then take the next point and compare to 
     # the following points
     # biggest integer value]
     minimum = 2147483647
     point1 = [0,0]
     point2 = [0,0]
     ArrSize = len(pts)
     #print("length of points is " + str(len(pts)))
     for i in range(ArrSize):
         for j in range(i+1,ArrSize):
             #print("i point is " + str(pts[i]))
             #print("j point is " + str(pts[j]))
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





def shortestDistStrip(pts,dist):
    Size = len(pts)
    minimum = 2147483647
    List = []
    point1 = []
    point2 = []
    #look through set, check to see that the y values are of a certain distance less than dist.
    for i in range(Size):
        j = i + 1
        while j < Size - 1 and (pts[i][1]-pts[j][1] < dist):
            List.append(distance(pts[j],pts[i]))
            j = j + 1
            if List[len(List)-1] < minimum:
                minimum = List[len(List)-1]
                point1 = pts[i]
                point2 = pts[j]
    if len(List) > 0:
        minimum = min(List)
    if len(List) < 2:
        return [minimum,minimum],[0,0]
    return point1, point2

def DnCShortestDistance(half,ySortedPts,n):
    Size = len(half)
    minimum = 2147483647
    minimumStripCompare = 2147483647
    
    minimumLeft1 = [0,0]
    minimumLeft2 = [0,0]

    minimumRight1 = [0,0]
    minimumRight2 = [0,0]

    minimumStrip1 = [0,0]
    minimumStrip2 = [0,0]
    
    #initializing all the lists
    leftList = []
    rightList = []
    stripList = []

    pointA = [0,0]
    pointB = [0,0]
    pointC = [0,0]
    pointD = [0,0]
    

    if n <= 3:
        return bruteForceSmallestDistance(half)
    

    # need to sort by X first

    # need to find the middle x position
    mid = n // 2
    midPoint = half[mid]
    # #defining the lists to the points
    #sortedX = pts.sorted(pts, key = lambda x: x[0])
    # do I need to recursively keep breaking it down in half or just brute force the left and the right.
    leftList = half[:mid]
    rightList = half[mid:]
    minimumLeft = DnCShortestDistance(leftList,ySortedPts,mid)
    minimumRight = DnCShortestDistance(rightList,ySortedPts,n-mid)
    minimumCompareLeft = distance(minimumLeft[0],minimumLeft[1])
    minimumCompareRight = distance(minimumRight[0],minimumRight[1])
    minimum = min(minimumCompareLeft, minimumCompareRight)
    if minimum == minimumCompareLeft:
        pointC = minimumLeft[0]
        pointD = minimumLeft[1]
    elif minimum == minimumCompareRight:
        pointC = minimumRight[0]
        pointD = minimumRight[1]

    # finding the starting position of the middle section to look at. 
    beginSpanX = midPoint[0] - minimum
    endingSpanX = midPoint[0] + minimum
    #Use y sorted points
    #check if it is in the span of x and y 
    ySortedPts.reverse()
    # need to find the points in the strip.
    for strip in ySortedPts:
        #check if it is in the span
        if strip[0] <= endingSpanX and strip[0] >= beginSpanX:
            stripList.append(strip)
            #break free if we have our first 5 elements.
            
    minimumStrip = shortestDistStrip(stripList,minimum)
    if len(minimumStrip) >= 2:
        minimumStripCompare = distance(minimumStrip[0],minimumStrip[1])    
    
    if minimum < minimumStripCompare:
        pointA = pointC
        pointB = pointD
    elif minimumStripCompare <= minimum:
        pointA = minimumStrip[0]
        pointB = minimumStrip[1]
    #print("The size of left and right respectfully are " + str(len(leftList)) +" " + str(len(rightList)))
    return pointA, pointB

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






def printPoints(pts):
    xPts = []
    yPts = []
    xMinPts = []
    yMinPts = []
    for i in range(len(points)):
        xPts.append(points[i][0])
        yPts.append(points[i][1])
    plt.scatter(xPts,yPts, marker='o')



print("The smallest distance by brute force is " + str(bruteForceSmallestDistance(points)))
complexityPoints = []
complexityPoints = timeBruteForceSmallestDistance()
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
# xPts = []
# yPts = []
# xMinPts = []
# yMinPts = []
# for i in range(len(points)):
#     xPts.append(points[i][0])
#     yPts.append(points[i][1])
# plt.scatter(xPts,yPts, marker='o')
printPoints(points)
xPts = []
yPts = []
xPts = bruteForceSmallestDistance(points)[0]
yPts = bruteForceSmallestDistance(points)[1]
plt.plot(xPts,yPts)
plt.show()

#graphing the time it takes to run the code.
plt.plot(range(0,300,10),complexityPoints)
#plt.plot(range(2),complexityPoints)
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

