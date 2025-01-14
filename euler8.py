from functools import reduce

def arrProduct(li):
    product = reduce(lambda a,b: a*b, li)
    return product

def horizontal(li, times):
    ans = 0
    for row in li:
        for i in range(len(row) - times + 1):
            ans = max(ans, arrProduct(row[i:i+times]))  
    return ans

def vertical(li, times):
    ans = 0
    for col in zip(*li):
        for i in range(len(col) - times + 1):
            ans = max(ans, arrProduct(col[i:i+times]))
    return ans

def leftDiagonal(li, times):
    row, col = len(li), len(li[0])
    ans = 0
    for r in range(row-times+1):
        for c in range(col-times+1):
            pr = 1
            for i in range(times):
                pr*=li[r+i][c+i]
            ans = max(ans, pr)
    return ans

def rightDiagonal(li, times):
    row, col = len(li), len(li[0])
    ans = 0
    for r in range(row-times+1):
        for c in range(times-1, col):
            pr = 1
            for i in range(times):
                pr*=li[r+i][c-i]
            ans = max(ans, pr)
    return ans

def solve(li, times):
    ans = horizontal(li, times)
    ans = max(vertical(li, times), ans)
    ans = max(leftDiagonal(li, times), ans)
    ans = max(rightDiagonal(li, times), ans)
    return ans

with open('euler8_data', 'r') as fil:
    dat = fil.read()
    dat = dat.split('\n')
    dat = ''.join(dat)
    if dat[-1] == '':
        dat = dat[:-1]
    li = [list(map(int, list(st))) for st in dat]

ans = solve(li, 13)
print(ans)
