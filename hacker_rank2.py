__author__ = 'rakesh'

x = raw_input()

open = '('
close = ')'

y = list(x)

count1 = 0
count2 = 0
count = 0
reverseCount = 0

for i in range(len(y)):

    if open == y[i]:
        count1 = count1 + 1

    else:
        count2 = count2 + 1

if count1 != count2:
    print -1

else:
    for i in range(len(y)-1):
        if (y[i] == open) and (y[i+1] != close):
            count = count + 1

    z = y[: : -1]

    for i in range(len(z)-1):
        if (z[i] == open) and (z[i+1] != close):
            reverseCount = reverseCount + 1

    if reverseCount >= count:
        print reverseCount

    else:
        print count



