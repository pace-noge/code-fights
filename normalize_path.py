def simplifyPath(path):

    parts = path.split("/")
    simplified = [''] * len(parts)
    length = 0
    for part in parts:
        if part == '.' or part == '' or part == '..':
            if part == '..' and length > 0:
                length -= 1
            continue
        simplified[length] = part
        length += 1

    if length == 0:
        return '/'

    result = ''
    for i in range(length):
        result += '/' + simplified[i]

    return result
