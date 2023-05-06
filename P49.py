# cook your dish here
for _ in range(int(input())):
    n, k, v = map(int, input().split())
    a = list(map(int, input().split()))
    
    d = (n+k)*v - int(sum(a))
    if d>0 and d%k==0:
        print(d//k)
    else:
        print(-1)
    
