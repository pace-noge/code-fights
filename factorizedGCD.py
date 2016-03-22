"""
Find the greatest common divisor of two given integers. Each integer is given in the form of its prime factorization - a sorted array of all prime factors of the number.

Example

gcd([2, 3, 3, 3, 5], [2, 2, 2, 2, 3, 3]) = 18 (= gcd(270, 144)).

[input] array.integer a

A prime factorization of an integer greater than 1.
[input] array.integer b

A prime factorization of an integer greater than 1.
[output] integer


"""

def factorizedGCD(a, b):
    j = 0
    result = 1
    for i in range(len(a)):
        while j < len(b) and a[i] > b[j]:
            j += 1
        if j < len(b) and a[i] == b[j]:
            result *= b[j]
            j += 1
    return result