import numpy as np
import pandas as pd
import time
from random import randint
from math import sqrt
import matplotlib.pyplot as plt
import problem1
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

def shortestDistStrip(pts,dist):
    Size = len(pts)
    minimum = 2147483647
    List = []
    #look through set, check to see that the y values are of a certain distance less than dist.
    for i in range(Size):
        j = i + 1
        while j < Size and (pts[i][1]-pts[j][1] < dist):
            List.append(distance(pts[j],pts[i]))
            j = j + 1
    if len(List) > 0:
        minimum = min(List)
    return minimum

def DnCShortestDistance(half,ySortedPts,n):
    Size = len(half)
    minimum = 2147483647
    minimumLeft = 2147483647
    minimumRight = 2147483647
    minimumStrip = 2147483647
    #initializing all the lists
    leftList = []
    rightList = []
    stripList = []
    

    if n <= 3:
        return bruteForceSmallestDistance(half)
    '''
    if Size >= 5:
        #size of intersection is 5. for 5 points.
        print("size of intersection is 5")
        middleList = [(0,0)] * 5
    else:
        print("size of intersection is " + str(Size))
        middleList = [(0,0)] * Size
        #size of intersection is amount of points there are.
    '''

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
    minimum = min(minimumLeft, minimumRight)
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

