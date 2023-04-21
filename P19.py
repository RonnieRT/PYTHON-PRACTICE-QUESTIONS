# cook your dish here
for _ in range(int(input())):
    n, x = map(int,input().split())
    enemyhealth = sorted(list(map(int,input().split())))
    maxhealth = max(enemyhealth)
    '''
    if the number enemies is greater than the health of
    the strongest enemy, the best solution is to take
    one point away from each enemy each round
    '''
    if n >= maxhealth:
        print(maxhealth)
        continue
    else:
        cnt = 0
        for enemy in enemyhealth:
            cnt += -(-enemy//x)
        print(min(cnt,maxhealth))    
    '''
    since at least one enemy has more health than the
    total number of enemies, it may be better to target
    enemies one by one.  cnt is the count of how many 
    this would be necessary, based on the max damage
    we can inflict, x
    But the final answer will depend on the size of x.
    If x is small, it may still be better to take one 
    point of health away from each enemy each turn,
    so the best answer is maxhealth
    '''    
