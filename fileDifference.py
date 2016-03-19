"""
Once upon a time there was a File. It was perfect and there was no need to change it. But one day a group of programmers came across it and decided to make a couple of changes by adding new symbols here and there. They ended up with two versions of the File. You think that the programmers didn't have enough time to ruin it completely, so you want to restore it.

Your approach is as follows: if a string result can be obtained from both versions by removing some symbols in them, then it can be the File. You need to find the longest result possible.

Example

For version1 = 'CodeFigh#ts' and version2 = 'Co$deFig?hts' the output should be 'CodeFights'.

[input] string version1

[input] string version2

[output] string
"""

def theFile(version1, version2):

    len1 = len(version1)
    len2 = len(version2)
    maxLen = []
    take = []
    maxLen.append([0] * (len2 + 1))
    take.append([False] * (len2 + 1))
    for i in range(1, len1 + 1):
        maxLen.append([0] * (len2 + 1))
        take.append([False] * (len2 + 1))
        for j in range(1, len2 + 1):
            if version1[i - 1] == version2[j - 1]:
                maxLen[i][j] = maxLen[i - 1][j - 1] + 1
                take[i][j] = True
            else:
                maxLen[i][j] =  maxLen[i][j]+1
    answer = []
    i = len1
    j = len2
    while i > 0 and j > 0:
        if take[i][j]:
            i -= 1
            j -= 1
            answer.append(version1[i])
        else:
            if maxLen[i - 1][j] > maxLen[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return ''.join(list(reversed(answer)))
