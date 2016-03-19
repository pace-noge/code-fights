"""
Given a string s of lowercase Latin letters ('a' - 'z'), get the maximum distance between two same letters, and return this distance along with the letter that formed it.

If there is more than one letter with the same maximum distance, return the one that appears in s first.

Example:

For s = "fffffahhhhhhaaahhhhbhhahhhhabxx" the answer should be distSameLetter(s) = "a23".

The maximum distance is formed by the character 'a' from index 5 to index 27 (0-based). Therefore, the answer is "a23".

[input] string s

A string of lowercase Latin letters, where at least one letter appears twice.
[output] string

The letter that formed the maximum distance and the distance itself.
"""
def distSameLetter(s):
    from collections import OrderedDict
    y = OrderedDict()
    for x in list(OrderedDict.fromkeys(s).keys()):
        f = s.index(x)
        l = len(s) - s[::-1].index(x)
        c = l - f
        y[x] = c    
    return max(y, key=lambda x: y[x]) + str(y[max(y, key=lambda x: y[x])])
