# cook your dish here
for i in range(int(input())):
    n=int(input())
    st=input()
    a=0
    b=0
    s=1
    r=0
    for j in range(n):
        if s==1:
            if st[j]=="A":
                a+=1 
            else:
                s=0
        else:
            if st[j]=="B":
                b+=1 
            else:
                s=1 
    print(a,b)
