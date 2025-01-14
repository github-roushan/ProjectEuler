'''
a^2 + b^2 = c^2
a = 2mn
b = m*2 - n*2
c = m*2 + n*2

a+b+c = N
implies
2m(m+n) = N
'''

def solve(N):
    if N % 2:
        return -1
    maxProduct = -1
    for m in range(1, N//2+1):
        m_n = N//(2*m)
        n = m_n - m
        if n <= m:
            break
        curProduct = 2*m*n * (m**2 + n**2) * (m**2 - n**2)
        maxProduct = max(maxProduct, curProduct)
        print(2*m*n , (m**2 + n**2) , (m**2 - n**2))
    return maxProduct

for case in range(int(input())):
    N = int(input())
    print(solve(N))
