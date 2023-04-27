# cook your dish here
for _ in range(int(input())):
    s = input()
    t = []
    for j in range(len(s)-1):
        if(not(s[j]+s[j+1] in t)):
            t.append(s[j]+s[j+1])
    print(len(t))
