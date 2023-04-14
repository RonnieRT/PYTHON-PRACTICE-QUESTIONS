# cook your dish here
for _ in range(int(input())):
    x=input("")
    a=x.count("1")
    b=x.count("0")
    if(a<=b):
        print("LOSE")
    else:
        print("WIN")
