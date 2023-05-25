# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    a=input()
    c=0
    x=0
    for j in a:
        if(j=="*"):
            c+=1 
            x=max(x,c)
        else:
            c=0
    if x>=k:
        print("YES")
    else:
        print("NO")
