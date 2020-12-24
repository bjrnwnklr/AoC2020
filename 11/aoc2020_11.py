# f_name = 'ex1.txt'
f_name = 'input.txt'

with open(f_name, 'r') as f:
    grid = [[x for x in line.strip('\n')] for line in f.readlines()]

# save a copy of the grid, we'll probably need it later
orig_grid = grid[:]

# dimensions of the grid
WIDTH = len(grid[0])
HEIGHT = len(grid)


def get_neighbors(r, c):
    """
    Find the neighbors of a grid cell and return a list of neighboring seat coordinates
    in (r, c) tuples. Floor cells are ignored.
    :param r: row number of the seat to check
    :param c: column number of the seat to check
    :return: list of (r, c) tuples of seats neighboring the given seat.
    """
    # i = rows, j = columns
    neighbors = []
    for i in [-1, 0, 1]:
        temp_r = r + i
        if 0 <= temp_r <= HEIGHT:
            for j in [-1, 0, 1]:
                temp_c = c + j
                if (0 <= temp_c <= WIDTH
                        and (temp_c != 0 and temp_r != 0)
                        and grid[temp_r][temp_c] in ['L', '#']):
                    neighbors.append((temp_r, temp_c))
    return neighbors


def get_occupied_seats(r, c):
    """
    Return the count of occupied seats around the given seat.
    :param r: row number of the seat to check
    :param c: column number of the seat to check
    :return: count of occupied seats surrounding the given seat.
    """
    occ_count = 0
    for i in [-1, 0, 1]:
        temp_r = r + i
        if 0 <= temp_r < HEIGHT:
            for j in [-1, 0, 1]:
                temp_c = c + j
                if (0 <= temp_c < WIDTH
                        and ((temp_r, temp_c) != (r, c))
                        and grid[temp_r][temp_c] == '#'):
                    occ_count += 1
    return occ_count


def print_grid(grid):
    for row in grid:
        print(''.join(x for x in row))


changed = True
cycles = 0
while changed:
    # iterate through each seat and generate a new state map
    temp_state = []
    changed = False
    for r in range(0, HEIGHT):
        temp_row = []
        for c in range(0, WIDTH):
            curr_val = grid[r][c]
            if curr_val == 'L':
                # check empty seat rule
                if get_occupied_seats(r, c) == 0:
                    curr_val = '#'
                    changed = True
            elif curr_val == '#':
                # check occupied seat rule
                if get_occupied_seats(r, c) >= 4:
                    curr_val = 'L'
                    changed = True
            temp_row.append(curr_val)
        temp_state.append(temp_row)

    # deep copy the temp_state grid
    grid = [[x for x in row] for row in temp_state]
    cycles += 1
    # print(f'[{cycles}]: Changed = {changed}')
    # print_grid(grid)

# we reached a stable state without any further changes
print(f'Stable state reached after {cycles} cycles.')
# count occupied seats
occ_count = sum(1 for row in grid for seat in row if seat == '#')
print(f'Counted {occ_count} occupied seats.')

# part 1: 2204 occupied seats
