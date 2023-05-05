for _ in range(int(input())):
    N = int(input())
    S = [0,0,0,0,0,0,0,0,0,0]
    for i in range(N):
        a = list(input())
        for x in range(10):
            S[x] = S[x] ^ int(a[x])
            
    print(S.count(1))
