# cook your dish here
for i in range(int(input())):
    d=input()
    print("Yes" if d.count("0")==1 or d.count("1")==1 else "No")
