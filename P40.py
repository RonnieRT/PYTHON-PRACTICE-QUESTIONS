# cook your dish here
t=int(input())
side1=[]
side2=[]
m,c=map(int,input().split())
while t:
    t-=1
    x,y,p=map(int,input().split())
    river=(m*x)+c
    if y>river:
        side1.append(p)
    else:
        side2.append(p)
print(max(sum(side1),sum(side2)))
