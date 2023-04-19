# cook your dish here
T = int(input())
for i in range(T):
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    Sum = 0
    for k in arr :
        Sum += k
    for j in range(Q):
        Li, Ri = map(int, input().split())
        if ((Ri-Li)+1)%2:
            Sum += 1
    print(Sum)
            
        
