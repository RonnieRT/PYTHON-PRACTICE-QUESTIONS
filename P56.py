# cook your dish here
for _ in range(int(input())):
    n=input()
    if int(n[0])>1:
        print("1"+n)
    else:
        print(n[0]+"0"+n[1:])
