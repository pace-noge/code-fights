def processingRequests(servers, requests):
    return min(sum(i < 2 * servers for i in requests), servers)


if __name__ == "__main__":
    print processingRequests(10, [1, 2, 3, 5, 7, 11, 13, 15, 19, 22, 27, 30, 2000])