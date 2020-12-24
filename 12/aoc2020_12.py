# f_name = 'ex1.txt'
f_name = 'input.txt'

with open(f_name, 'r') as f:
    instructions = [(line[0], int(line[1:].strip('\n'))) for line in f.readlines()]

direction_moves = {
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
    'N': (-1, 0)
}

directions = [
    'E',
    'S',
    'W',
    'N'
]

pos = (0, 0)
curr_dir = 0 # 0 = East

for action, val in instructions:
    if action in direction_moves or action == 'F':
        if action == 'F':
            move_in = direction_moves[directions[curr_dir]]
        else:
            move_in = direction_moves[action]
        pos = (pos[0] + move_in[0] * val, pos[1] + move_in[1] * val)
    else:
        # calculate turning in direction
        # L means moving backwards in directions index, R means moving forwards in direction index
        # degrees are all multiples of 90, so mean 90 = move 1 index, etc
        # use modulo to determine new direction
        i = val // 90
        sign = 1 if action == 'R' else -1
        curr_dir = (curr_dir + sign * i) % 4

print(f'Position is {pos}, facing {directions[curr_dir]}. Manhattan distance {abs(pos[0]) + abs(pos[1])}.')

# Part 1: 962

pos = (0, 0)
wp = (-1, 10)

turns = [

]

for action, val in instructions:
    if action in direction_moves:
        # move the waypoint
        move_in = direction_moves[action]
        wp = (wp[0] + move_in[0] * val, wp[1] + move_in[1] * val)
    elif action == 'F':
        pos = (pos[0] + wp[0] * val, pos[1] + wp[1] * val)
    else:
        i = val // 90
        sign = 1 if action == 'R' else -1

