def get_median(list):
    if len(list) % 2 == 0:
        return sum([list[:len(list)/2][0], list[len(list)/2:][1]])/2.0
    else:
        return len(list)/2.0

def priceSuggestion(contractData):
    if contractData:
        contractData = sorted(contractData)
        first_group = contractData[:len(contractData)/2]
        second_group = contractData[len(contractData)/2:]
        print second_group
        if len(first_group) % 2 == 0:
            first_median = first_group[int(get_median(first_group)-1)]
        else:
            first_median = first_group[int(get_median(first_group))]
        second_median = second_group[int(get_median(second_group))]
        return [first_median, second_median]
    return []


if __name__ == "__main__":
    print priceSuggestion([1, 5, 6, 3, 2, 4, 7, 8])