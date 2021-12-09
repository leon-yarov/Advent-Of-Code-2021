with open('input.txt') as f:
    lines = f.read().split(',')
    # lines = "3,4,3,1,2".split(',')
    lines = list(map(int, lines))



def fish(initial,days):
    fish_per_day = {x:0 for x in range(0,9)}
    for i in initial:
        fish_per_day[i] += 1
    for i in range(days):
        zero = fish_per_day[0]
        for n in range(0,len(fish_per_day)-1):
            fish_per_day[n] = fish_per_day[n+1]
        fish_per_day[8] = zero
        fish_per_day[6] += zero
    return fish_per_day

print(sum(fish(lines,80).values()))
print(sum(fish(lines,256).values()))
