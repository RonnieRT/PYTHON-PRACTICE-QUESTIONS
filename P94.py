# cook your dish here
num =int(input())
for i in range(num):
    a=input()
    b=a.split()
    if int(b[0])>=int(b[1]):
        print("yes")
    else:
        print("no")
