# cook your dish here
t=int(input())

for tc in range(t):

    x,y,k,n=map(int,input().split())
    a=x-y
    b=0
    for j in range(n):
        p,c=map(int,input().split())
        if p>=a:
            if k-c>=0:
                b+=1
    if b>0:
        print("LuckyChef")
    else:
        print("UnluckyChef")
