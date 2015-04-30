__author__ = 'rakesh'

#Analyzing the stock market and how to maximize the profit when you know the price for next N days.

#https://www.hackerrank.com/challenges/stockmax

x = 1
PROFIT = 0

def stockMax():

    y = 9  #stock prices for N days

    price = [1, 2, 100]  #the numbers are stored as character but when you intialize it they are integers

    def findMax(stockList = []):  #using recursion to find the maximum profit we can obtain

        global PROFIT

        highestShare = max(stockList)
        l = len(stockList)
        maxProfit = []
        count = 0
        shares = 0
        if l == 1:
            return 0

        elif highestShare == stockList[l-1]:
            for k in range(l-1):
                shares = shares + int(stockList[k])
                count = count + 1
            highestShare = int(highestShare)
            PROFIT = PROFIT + (highestShare*count - shares)
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

