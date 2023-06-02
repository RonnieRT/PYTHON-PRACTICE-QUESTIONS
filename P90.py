for i in range(int(input())):
    x,y,z=map(int,input().split())
    k=[x,y,z].count(0)
    if k>=2: print('Water filling time')
    else: print("Not now")
    
