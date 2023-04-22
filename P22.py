# cook your dish here
tc=int(input())
for t in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    flag=0
    c=0
    for i in a:
        if i>n:
           flag=1 
           break
    sc=0
    l1=[]
    for i in range(1,n+1):
        l1.append(i)
    sum=0
    for i in range(n):
        if l1[i]-a[i]>=0 :
            sum+=l1[i]-a[i]
        else:
            flag=1 
            break
    if flag==1:
        print(-1)
    else:
        print(sum)
        
