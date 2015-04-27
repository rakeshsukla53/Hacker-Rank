__author__ = 'rakesh'

def doesCircleExists(commands):

    x = list(commands)

    y = len(set(x))


    if len(x) == y:
        return 'YES'
    else:
        return 'NO'

print doesCircleExists('RLG')

