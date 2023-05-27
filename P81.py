# cook your dish here
t=int(input())
while t>0:
    n,x,y=map(int,input().split())
    a=x*y
    if a>=n:
        print("YES")
    else:
        print("No")
    t-=1
