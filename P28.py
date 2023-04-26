# cook you dish here
for i in range(int(input())):
    n=int(input())
    q=list(map(int,input().split()))
    l=[]
    r=0
    for j in range(n-1):
        if q[j+1]-q[j]<=2:
            r+=1 
        else:
            l.append(r+1)
            r=0
    l.append(r+1)
   
    print(min(l),max(l))    
