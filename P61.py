# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(1,n+1):
        if i not in a:
            b.append(i)
    even_elements=[str(b[i]) for i in range(0, len(b),2)]
    odd_elements=[str(b[i]) for i in range(1,len(b),2)]
    if len(even_elements) > 0:
        print(*even_elements)
    else:
        print(-1)
    
    if len(odd_elements) > 0:
        print(*odd_elements)
    else:
        print(-1)

    
