__author__ = 'rakesh'


#modified fibonacii series
#this is modified version

#solving fibonacci using dynamic programming and this is a modified one
'''

Given the nth and (n+1)th terms, the (n+2)th can be computed by the following relation
Tn+2 = (Tn+1)2 + Tn
'''

n = raw_input().split(" ")

first = int(n[0])
second = int(n[1])
n = int(n[2])

memory = [] #initalizae the memory with input -1

for i in range(n+1):
    memory.append(-1)


def fibonacci(n):

    if memory[n] == -1:

        if n == 0:

            memory[n] = first  #this is fibonacci series using top down approach

        elif n == 1:
            memory[n] = second

        else:

            memory[n] = pow(fibonacci(n-1), 2) + fibonacci(n-2)

    return memory[n]

fibonacci(n)

print memory[0:n]



