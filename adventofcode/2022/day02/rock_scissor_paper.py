def evaluate_round(opponent, you):

    points = 0

    shape_points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    points += shape_points[you]

    winmap = {
        'A': 'Y', # Rock (A) beaten by paper (Y)
        'B': 'Z', # Paper (B) beaten by scissors (Z),
        'C': 'X' # Scissors (C) beaten by rock (X)
    }

    drawmap = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    # Assign points if you draw
    if drawmap[opponent] == you:
        points += 3

    # Assign points if you win
    elif winmap[opponent] == you:
            points += 6


    return points


## PART 2

def follow_guide(opponent, outcome):

    points = 0

    win = {
        'A': 'paper',
        'B': 'scissors',
        'C': 'rock',
    }

    draw = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
    }

    lose = {
        'A': 'scissors',
        'B': 'rock',
        'C': 'paper',
    }


    outcome_map = {
        'X': [lose, 0],
        'Y': [draw, 3],
        'Z': [win, 6]
    }

    shape_map = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }

    return shape_map[outcome_map[outcome][0][opponent]] + outcome_map[outcome][1]



with open('input.dat', 'r') as f:
    lines = f.readlines()

total_points = 0
follow_guide_points = 0

for line in lines:
    shapes = line.split()
    if shapes:
        total_points += evaluate_round(opponent=shapes[0], you=shapes[1])
        follow_guide_points += follow_guide(opponent=shapes[0], outcome=shapes[1])



print(f'You got a total of {total_points} points following your own strategy')
print(f'You got a total of {follow_guide_points} points following the guide.')

