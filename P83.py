# cook your dish here
t=int(input())
while t>0:
    n,flag=int(input()),0
    s=input()
    d={}
    for i in s:
        d[i]=d.get(i,0)+1 
        if d[i]==2:
            flag=1
            break
    if flag==0:
        print(-1)
    else:
        print(n-2)
    t=t-1
    
        
    
