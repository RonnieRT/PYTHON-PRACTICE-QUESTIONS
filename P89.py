# cook your dish here    
x,y,n = map(int,input().split())
if n==1:
    print(x*n)
else:
    print((n-1)*y+x)
