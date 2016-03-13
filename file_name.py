def fileName(docs):
    r = []
    for i in docs:
        if i in r:
            for x in range(1, len(docs)):
                if i+"({})".format(x) not in r:
                    r.append(i+"({})".format(x))
                    break
        else:
            r.append(i)

    return r


print fileName(["doc", "doc", "image", "doc(1)", "doc"])
