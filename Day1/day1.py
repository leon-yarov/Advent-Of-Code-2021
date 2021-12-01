from functools import reduce
with open('input1.txt') as f:
    input1 = f.read().split()


def increases(lines):
    first,count = lines[0],0
    for line in lines:
        if int(first) < int(line):
            # print(first,line)
            count += 1
        first = line
    return count


# print(increases(input1))

# print(input1)
def tag_inreases(input1):
    total,new_depth = 0,[]
    for i,n in enumerate(input1):
         total = sum(map(int,input1[i:i+3]))
         new_depth.append(total)
    return increases(new_depth)

print(tag_inreases(input1))
