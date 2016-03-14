def GoldMineRace(cities, speed, goldmine):
    x = []
    for i in cities:
        x.append(((i[0] - goldmine[0]) **2 + (i[1] - goldmine[0]) **2) **.5)

    arrive = [x[y]/speed[y] for y in range(len(x))]
    z = []
    for y in arrive:
        if arrive.count(y) == 1:
            z.append(y)
    if len(z) == 0:
        return -1
    else:
        return arrive.index(min(arrive))
