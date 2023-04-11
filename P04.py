# cook your dish here 
a = int(input())
for _ in range(a):
    b = int(input())
    lis = list(map(int, input().split()))
    c = 0 
    for i in range(b):
        p = 1
        s = 0
        for i in range(i,b):
            s = s + lis[i] 
            p = p * lis[i] 
            if s ==  p:
                c = c + 1 
    print(c)
    
    
    
