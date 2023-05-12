# cook your dish here
for _ in range(int(input())):
    s='abcdefghijklmnopqrstuvwxyz'
    n,x=map(int,input().split())
    if n<2*x-1:
        print(-1)
    elif n==2*x-1:
        print(s[:x]+s[:x-1][::-1])
    else:
        print(s[:x]+(s[0]*(n-(2*x)))+s[:x][::-1])
