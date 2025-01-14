import bisect

def ispalindrome(num):
    num_str = str(num)
    L = len(num_str)
    for i in range(L//2):
        if num_str[i] != num_str[L-i-1]:
            return False
    return True

allPalindromes = []
for num1 in range(100, 1000):
    for num2 in range(num1, 1000):
        pro  = num1 * num2
        if ispalindrome(pro):
            allPalindromes.append(pro)
allPalindromes.sort()

def getLargestPalindromeLessThan(LIM):
    ind = bisect.bisect_left(allPalindromes, LIM)
    if ind == len(allPalindromes):
        return allPalindromes[-1]
    ind -= 1
    if ind < 0:
        return -1
    return allPalindromes[ind]

for case in range(int(input())):
    N = int(input())
    print(getLargestPalindromeLessThan(N))
            
