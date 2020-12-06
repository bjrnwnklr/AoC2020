

f_name = 'input.txt'
# f_name = 'ex1.txt'

with open(f_name, 'r') as f:
    grid = [[c for c in row.strip('\n')] for row in f.readlines()]

# get grid dimensions to know when we have reached the bottom and when we have reached the right end
# we will wrap around using %
height = len(grid)
width = len(grid[0])

# (row, column)
pos = (0, 0)

trees = 0

while pos[0] < height-1:
    pos = (pos[0] + 1, (pos[1] + 3) % width)
    if grid[pos[0]][pos[1]] == '#':
        trees += 1

print(f'Part 1: Encountered {trees} trees.')

# Part 1: 195

