# cook your dish here
n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    a = [x, y, z]
    print(sorted(a)[1])
