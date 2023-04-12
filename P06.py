# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=((15*a)-(2*b));
    if(c<0):
        print("no")
    else:
        print("yes")
