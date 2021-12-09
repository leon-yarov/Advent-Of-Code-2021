with open('input.txt') as f:
    lines = f.read().replace('->','').split()
    lines = list(map(tuple,map(lambda x: x.split(','),lines)))
    lines = [(int(x[0]),int(x[1])) for x in lines]

area = {}


def interpolate(p1,p2,diagonal = True):
    n,arr = p1, []
    y = p2[1] - p1[1]
    x = p2[0] - p1[0]
    if (y != 0 and x != 0 and diagonal): return []
    if y < 0:
        y = -1
    elif y > 0:
        y = 1
    if x < 0:
        x = -1
    elif x > 0:
        x = 1
    while n != p2:
        arr.append(n)
        n = (n[0] + x, n[1] + y)
    arr.append(p2)
    return arr


def part1(lines,diagonal = True):
    for i in range(0,len(lines),2):
        for n in interpolate(lines[i],lines[i+1],diagonal):
            if n not in area.keys():
                area[n] = 1
            else: area[n] += 1
        # print(interpolate(lines[i],lines[i+1]))
    ans = len(area.values()) - list(area.values()).count(1)
    print(ans)

if __name__ == '__main__':
    part1(lines)
    area = {}
    part1(lines,False)
