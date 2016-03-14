def distSameLetter(s):
    set_s = set(s)
    f = {}
    for x in set_s:
        first = s.index(x)
        last = s[::-1].index(x)
        count = len(s) - last
        tot = count-first
        f[x] = tot

    return sorted(f, key= lambda x: f[x], reverse=True)[0]+str(f[sorted(f, key= lambda x: f[x], reverse=True)[0]])