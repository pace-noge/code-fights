def processingRequests(servers, requests):
    hasil = []
    for i in range(1, servers + 1):
        hasil.append([x for x in requests[:2*i] if x < ])
    print hasil
    return len(hasil)



if __name__ == "__main__":
    print processingRequests(2, [1, 5, 6])