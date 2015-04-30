__author__ = 'rakesh'

#Analyzing the stock market and how to maximize the profit when you know the price for next N days.

#https://www.hackerrank.com/challenges/stockmax

x = input()
PROFIT = 0

def stockMax():

    global PROFIT
    PROFIT = 0

    y = input()  #stock prices for N days

    price = raw_input().split(" ") #the numbers are stored as character but when you intialize it they are integers

    price = map(int, price)

    def findMax(stockList = []):  #using recursion to find the maximum profit we can obtain

        global PROFIT

        highestShare = max(stockList)
        l = len(stockList)
        count = 0
        shares = 0
        if l == 1:
            return 0

        elif highestShare == stockList[l-1]:
            for k in range(l-1):
                shares = shares + int(stockList[k])
                count = count + 1

            PROFIT = PROFIT + (int(highestShare*count) - shares)

            return PROFIT

        else:

            for i in range(l):

                if stockList[i] == highestShare:
                    left = stockList[0:i+1]
                    right = stockList[i+1:l]
                    findMax(left)
                    findMax(right)
                    break


        return PROFIT


    print findMax(price)


for i in range(x):

    stockMax()

