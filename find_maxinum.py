__author__ = 'rakesh'

#Questions - https://www.hackerrank.com/challenges/maximizing-xor

maxValue = []

l = raw_input("Enter the value for l")
r = raw_input("Enter the value for r")

l = int(l)
r = int(r)

for a in range(l,  r+1):

    for b in range(a, r+1):

        maxValue.append(a^b)


print max(maxValue)














