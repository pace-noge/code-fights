def ratingThreshold(threshold, ratings):
    hasil = []
    for x in ratings:
        # print x
        # print (sum(x)/float(len(x))) < threshold
        if (sum(x)/float(len(x))) < threshold:
            hasil.append(ratings.index(x))
    return hasil


if __name__ == "__main__":
    ratings = [[3, 4],
        [3, 3, 3, 4],
        [4]]
    threshold = 3.5
    print ratingThreshold(threshold, ratings)
