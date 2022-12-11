with open('input.dat', 'r') as f:
    lines = f.readlines()

calories = []
elf_cal = 0

for line in lines:
    if line.strip():
        elf_cal += int(line)
    else:
        calories.append(elf_cal)
        elf_cal = 0


print('Max number of calories: ', max(calories))

# PART 2

calories.sort()
print('Total calories carried by top three elves: ', sum(calories[-3:]))



    