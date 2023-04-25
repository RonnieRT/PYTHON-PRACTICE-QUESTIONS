# cook your dish here
goals = int(input())
for distractions in range(goals):
    aim = int(input())
    chef = ''
    for stress in range(aim):
        chef += input()
    life = []
    life.append(chef.count('c') // 2)
    life.append(chef.count('o'))
    life.append(chef.count('d'))
    life.append(chef.count('e') // 2)
    life.append(chef.count('h'))
    life.append(chef.count('f'))
    print(min(life))
