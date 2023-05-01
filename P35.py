goals = int(input())
for distractions in range(goals):
    wife = int(input())
    life = list(map(int, input().split()))
    aim = len(set(life))
    print((aim * (aim - 1)) // 2)
