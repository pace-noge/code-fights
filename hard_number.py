def countDown(n):
    if n % 3 != 0:
        return str(-1)
    s = zip(*(iter(range(n, 0, -1)),) *3)
    f = "".join(str(y) for y in s[0])
    for x in s[1:]:
        print x
        f += "".join(sorted("".join(str(y) for y in x))
    print f
    return f


countDown(9)