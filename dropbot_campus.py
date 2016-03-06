def campusCup(emails):
    emails_dict = {}
    ranks = {}
    points = {}
    for email in emails:
        domain = email.split("@")[1]
        acc = email.split("@")[0]
        if domain not in emails_dict:
            emails_dict[domain] = [acc]
        else:
            emails_dict[domain].append(acc)

    for x in emails_dict:
        point = len(emails_dict[x]) * 20
        ranks[x] = point
        if point >= 500:
            additional = 25
        elif point >= 300:
            additional = 15
        elif point >= 200:
            additional = 8
        elif point >= 100:
            additional = 3
        else:
            additional = 0
        points[x] = additional

    return sorted(points, key=lambda x: (-points[x], x))

print campusCup(["a@rain.ifmo.ru", "b@rain.ifmo.ru", "c@rain.ifmo.ru", "d@rain.ifmo.ru", "e@rain.ifmo.ru", "noname@mit.edu"])

