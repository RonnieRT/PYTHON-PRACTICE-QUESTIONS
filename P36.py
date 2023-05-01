for _ in range(int(input())):
    s, n = map(int,input().split())
    
    if s<n:
        if s%2 == 0 or s==1:
            print('1')
        else:
            print('2')
    else:
        c = s // n 
        r = s - c*n 
        if r == 0:
            print(c)
        elif r==1 or r%2 == 0:
            print(c+1)
        else:
            print(c+2)
