"""
1. Define a Python function remdup(l) that takes a nonempty list of integers l 
and removes all duplicates in l, keeping only the first occurrence of each 
number. For instance:

>>> remdup([3,1,3,5])
[3, 1, 5]

>>> remdup([7,3,-1,-5])
[7, 3, -1, -5]

>>> remdup([3,5,7,5,3,7,10])
[3, 5, 7, 10]
"""

def lst2uniqLst(vLst): uniqLst = []; [uniqLst.append(i) for i in vLst if (i not in uniqLst)]; return uniqLst

#print(lst2uniqLst([3,1,3,5]))
#print(lst2uniqLst([7,3,-1,-5]))
#print(lst2uniqLst([3,5,7,5,3,7,10]))

"""
2. Write a Python function sumsquare(l) that takes a nonempty list of integers 
and returns a list [odd,even], where odd is the sum of squares all the odd 
numbers in l and even is the sum of squares of all the even numbers in l.

Here are some examples to show how your function should work.

>>> sumsquare([1,3,5])
[35, 0]

>>> sumsquare([2,4,6])
[0, 56]

>>> sumsquare([-1,-2,3,7])
[59, 4]
"""

# ==============================================================================
#even = [vLst[i] for i in range(len(vLst)) if i%2 == 0]
#print even
#odd = [vLst[i] for i in range(len(vLst)) if i%2 != 0]
#print odd 

def sumsquare(vLst):
    even = [i for i in vLst if i%2 == 0]
    odd = [i for i in vLst if i%2 != 0]
    evenSquare = map(lambda v: v**2,even)
    oddSquare = map(lambda v: v**2,odd)
    evenSum = sum(evenSquare)
    oddSum = sum(oddSquare)
    return [oddSum,evenSum]

#print(sumsquare([1,3,5]))
#[35, 0]

#print(sumsquare([2,4,6]))
#[0, 56]

#print(sumsquare([-1,-2,3,7]))
#[59, 4]

# ==============================================================================

"""
3. A two dimensional matrix can be represented in Python row-wise, as a list of 
lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3  4
5  6  7  8

would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

The transpose of a matrix converts each row into a column. The transpose of the 
matrix above is:

1  5
2  6
3  7
4  8

which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].

Write a Python function transpose(m) that takes as input a two dimensional 
matrix m and returns the transpose of m. The argument m should remain 
undisturbed by the function.

Here are some examples to show how your function should work. You may assume 
that the input to the function is always a non-empty matrix.

>>> transpose([[1,2,3],[4,5,6]])
[[1, 4], [2, 5], [3, 6]]

>>> transpose([[1],[2],[3]])
[[1, 2, 3]]

>>> transpose([[3]])
[[3]]
"""


def transposeDebug(vLst):
    """
    this is a simple zip implementation 
    22:14 10/02/2022
    """
    vLst3 = []
    [[vLst3.append(j) for j in i] for i in vLst]       #flatLst
    print len(vLst3), ". . . ."
    print vLst3
    print len(vLst3)/len(vLst), "__ __ __"
    outLst = []
    for i in range(0,int(len(vLst3)/len(vLst)),1):
        localLst = []
        print "i: ",i, "...."
        localLst.append(vLst3[i])
        #print i+ int(len(vLst3)/len(vLst))
        for m in range(len(vLst)-1):
            incrIndex = ((len(vLst[0])) * (m+1))+i
            print str(incrIndex)+"x"
            #localLst.append("i")
            localLst.append(vLst3[incrIndex])
        outLst.append(localLst)
    return outLst


def transpose(vLst):
    """
    this is a simple zip implementation 
    22:14 10/02/2022
    """
    vLst3 = []
    [[vLst3.append(j) for j in i] for i in vLst]       #flatLst
    #print len(vLst3), ". . . ."
    #print vLst3
    #print len(vLst3)/len(vLst), "__ __ __"
    outLst = []
    for i in range(0,int(len(vLst3)/len(vLst)),1):
        localLst = []
        #print "i: ",i, "...."
        localLst.append(vLst3[i])
        #print i+ int(len(vLst3)/len(vLst))
        for m in range(len(vLst)-1):
            incrIndex = ((len(vLst[0])) * (m+1))+i
            #print str(incrIndex)+"x"
            #localLst.append("i")
            localLst.append(vLst3[incrIndex])
        outLst.append(localLst)
    return outLst

print list(zip(*[[1,2,3],[4,5,6]]))     # [(1, 4), (2, 5), (3, 6)]

print(transpose([[1,2,3],[4,5,6]]))     # [[1, 4], [2, 5], [3, 6]]
print(transpose([[1],[2],[3]]))
print(transpose([[3]]))

print(transpose([[1,2,3],[4,5,6],[44,45,46]]))
