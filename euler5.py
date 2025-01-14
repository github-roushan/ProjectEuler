from math import gcd

def _lcm(a, b):
    return a*b // gcd(a, b)

def LCM(li: list) -> int:
    lcm = 1
    for it in li:
        lcm = _lcm(it, lcm)
    return lcm
    
for case in range(int(input())):
    N = int(input())
    L = list(range(1, N+1))
    print(LCM(L))