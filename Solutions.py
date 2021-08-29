import numpy as np
import pandas as pd
import time
from random import randint
from math import sqrt
import matplotlib.pyplot as plt
### global section.

plt.close("all")
#test points 
points = [(0,0),(4,2),(6,3),(5,7),(3,100),(1,104),(7,90)]

#random points for complexity measurement
randomPoints  = [(randint(0, 1000),randint(0, 1000)) for i in range(1000)]

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
     # biggest integer value
     minimum = 2147483647
     ArrSize = len(pts)
     #print("length of points is " + str(len(pts)))
     for i in range(ArrSize):
         for j in range(i+1,ArrSize):
             #print("i point is " + str(pts[i]))
             #print("j point is " + str(pts[j]))
             if distance(pts[i],pts[j]) < minimum:
                minimum = distance(pts[i],pts[j])
     return minimum   

def timeBruteForceSmallestDistance():
    times = []
    for x in range(0,1000,10):
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

#TODO: recursivy this. Right now it works for breaking it in half once.
#TODO: plot the time. Might need a certain library.
def DnCShortestDistance(half,pts,n):
    Size = len(pts)
    minimum = 2147483647
    minimumLeft = 2147483647
    minimumRight = 2147483647
    minimumMiddle = 2147483647
    #initializing all the lists
    leftList = []
    rightList = []
    middleList = []
    
    if n <= 3:
        return bruteForceSmallestDistance(pts)
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
    pts.sort(key = lambda pts:pts[0])


    # need to find the middle x position
    mid = n // 2
    midPoint = half[mid]
    # #defining the lists to the points
    #sortedX = pts.sorted(pts, key = lambda x: x[0])
    # do I need to recursively keep breaking it down in half or just brute force the left and the right.
    leftList = pts[:Size//2]
    rightList = pts[Size//2:]
    minimumLeft = DnCShortestDistance(leftList,pts,mid)
    minimumRight = DnCShortestDistance(rightList,pts,n-mid)
    minimum = min(minimumLeft, minimumRight)
    # finding the starting position of the middle section to look at. 
    beginSpanX = midPoint[0] - minimum
    endingSpanX = midPoint[0] + minimum
    #need to sort by Y
    pts.sort(key = lambda pts:pts[1])
    #check if it is in the span of x and y 
    pts.reverse()
    # need to change name of X
    for strip in pts:
        #check if it is in the span
        if strip[0] <= endingSpanX and strip[0] >= beginSpanX:
            middleList.append(strip)
            #break free if we have our first 5 elements.
            if len(middleList) == 5:
                break


    minimumMiddle = bruteForceSmallestDistance(middleList)
    minimum = min(minimum,minimumMiddle)

    #print("The size of left and right respectfully are " + str(len(leftList)) +" " + str(len(rightList)))
    return minimum

def timeDnCShortestDistance():
    times = []
    for x in range(0,1000,10):
        start_time = time.time()
        list2 = DnCShortestDistance(randomPoints[0:x],randomPoints[0:x],x)
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





### problem 4




### problem 5








### running the code


#problem 1. 
print("The smallest distance by brute force is " + str(bruteForceSmallestDistance(points)))
complexityPoints = []
complexityPoints = timeBruteForceSmallestDistance()

'''
plt.plot(range(0,1000,10),complexityPoints)
plt.xlabel('size: N')
plt.ylabel('time(S)')
plt.title('Run Time for Brute Force Approach')
plt.show()
'''


# problem 2
print("The smallest distance by Divide and conquer is " + str(DnCShortestDistance(points,points,len(points))))


complexityPoints = []
complexityPoints = timeDnCShortestDistance()
plt.plot(range(0,1000,10),complexityPoints)
plt.xlabel('size: N')
plt.ylabel('time(S)')
plt.title('Run Time for Divide and Conquer approach')
plt.show()




