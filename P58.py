for _ in range(int(input())):
  n=int(input())
  l=[0]*(n**2)
  for i in range(n):
    r=list(map(int,input().split()))
    for j in range(n):
      x=r[j]  
      l[x-1]=[i+1,j+1]
    
  c=0
  for x in range(1,n**2):
    a=l[x-1]
    b=l[x]
    
    c+=abs(a[0]-b[0])+abs(a[1]-b[1])
    
  print(c)
