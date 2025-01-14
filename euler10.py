
dic = {}
limit = 2*10**6
for i in range(1,limit+1):
    dic[i] = True
dic[1] = False

sm = 0
for i in range(2, limit+1):
    if dic[i]:
        sm += i
        num = i
        while num + i <= limit:
            num+=i
            dic[num] = False

print(sm)
            

