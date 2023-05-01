# cook your dish here
for _ in range(int(input())):

    a=[]
    loss=0
    for k in range(int(input())):
        b=[int(i) for i in input().split()]
        a.append(b)
        up=b[0]+(b[2]*b[0])/100
        sp=up-(up*b[2])/100
        loss+=b[0]*b[1]-sp*b[1]
    print(loss)
