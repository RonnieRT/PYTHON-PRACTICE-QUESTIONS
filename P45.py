# cook your dish here
import statistics
from statistics import mode
t=int(input())

while(t>0):
    x=int(input())
    l=list(map(int,input().split()))
    m=mode(l)
    if(l.count(m)>(x+1)//2):
        print("no")
    else:
        print("yes")
    t=t-1    
    
    
    
