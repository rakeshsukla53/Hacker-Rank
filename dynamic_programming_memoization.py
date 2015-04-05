__author__ = 'rakesh'


n = input("Enter any number")

memory = [] #initalizae the memory with input -1

for i in range(n+1):
    memory.append(-1)


def fibonacci(n):

    if memory[n] == -1:

        if n <= 1:

            memory[n] = 1  #this is fibonacci series using top down approach

        else:

            memory[n]= fibonacci(n-1) + fibonacci(n-2)

    return memory[n]

fibonacci(n)

print memory




