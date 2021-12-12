with open('input.txt') as f:
    lines = list(map(int,f.read().split(',')))

print(lines)

def normalize(input,f = lambda x: x):
    l = max(input) + 1
    fuel, fuel_arr = 0,[]
    for i in range(l):
        for j in input:
            fuel += f(abs(j - i))
        fuel_arr.append(fuel)
        fuel = 0
    return min(fuel_arr)

part2 = lambda x: sum([y for y in range(1,x+1)])
normal = normalize(lines)
print(normal)
normal = normalize(lines,part2)
print(normal)




