__author__ = 'rakesh'

def cavityMap(arr):

    newMap = []
    for i in range(len(arr)):

        x = list(str(arr[i]))
        newMap.append(x)

    for i in range(len(arr)):

        for j in range(1, len(arr)-1):

            if (int(newMap[i][j]) > int(newMap[i][j-1])) and (int(newMap[i][j]) > int(newMap[i][j+1])):
                newMap[i][j] = '0'

    for i in range(len(arr)):
        print "".join(newMap[i])


cavityMap([1112, 1912, 1892, 1234])
