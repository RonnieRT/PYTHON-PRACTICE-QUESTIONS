# cook your dish here
t=int(input())
for x in range(t):
    a=[int(c) for c in input().split()]
    if a[0]>a[1]:
        print("LOSS")
    elif a[0]<a[1]:
        print("PROFIT")
    else:
        print("NEUTRAL")
    
