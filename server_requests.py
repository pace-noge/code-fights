def processingRequests(servers, requests):
    hasil = []
    x = []
    result = []
    y = []
    for i in range(1, servers + 1):
        process_data = range(1, (2*i)+1)
        y.append(process_data)
        hasil.append([x for x in requests if x in process_data])
    #for x in range(len(hasil)):
    for i in range(len(hasil)):
        print max(y[i])
        print i
        if requests[i] > i and requests[i] <= max(y[i]):
            result.append(requests[i])
        print result
    print result
    return len(result)



if __name__ == "__main__":
    print processingRequests(10, [1, 2, 3, 5, 7, 11, 13, 15, 19, 22, 27, 30, 2000])