
"""
Implement a function that can reduce a fraction.

Example

fractionReducing([2, 6]) = [1, 3]
fractionReducing([4, 1]) = [4, 1]
[input] array.integer fraction

array A of two positive integers representing fraction A[0] / A[1]
[output] array.integer

reduced version of A
"""
def fractionReducing(fraction):

    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    commonDivisor = gcd(fraction[0], fraction[1])
    fraction[0] /= commonDivisor
    fraction[1] /= commonDivisor

    return fraction
