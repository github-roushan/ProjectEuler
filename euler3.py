#!/bin/python3

def getMaxPrime(num):
    prime = 2
    maxPrime = 0
    while prime**2 <= num:
        while num % prime == 0:
            maxPrime = max(prime, maxPrime)
            num = num // prime
        prime += 1
        if prime % 2 == 0:
            prime += 1
    if num > 1:
        maxPrime = max(maxPrime, num)
    return maxPrime

for case in range(int(input())):
    N = int(input().strip())
    print(getMaxPrime(N))
