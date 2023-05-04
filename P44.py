
# cook your dish here
t=int(input())

while(t>0):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    if x==1 and a[0]==y:
        print("yes")
    elif y in a:
        if(a.index(y)<x-1):
            print("yes")
        else:
            print("no")
    else:
        print("no")
    t=t-1    
