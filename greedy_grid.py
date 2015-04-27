__author__ = 'rakesh'

#here we will use greedy algorithm because we will
# **ITERATIVELY MAKE MYOPIC DECISION AND HOPE EVERYTHING WORKS OUT AT THE END**

from pylab import *

#the matrix operation works here

x = input()

y = input()

st = []

output = "YES"

for i in range(y):

    k = raw_input()
    st.append(list(k))

m = array(st)

for i in range(y):
    m[i].sort()

for i in range(y):
    for j in range(y-1):
        if ord(m[i][j]) >= ord(m[i][j+1]):
            output = "NO"

for i in range(y):
    for j in range(y-1):
        if ord(m[j][i]) >= ord(m[j+1][i]):
            output = "NO"

print output







