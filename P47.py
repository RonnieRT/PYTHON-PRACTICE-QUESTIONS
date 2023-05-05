# cook your dish here
for t in range(int(input())):
    N = int(input())
    S = input()
    if N == 2: print(1)
    else:
        ans = S.count("01")
        if S[0] == '1': ans += 1
        if S[-1] == '0': ans += 1
        print(ans)
