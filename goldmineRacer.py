"""
On a particular continent far far away, a precious gold mine was reported to be found. Every country started to gather up armies and went for the mine. Only one will dominate!



Given the x and y coordinates of each city on the continent, the coordinates of the goldmine and speed of each army, determine which country will take over the gold mine if all armies start to move from the cities simultaneously.

The first army to reach the mine captures it. However, if two or more armies reach the gold mine at the same time, they will fight to death, so none of them will get it.

Example:

For cities = [[3,0],[2,0],[0,1]], speed = [3,3,3] and goldmine = [0, 0], the answer should be
GoldMineRace(cities, speed, goldmine) = 2.
The armies travel with the same speed, but the second city (0-based) is closer to the gold mine than other two, so their army will reach the mine first.

For cities = [[-3,-4],[3,4],[-3,4],[3,-4]], speed = [5, 5, 2, 2] and goldmine = [0, 0], the answer should be
GoldMineRace(cities, speed, goldmine) = -1.
At first armies from cities 2 and 3 will meet and fight to death. After some time, armies from cities 0 and 1 will battle for the mine and die a heroic death. Thus, no one will conquer the mine, so the answer is -1.

[input] array.array.integer cities

A matrix of cities' coordinates in the format [x, y].
[input] array.float speed

Array of the same length as cities, speed[i] is the speed of the army from cities[i].
[input] array.integer goldmine

The mine's coordinates in the format [x, y].
[output] integer

The 0-based index of the country that will dominate, or -1 if no one will.

"""

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
