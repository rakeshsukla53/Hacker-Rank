__author__ = 'rakesh'


#Kadane Algorithm for finding the maximum contiguous Problem subarray in 1-D Sequence

#watch this video for more understanding of the problem https://www.youtube.com/watch?v=EK71U-vTOt4

x = input()


def subArray():

    y = input()
    array = raw_input().split(" ") #strings can be split not the int value

    #basically array[start:end] > sum of all the continous subsets

    sum = 0
    start = -1
    index = 0
    end = -1
    totalSum = 0

    for j in xrange(y):
        var = sum + int(array[j])  #for finding the maxinum contigous subarray
        if var > 0:
            if sum == 0:
                index = j
            sum = var
        else:
            sum = 0  #reset to zero for finding

        if var > totalSum:  #checking if the previous solution is better or this one
            totalSum = sum
            start = index
            end = j
    output = 0
    output1 = 0
    maxArray = array[start:end+1]

    if len(maxArray) != 0:


        #print maxArray
        for k in range(len(maxArray)):
            output = output + int(maxArray[k])

        for p in range(len(array)):
            if int(array[p]) >= 0:
                u = int(array[p])
                output1 = output1 + u

        print output, output1

    else:
        k = min(array)
        print k, k

for i in range(x):

    subArray()

'''
1
6
-1 -2 -3 -4 -5 -6
if all the values are negative then you need to modify you code

'''