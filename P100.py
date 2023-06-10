t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    x=x*5
    if x>=y:
        print("YES")
    else:
        print("NO")
