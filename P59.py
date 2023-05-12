for i in range(int(input())):
    a=input().split()
    b=[]
    for i in range(len(a)):
        b.append(a[i].capitalize())
    c=[]
    if len(b)>1:
        for i in range(len(b)-1):
            d=b[i]
            c.append(d[0]+'.')
        c.append(b[-1])
        print(*c)
    else:
        print(b[-1])
        
