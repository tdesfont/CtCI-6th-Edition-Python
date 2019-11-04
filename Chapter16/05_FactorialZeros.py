"""
    16.5 Factorial Zeros
"""

def getPowerDiv(n, div):
    c = 0
    while n % div == 0:
        n /= div
        c += 1
    return c

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def factorialZeros(n):
    power2 = 0
    power5 = 0
    for i in range(1, n+1): # Warning: Do not start from 0
        power2 += getPowerDiv(i, 2) # Warning: Apply on i and not n
        power5 += getPowerDiv(i, 5)
    return min(power2, power5)

if __name__ == "__main__":
    print(getPowerDiv(71, 2))
    n = 89
    print("n, n!, trailingZeros")
    print("{}, {}, {}".format(n, factorial(n), factorialZeros(n)))