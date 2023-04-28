# cook your dish here
t = int(input())

def alice(s,x):
  temp = s[0]
  if temp == '1':
    x.append(temp)
  else:
    x.insert(0,temp)    
  del s[0]

def bob(s,x):
  temp = s[-1]
  if temp == '1':
    x.insert(0,temp)
  else:
    x.append(temp)
  del s[-1]

for _ in range(t):
    
  n = int(input())
  s = list(input())
  x = []
  
  for i in range(n):
    if i%2 == 0:
      alice(s,x)
    else:
      bob(s,x)
  print("".join(x))
