for i in range(int(input())):
    n , m = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    c = 0
    for i in range(-1 , -len(p) - 1 , -1):
        m = m - p[i]
        c = c + 1
        if m <= 0:
            print(c)
            break
    else:
        print(-1)
