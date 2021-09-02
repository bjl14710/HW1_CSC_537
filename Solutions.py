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
pointsOfMinimumBF = [(0,0),(0,0)]
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

'''
Idea of this approach is to look at all distances that we can find 
in a graph between two points and simply select the minimum.
'''



### problem 2

'''
This problem requires that we find the smallest distance between two points
but instead of Brute-Force, we are going to use a Divide and Conquer 
algorithm.
'''

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

#split the set in half.


'''
For this answer, we should break up the set of points into 
the left and the right side, and the cross section side. 
The cross-section side simply uses the fact that we only need
to use the top 5 points AFTER sorting the points by Y
and these are the 5 points in the cross section. This cross
Section is defined by the minimum point after looking at the 
left and right sections. Then using that as a distance D 
between the middle section. So only need to compare the 
5 points there to find the minimum of the cross section. 
After that, then we can compare that minimum to the minimum we 
already found. That min being d. 
'''
### problem 3

'''
for this problem. Shouls look at Convex hull by looking at farthest left 
point, then going through Every single point. A segment is used to represent
the Convex Hull if and only if all other points are on the same side of 
that segment.
'''

# def slope(a,b):
#     if b[0] - a[0] != 0:
#         m = (b[1]-a[1])/(b[0]-a[0])
#     return m

# #y=mx+b so b = y-mx
# def findYIntersect(a,m):
#     YIntersect = a[1]-m*a[0]
#     return YIntersect

# def tangentLineCompare(a,b,compare):
#     m = slope(a,b)
#     const = findYIntersect(a, m)
#     bigger = 3
#     if compare[0]*m + const < compare[1]:
#         bigger = 0
#     elif compare[0]*m + const > compare[1]:
#         bigger = 1
#     elif compare[0]*m + const == compare[1]:
#         bigger = 2
#     return bigger

#pt1 is 0 pt2 is b and ptk is a
def crossSection(pt1,ptk,pt2):
    # comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
    comp = (ptk[0]-pt1[0])*(pt2[1]-pt1[1])-(ptk[1]-pt1[1])*(pt2[0]-pt1[0])
    return comp


def BruteForceConvexHull(pts):
    #sorting by x to get farthest left point.
    # pts.sort(key = lambda pts:pts[0])
    convexHull = []
    # convexHull.append(min(pts))
    Size = len(pts)
    #loop through all segments and make a line between the two.
    # use the y=mx+b
    # m = None
    for i in range(Size):
        for j in range(Size):
            # if j == i and i >= len(pts) - 1:
            #     j = 0
            # elif j == i and i < len(pts):
            #     j = i + 1
            # if j >= len(pts):
            #     j = 0
            #find slope
            # m = slope(pts[i],pts[j])
            # #use slope to find line intersect
            # YIntersect = findYIntersect(pts[i], m)
            # #for every point that is not i or j
            # k = j + 1
            # if k >= len(pts):
            #     k = 0
            # bigger = tangentLineCompare(pts[i], pts[j], pts[k])
            #check that every point is checked even if we passed
            #it already.
            valid = None
            if i == j:
                valid = False
            lef = 0
            rit = 0
            
            for p in pts:
                if p != pts[j] and p != pts[i]:
                    if crossSection(pts[i], pts[j], p) == 0:
                        lef = lef + 1
                        rit = rit + 1
                    elif crossSection(pts[i], pts[j], p) < 0:
                        lef = lef + 1
                        valid = False
                    elif crossSection(pts[i], pts[j], p) > 0:
                        rit = rit + 1
                        valid = True
                if (rit >= Size-2) and valid and pts[j] not in convexHull:
                    convexHull.append(pts[i])
                    convexHull.append(pts[j])
            #convexHull.sort(key = lambda convexHull:convexHull[1])
            # 
    return convexHull


### problem 4
'''
need to use the divide and conquer approach to the Andrews algorithm.
'''

