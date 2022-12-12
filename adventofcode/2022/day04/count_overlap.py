def read_input(file):

    with open(file, 'r') as f:
        lines = f.readlines()

    pairs = []
    for line in lines:
        elves = line.split(',')

        elf1 = [i for i in range(int(elves[0].split('-')[0]), int(elves[0].split('-')[1])+1)]
        elf2 = [i for i in range(int(elves[1].split('-')[0]), int(elves[1].split('-')[1])+1)]

        pairs.append([elf1,elf2])



    return pairs


def is_full_overlap(elf1, elf2):

    long = elf1 if len(elf1)>=len(elf2) else elf2
    short = elf1 if len(elf1)<len(elf2) else elf2

    return all([x in long for x in short])


def is_partial_overlap(elf1, elf2):
    long = elf1 if len(elf1)>=len(elf2) else elf2
    short = elf1 if len(elf1)<len(elf2) else elf2

    return any([x in long for x in short])


pairs = read_input('input.dat')

full_overlap = 0
partial_overlap = 0
for pair in pairs:
    if is_full_overlap(pair[0], pair[1]):
        full_overlap += 1
        partial_overlap += 1
    elif is_partial_overlap(pair[0], pair[1]):
        partial_overlap += 1


print(f'Full overlap in {full_overlap} pairs, and partial overlap in {partial_overlap} pairs of a total of {len(pairs)} pairs')