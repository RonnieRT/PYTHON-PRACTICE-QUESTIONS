# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=0
    for i in range(n-k+1):
        s=sum(l[i:i+k])
        m=max(m,s)
    print(m)