def andrewsScan(pts):
    #sort by x 
    Size = len(pts)
    if Size < 2:
        return pts[0]
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
    for p in pts:
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


#TODO: remove this part of the code
def convex_hull(points):

    """Computes the convex hull of a set of 2D points.

 

    Input: an iterable sequence of (x, y) pairs representing the points.

    Output: a list of vertices of the convex hull in counter-clockwise order,

      starting from the vertex with the lexicographically smallest coordinates.

    Implements Andrew's monotone chain algorithm. O(n log n) complexity.

    """

 

    # Sort the points lexicographically (tuples are compared lexicographically).

    # Remove duplicates to detect the case we have just one unique point.

    points = sorted(set(points))

 

    # Boring case: no points or a single point, possibly repeated multiple times.

    if len(points) <= 1:

        return points

 

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.

    # Returns a positive value, if OAB makes a counter-clockwise turn,

    # negative for clockwise turn, and zero if the points are collinear.

    def cross(o, a, b):

        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

 

    # Build lower hull

    lower = []

    for p in points:

        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:

            lower.pop()

        lower.append(p)

 

    # Build upper hull

    upper = []

    for p in reversed(points):

        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:

            upper.pop()

        upper.append(p)

 

    # Concatenation of the lower and upper hulls gives the convex hull.

    # Last point of each list is omitted because it is repeated at the beginning of the other list.

    return lower[:-1] + upper[:-1]

 

# Example: convex hull of a 10-by-10 grid.

### problem 5

def DnC_ComplexHull(pts):
    complexHull = []
    midPoint = len(pts) // 2
    return complexHull







### running the code


#problem 1. 
print("The smallest distance by brute force is " + str(bruteForceSmallestDistance(points)))
complexityPoints = []
complexityPoints = timeBruteForceSmallestDistance()
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
xPts = []
yPts = []
xMinPts = []
yMinPts = []
for i in range(len(points)):
    xPts.append(points[i][0])
    yPts.append(points[i][1])
plt.scatter(xPts,yPts, marker='o')
xPts = []
yPts = []
xPts = bruteForceSmallestDistance(points)[0]
yPts = bruteForceSmallestDistance(points)[1]
plt.plot(xPts,yPts)


plt.plot(range(0,300,10),complexityPoints)
#plt.plot(range(2),complexityPoints)
plt.xlabel('size: N')
plt.ylabel('time(S)')
plt.title('Run Time for Brute Force Approach')
plt.show()



# problem 2

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



# do I need to graph the closest dots???


# definetly have to graph the complex hull



# graphing the points 
xPts = []
yPts = []
# for i in range(len(points)):
#     xPts.append(points[i][0])
#     yPts.append(points[i][1])
for i in range(len(randomPoints)):
    xPts.append(randomPoints[i][0])
    yPts.append(randomPoints[i][1])

plt.scatter(xPts,yPts, marker='o')
'''
df = pd.DataFrame(points,
                    columns= ['x', 'y'])

ax1 = df.plot.scatter(x='x', y='y')
'''


#graphing problem 3


print("the points for the convex hull through brute force is " + str(BruteForceConvexHull(randomPoints)))


complexityPoints = []
complexityPoints = BruteForceConvexHull(randomPoints)
xPts = []
yPts = []
for i in range(len(BruteForceConvexHull(randomPoints))):
    xPts.append(complexityPoints[i][0])
    yPts.append(complexityPoints[i][1])
#complexityPoints = [0,0]
#complexityPoints[1] = timeDnCShortestDistance()
xPts.append(xPts[0])
yPts.append(yPts[0])
plt.plot(xPts,yPts)
#plt.plot(range(2),complexityPoints)

plt.xlabel('x points')
plt.ylabel('y points')
plt.title('convex hull brute force')
plt.show()




#problem 4


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
xPts.append(xPts[0])
yPts.append(yPts[0])
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


