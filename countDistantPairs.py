"""
Given a string inputString and an integer distance, find the number of pairs of equal characters in the inputString delimited by exactly distance characters.

Example

for inputString = "abacaba", distance = 1 output should be 3
for inputString = "abacaba", distance = 2 output should be 0
for inputString = "abacaba", distance = 3 output should be 3
[input] string inputString

a string of lowercase letters
[input] integer distance

a positive integer
[output] integer


"""
countDistantPairs = lambda s, d: len([i for i in [s[i:i+d+2] for i in range(len(s))] if len(i)==d+2 and i[0] == i[-1]])