class Tile:
    def __init__(self, pos, color=0):
        # color: 0=white, 1=black
        self.pos = pos
        self.color = color

    def __repr__(self):
        return f'Tile({self.pos}, {self.color})'

    def flip(self):
        self.color = (self.color + 1) % 2


class Floor:
    # hex coordinations using cube system (https://www.redblobgames.com/grids/hexagons/)
    # - each coordinate is (x, y, z)
    # - x + y + z = 0
    # - e: (-1, 1, 0)
    # - nw: (1, 0, -1)
    directions = {
        'e': (-1, 1, 0),
        'se': (-1, 0, 1),
        'sw': (0, -1, 1),
        'w': (1, -1, 0),
        'nw': (1, 0, -1),
        'ne': (0, 1, -1)
    }

    def __init__(self):
        self.tiles = dict()

    def __repr__(self):
        return f'Floor({len(self.tiles)})'

    def flip_tile(self, path):
        tokens = self._tokenize(path)
        pos = (0, 0, 0)
        for step in tokens:
            delta = self.directions[step]
            pos = tuple(pos[i] + delta[i] for i in range(3))

        if pos not in self.tiles:
            self.tiles[pos] = Tile(pos)
        self.tiles[pos].flip()

    def _tokenize(self, path):
        raw = list(path)
        tokens = []
        current_token = ''
        while raw:
            current_token += raw.pop(0)
            if current_token in self.directions:
                tokens.append(current_token)
                current_token = ''
        return tokens

    def get_black_tiles(self):
        return sum(t.color for t in self.tiles.values())

    # Part 2 methods
    def _grid_dimensions(self):
        # determine the current dimensions of the grid so we can review all tiles within the grid
        mins = [min(self.tiles, key=lambda x: x[i])[i] for i in range(3)]
        maxs = [max(self.tiles, key=lambda x: x[i])[i] for i in range(3)]
        return mins, maxs

    def _neighbor_black_tiles(self, pos):
        count = 0
        for neighbor in self.directions.values():
            n_pos = tuple(pos[i] + neighbor[i] for i in range(3))
            if n_pos in self.tiles and self.tiles[n_pos].color == 1:
                count += 1
        return count

    def flip_all(self):
        flip_queue = []
        mins, maxs = self._grid_dimensions()
        for x in range(mins[0] - 1, maxs[0] + 2):
            for y in range(mins[1] - 1, maxs[1] + 2):
                for z in range(mins[2] - 1, maxs[2] + 2):
                    pos = (x, y, z)
                    black_tiles = self._neighbor_black_tiles(pos)
                    if pos in self.tiles:
                        if self.tiles[pos].color == 1:
                            if black_tiles == 0 or black_tiles > 2:
                                flip_queue.append(pos)
                        else:
                            if black_tiles == 2:
                                flip_queue.append(pos)
                    else:
                        if black_tiles == 2:
                            self.tiles[pos] = Tile(pos)
                            flip_queue.append(pos)
        for t in flip_queue:
            self.tiles[t].flip()


if __name__ == '__main__':
    # f_name = 'ex1.txt'
    f_name = 'input.txt'

    floor = Floor()

    with open(f_name, 'r') as f:
        for line in f.readlines():
            floor.flip_tile(line.strip())

    # Part 1
    part1 = floor.get_black_tiles()
    print(f'Part 1: {part1}')

    # Part 2 - game of life (again...)
    for day in range(1, 101):
        floor.flip_all()
        print(f'Day {day}: {floor.get_black_tiles()}')

# part 1: 269
# Part 2: 3667
