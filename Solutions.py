import numpy as np
from math import sqrt
### global section.

points = [(0,0),(4,2),(6,3),(5,7)]

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
     #print("length of points is " + str(len(pts)))
     for i in range(len(pts)):
         for j in range(i+1,len(pts)):
             #print("i point is " + str(pts[i]))
             #print("j point is " + str(pts[j]))
             if distance(pts[i],pts[j]) < minimum:
                minimum = distance(pts[i],pts[j])
     return minimum   



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



