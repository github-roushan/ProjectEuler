LIM = 2*10**6
sieve = [True]*LIM
sieve[0] = sieve[1] = False

for i in range(2, LIM):
    if not sieve[i]:
        continue
    for j in range(2*i, LIM, i):
        sieve[j] = False

allPrimes = [i for i in range(LIM) if sieve[i]]
for case in range(int(input())):
    N = int(input())
    print(allPrimes[N-1])
    