with open('input.txt') as f:
    puzzle_input = f.read().split()


def rotate_list(puzzle):
    puzzle = list(zip(*puzzle[::-1]))
    puzzle = [list(i) for i in puzzle]
    return puzzle

def count_bits(puzzle):
    gamma,epsilon = '',''
    puzzle = rotate_list(puzzle)
    for n in puzzle:
        zero,one = n.count('1'),n.count('0')
        if zero > one: gamma,epsilon = gamma + '1', epsilon + '0'
        else: gamma,epsilon = gamma + '0', epsilon + '1'
    return int(gamma,2),int(epsilon,2)

def get_column(puzzle,n):
    return [i[n] for i in puzzle]

def discard_bits(puzzle,bit,n = 0):
    zero,one = get_column(puzzle,n).count('0'),get_column(puzzle,n).count('1')
    if bit == '1':
        if one >= zero:
            puzzle = list(filter(lambda x: x[n] == '1', puzzle))
        else:
            puzzle = list(filter(lambda x: x[n] == '0', puzzle))
    else:
        if one >= zero:
            puzzle = list(filter(lambda x: x[n] == '0', puzzle))
        else:
            puzzle = list(filter(lambda x: x[n] == '1', puzzle))

    if len(puzzle) <= 1: return puzzle[0]
    if n == len(puzzle[0])-1: return discard_bits(puzzle,bit,0)
    if len(puzzle) > 1: return discard_bits(puzzle,bit,n + 1)

# ans = count_bits(puzzle_input)
# print(ans[0] * ans[1])

oxy = discard_bits(puzzle_input,'1')
co2 = discard_bits(puzzle_input,'0')
print(int(oxy,2) * int(co2,2))
