
## f0, f1, f2 = 0, 1, 1

def getEvenFibSumUnder(LIM):
    f2, f3  = 1, 2
    totalEvenFibonacciSum = 0

    while f3 < LIM:
        totalEvenFibonacciSum += f3
        ## every 3rd number is even fib
        f2, f3 = f3, f2+f3
        f2, f3 = f3, f2+f3
        f2, f3 = f3, f2+f3
    
    return totalEvenFibonacciSum

for case in range(int(input())):    
    N = int(input())
    print(getEvenFibSumUnder(N))
