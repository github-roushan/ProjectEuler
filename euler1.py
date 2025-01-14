
def get(num, k):
    n = num//k
    return (n * (n+1) * k) // 2

for case in range(int(input())):
    num = int(input())
    sum3 = get(num-1, 3)
    sum5 = get(num-1, 5)
    sum15 = get(num-1, 15)

    ans = sum3 + sum5 - sum15
    print(ans)
