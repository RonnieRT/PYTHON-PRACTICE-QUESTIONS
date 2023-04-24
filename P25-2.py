t = int(input())
for i in range(t):
    n = input()
    c0 = n.count("0")
    c1 = n.count("1")
    if c0 == 1 or c1 == 1:
        print("Yes")
    else:
        print("No")
