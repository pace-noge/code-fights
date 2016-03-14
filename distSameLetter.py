def distSameLetter(s):
    from collections import OrderedDict
    y = OrderedDict()
    for x in list(OrderedDict.fromkeys(s).keys()):
        f = s.index(x)
        l = len(s) - s[::-1].index(x)
        c = l - f
        y[x] = c    
    return max(y, key=lambda x: y[x]) + str(y[max(y, key=lambda x: y[x])])
