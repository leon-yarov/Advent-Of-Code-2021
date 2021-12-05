with open('input.txt') as f:
    puzzle = f.read().split()

def move():
    forward,depth = 0,0
    for i,n in enumerate(puzzle):
        if n == 'forward': forward += int(puzzle[i+1])
        elif n == 'down': depth += int(puzzle[i+1])
        elif n == 'up': depth -= int(puzzle[i+1])
    print(forward * depth)

move()


def aim():
    depth,horizontal,aim = 0,0,0
    for i,n in enumerate(puzzle):
        if n == 'forward':
            horizontal += int(puzzle[i+1])
            depth +=  aim * int(puzzle[i+1])
        elif n == 'down': aim += int(puzzle[i+1])
        elif n == 'up': aim -= int(puzzle[i+1])
    print(depth * horizontal)

aim()

