# cook your dish here
for _  in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    j=n-1
    x=0
    y=0
    while i<=j:
        if x<y:
            x+=a[i]
            i+=1
        else:
            y+=a[j]
            j-=1
    print(max(x,y))
