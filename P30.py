# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    l=[int(j) for j in input().split()]
    
    s=sum(l)
    
    a=s/x
    
    c=0
    for j in l:
        t=(s-j)/(x-1)
        if a==t:
            c=l.index(j)+1
            break
    
    if c!=0:
        print(c)
    else:
        print('Impossible')
