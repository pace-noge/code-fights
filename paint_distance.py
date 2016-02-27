def requestMatching(pros, distances, travelPreferences):
    matching_score = {}
    non_match_score = {}
    for x in range(len(pros)):
        if distances[x] <= travelPreferences[x]:
            matching_score[pros[x]] = distances[x]
        else:
            non_match_score[pros[x]] = distances[x] - travelPreferences[x]

    if len(matching_score) >= 5:
        return sorted(matching_score, key=lambda x: (matching_score[x], x))
    else:
        return sorted(matching_score, key=lambda x: (matching_score[x], x)) + sorted(non_match_score, key=lambda x: (non_match_score[x], x))[:5-len(matching_score)]


if __name__ == "__main__":
    pros = ["Michael", "Mary", "Ann", "Nick", "Dan", "Mark"]
    distances = [12, 10, 19, 15, 5, 20]
    travelPreferences = [12, 8, 25, 10, 3, 10]
    print requestMatching(pros, distances, travelPreferences)

