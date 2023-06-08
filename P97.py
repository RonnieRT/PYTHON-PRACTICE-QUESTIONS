# cook your dish here
t=int(input())
while t>0:
    a,b=map(int,input().split())
    if b>=a:
        print("YES")
    else:
        print("NO")
    t=t-1    
