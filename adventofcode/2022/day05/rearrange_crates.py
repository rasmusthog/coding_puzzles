def read_input(file):

    with open(file, 'r') as f:
        lines = f.readlines()


    rows = []

    # Get the initial crate configuration in separate lists
    for i, line in enumerate(lines):
        if line.strip():
            rows.append(line)
        else:
            stop = i
            break

    columns = len(rows[-1].split())

    crates = [[] for i in range(columns)]

    for row in reversed(rows[:-1]):
        for i in range(columns):
            crate = row[(3*i)+i:3*(i+1)+i]
            if crate.split():
                crates[i].append(crate)

    

    moves = []
    for i, line in enumerate(lines):
        if i <= stop:
            continue
        else:
            moves.append(line.split())



    return crates, moves

def move_crates(crates: list, number: int, origin: int, destination: int, crane='cratemover9000') -> list:

    if crane == 'cratemover9000':

        for i in range(number):
            crate = crates[origin-1].pop()
            crates[destination-1].append(crate)

    elif crane == 'cratemover9001':

        crate = crates[origin-1][-number:]
        
        if number < len(crates[origin-1]):
            del crates[origin-1][-number:]
        else:
            crates[origin-1] = []

        for c in crate:
            crates[destination-1].append(c)


    return crates


crates, moves = read_input('input.dat')

for move in moves:
    crates = move_crates(crates=crates, number=int(move[1]), origin=int(move[3]), destination=int(move[5]))



message = []
for crate in crates:
    message.append(crate[-1][1:2])

message = ''.join(message)
print('The secret message with CrateMover 9000 is: ', message)



## PART 2
crates, moves = read_input('input.dat')
for move in moves:
    crate = move_crates(crates=crates, number=int(move[1]), origin=int(move[3]), destination=int(move[5]), crane='cratemover9001')


message = []
for crate in crates:
    message.append(crate[-1][1:2])

message = ''.join(message)
print('The secret message with CrateMover 9001 is: ', message)