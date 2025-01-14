
def solve(n):
    return (n * (n+1) * (3*n**2 - n - 2)) // 12

for case in range(int(input())):
    N = int(input())
    print(solve(N))
