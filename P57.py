# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    flag = True
    for i in range(1,n):
        if a[i-1]>a[i]:
            if (a[i-1]+a[i])<=x:
                a[i-1],a[i] = a[i],a[i-1]
            else:
                flag = False
                break
    if flag: print("YES")
    else: print("NO")
            
