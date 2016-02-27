
def search_nested(mylist, val):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            if mylist[i][j] == val:
                return True
    return False

def spamClusterization(requests, IDs, threshold):
    list_of_sets = []
    result = []
    if len(requests) <= 1:
        return []
    for req in requests:
        set_of_words = set([i.strip(",.?!") for i in req.lower().split()])
        list_of_sets.append(set_of_words)

    for i in range(len(list_of_sets)):
        A = list_of_sets[i]
        hasil = []
        hasil.append(IDs[i])
        for x in range(len(list_of_sets)):
            B = list_of_sets[x]
            if i != x:
                jaccard_index = float(len(A & B)) / float(len(A | B))
                if jaccard_index >= threshold:
                    hasil.append(IDs[x])
        if len(hasil) > 1:
            result.append(sorted(hasil))


    # temp_result = [list(x) for x in set(tuple(x) for x in result)]
    temp_result = map(list, set(map(tuple, sorted(result, key=lambda x: x[0]))))
    #print temp_result
    hasil = []
    for x in temp_result:
        #print hasil
        if not hasil:
            hasil.append(x)
        else:
            if not search_nested(hasil, x[0]):
                hasil.append(x)

            # for y in hasil:
            #     if x[0] not in y:
            #         print x[0] in y
            #         print x[0]," ",hasil
            #         hasil.append(x)


    print sorted(hasil, key=lambda x: x[0])




if __name__ == "__main__":
    requests = ["ab","cd","ef"]
    IDs = [1,2,3]
    threshold = 0.5
    spamClusterization(requests, IDs, threshold)
