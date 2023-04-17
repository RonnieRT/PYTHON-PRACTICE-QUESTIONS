# cook your dish here
from collections import Counter
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=Counter(l)
    for a,b in c.most_common(1):
        m=b
    print(n-m)
