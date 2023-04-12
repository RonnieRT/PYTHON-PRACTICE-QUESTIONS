# function to calculate strike rate
def calc_strike_rate(runs, balls):
    if balls == 0:
        return 0
    else:
        return (runs / balls) * 100

# main program
t = int(input())

for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))

    runs = 0
    balls = 0
    count = 0

    for i in range(n):
        runs += g[i]
        balls += 1
        sr = calc_strike_rate(runs, balls)
        if sr == 100:
            count += 1

    print(count)
