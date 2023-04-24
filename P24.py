
n=int(input())
for i in range(n):
    n,y=list(map(int,input().split()))
    a=list(map(int,input().split()))
    initial= 0
    for i in range (n):
        initial|=a[i]

    re=initial^y
    
    if(re|initial==y):
        print(re)
    else:
        print("-1")
        
  
