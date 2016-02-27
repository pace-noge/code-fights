def processingRequests(servers, requests):
    hasil = []
    x = []
    result = []
    for i in range(1, servers + 1):
        process_data = range(1, (2*i)+1)
        hasil.append([x for x in requests if x in process_data])
    #for x in range(len(hasil)):
    for i in range(len(hasil)):
        if len(hasil[i]) > i:
            result.append(hasil[i][i])
    print result
    return len(result)



if __name__ == "__main__":
    print processingRequests(3, [1,2,3,4,5,6,7,8,9,10])