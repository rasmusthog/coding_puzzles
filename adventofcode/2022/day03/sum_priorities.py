def find_shared(line):

    rucksack1, rucksack2 = line[0:int(len(line)/2)], line[int(len(line)/2):]

    for item in rucksack1:
        if item in rucksack2:
            return item

def find_priority(shared):

    base = ord('a')-1

    priority = ord(shared)-base

    if priority <= 0:
        base = ord('A')-1
        priority = ord(shared)-base + 26

    return priority


def group_elves(file):

    groups = []
    with open(file, 'r') as f:
        
        group = []
        for line in f:
            group.append(line.strip())
            if len(group) == 3:
                groups.append(group)
                group = []


    return groups



def find_badges(groups):

    badges = []

    for group in groups:
        elves = []
        for elf in group:
            elves.append(set(elf))
        s0 = elves[0].intersection(elves[1])
        print(s0)
        s1 = s0.intersection(elves[2])
        print(s1)

        badges.append(''.join(list(s1)))


    return badges


with open('input.dat', 'r') as f:
    lines = f.readlines()


priorities = 0
for line in lines:
    priorities += find_priority(find_shared(line.strip()))

print('The sum of priorities is: ', priorities)



## PART 2

groups = group_elves('input.dat')
badges = find_badges(groups)

priorities = 0
for badge in badges:
    priorities += find_priority(badge)

print('The sum of the badges is: ', priorities)