__author__ = 'rakesh'

#Handling matrix related computation
#if they are allowing package then you can use pylab , numpy

#without any package

#here we will use greedy algorithm because we will
# **ITERATIVELY MAKE MYOPIC DECISION AND HOPE EVERYTHING WORKS OUT AT THE END**


#the matrix operation works here

x = input()

def grid_challenge():


    y = input()

    st = []

    output = "YES"

    for i in range(y):

        k = raw_input()
        st.append(list(k))

    for i in range(y):
        st[i].sort()

    for i in range(y):
        for j in range(y-1):
            if ord(st[i][j]) >= ord(st[i][j+1]):
                output = "NO"

    for i in range(y):
        for j in range(y-1):
            if ord(st[j][i]) >= ord(st[j+1][i]):
                output = "NO"

    print output

for k in range(x):
    grid_challenge()


'''
#handling matrix using simple list of lists

matrix = []

a = raw_input()

b = raw_input()

matrix.append(list(a))

matrix.append(list(b))

print matrix[0][0]

__author__ = 'rakesh'

'''