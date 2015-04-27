__author__ = 'rakesh'


N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append(int(number))
   i = i + 1

count = 0

for i in range(len(C)):

    for j in range(len(C)):

        if abs(C[i] - C[j]) == K:
            count = count + 1

result = count/2

print result

