# cook your dish here
for i in range(int(input())):
    s=input()
    if(len(s)<5):
        print(s)
        continue
    res=""
    if("party" in s):
        res=s.replace("party","pawri")
        print(res)
    else:
        print(s)
  
