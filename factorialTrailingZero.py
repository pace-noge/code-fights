"""
Count the trailing zero of n!
"""
def factorialTrailingZeros(n):
    x = 0
    for num in range(2, n+1):
        while num > 0:
            if num % 5 == 0:
                x += 1
                num = num/5
            else:
                break
    return x