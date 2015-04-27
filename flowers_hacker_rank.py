__author__ = 'rakesh'

'''
You and your K-1 friends want to buy N flowers. Flower number i has cost ci.
Unfortunately the seller does not want just one customer to buy a lot of flowers,
so he tries to change the price of flowers for customers who have already bought some
flowers. More precisely, if a customer has already bought x flowers, he should pay (x+1)*ci
dollars to buy flower number i.You and your K-1 friends want to buy all N flowers in such a way
that you spend the least amount of money. You can buy the flowers in any order.
'''
#https://www.hackerrank.com/challenges/flowers this is the problem
#questions like these makes you realize that you have to use greedy algorithm in the
#**ITERATIVELY MAKE MYOPIC DECISION AND HOPE EVERYTHING WORKS OUT AT THE END**

N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append(int(number))
   i = i + 1

if K >= N:
    result = sum(C)

else:
    C.sort()
    C = C[: : -1]  #changing the order the list from ascending to descending
    #print C
    remaining_flowers = len(C) - K
    result = sum(C[:K])

    if K >= remaining_flowers:
        x = 1
        total = 0
        for i in range(remaining_flowers):
            total = total + (x + 1)*C[K]
            K = K + 1

        result = result + total

    else:
        x = 1
        total = 0
        div = K
        for i in range(remaining_flowers):
            #print C[K]
            total = total + (x + 1)*C[K]
            K = K + 1
            if K % div == 0:
                x = x + 1


        result = result + total


print result
'''
50 3
390225 426456 688267 800389 990107 439248 240638 15991 874479 568754 729927 980985 132244 488186 5037 721765 251885 28458 23710 281490 30935 897665 768945 337228 533277 959855 927447 941485 24242 684459 312855 716170 512600 608266 779912 950103 211756 665028 642996 262173 789020 932421 390745 433434 350262 463568 668809 305781 815771 550800
output = 163578911
'''