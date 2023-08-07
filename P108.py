# cook your dish here
a,b,c,d = map(int,input().split())
ts1=a*2+b
ts2 = c*2+d
if(ts1 == ts2):
    print("Equal")
elif(ts1>ts2):
    print("Messi")
else:
    print("Ronaldo")
