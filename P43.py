# cook your dish here
for  i in range(int(input())):
    A,B=map(int,input().split())
    if A-A*10/100 > B:
        print('DINING')
    elif B > A - A*10/100:
        print("ONLINE")
    else:
        print("EITHER")
