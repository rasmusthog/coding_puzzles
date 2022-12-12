def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    message = ''

    for line in lines:
        message = message.join(line.strip())


    return message
    
def find_marker(message, distinct=4):

    last_four = [None for i in range(distinct)]
    for i, char in enumerate(message):
        if None in last_four:
            for j, c in enumerate(last_four):
                if not c:
                    last_four[j] = char

        else:
            del last_four[0]
            last_four.append(char)

            if len(set(last_four)) == distinct:
                return i+1, ''.join(last_four)



    return None, None



message = read_input('input.dat')

pos, marker = find_marker(message)
print(f'The start-of-packet marker is "{marker}" at position {pos}')
pos, marker = find_marker(message, distinct=14)
print(f'The start-of-message marker is "{marker}" at position {pos}')

                

