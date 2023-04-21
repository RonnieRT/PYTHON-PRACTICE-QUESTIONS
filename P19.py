# cook your dish here
for _ in range(int(input())):
    n, x = map(int,input().split())
    enemyhealth = sorted(list(map(int,input().split())))
    maxhealth = max(enemyhealth)
    if n >= maxhealth:
        print(maxhealth)
        continue
    else:
        cnt = 0
        for enemy in enemyhealth:
            cnt += -(-enemy//x)
        print(min(cnt,maxhealth))       
