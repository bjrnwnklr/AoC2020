from collections import defaultdict


def get_tile_checksum(t):
    checksum = []
    # orig, upper (1-0)
    checksum.append(int(''.join([str(x) for x in t[0]]), 2))
    # orig, right (2-1)
    checksum.append(int(''.join([str(row[-1]) for row in t]), 2))
    # orig, bottom (3-2)
    checksum.append(int(''.join([str(x) for x in t[-1][::-1]]), 2))
    # orig, left (0-3)
    checksum.append(int(''.join([str(row[0]) for row in t[::-1]]), 2))

    # horiz flipped, upper (2-3)
    checksum.append(int(''.join([str(x) for x in t[-1]]), 2))
    # horiz flipped, right (1-2)
    checksum.append(int(''.join([str(row[-1]) for row in t[::-1]]), 2))
    # horiz flipped, bottom (0-1)
    checksum.append(int(''.join([str(x) for x in t[0][::-1]]), 2))
    # horiz flipped, left (3-0)
    checksum.append(int(''.join([str(row[0]) for row in t]), 2))

    checksum_matching = [checksum[i] for i in [6, 5, 4, 7, 2, 1, 0, 3]]

    return checksum, checksum_matching


# f_name = 'ex1.txt'
f_name = 'input.txt'

tile_dict = dict()

with open(f_name, 'r') as f:
    raw_tiles = f.read().strip().split('\n\n')

    for rt in raw_tiles:
        lines = rt.split('\n')
        tile_id = int(lines[0][4:9])
        tile = []
        for line in lines[1:]:
            tile.append([1 if x == '#' else 0 for x in line.strip()])

        tile_dict[tile_id] = tile

# generate two dictionaries:
# - per tile: checksum per side
# - per tile: matching checksum per side

checksum_per_side = defaultdict(list)
matching_checksums = dict()
sides_per_checksum = defaultdict(list)
for tile in tile_dict:
    checksum, checksum_matching = get_tile_checksum(tile_dict[tile])
    checksum_per_side[tile] = checksum
    for m, c in zip(checksum_matching, checksum):
        matching_checksums[m] = c

    for side, c in enumerate(checksum_per_side[tile]):
        sides_per_checksum[c].append((tile, side))

for t, c in checksum_per_side.items():
    print(f'{t}: {c}')

for m, c in matching_checksums.items():
    print(f'{m}: {c}')

for c in sides_per_checksum:
    print(f'{c}: {sides_per_checksum[c]}')

# generate a dict that lists for each side the matching sides
matching_sides = defaultdict(set)
for c in sides_per_checksum:
    for tile, side in sides_per_checksum[c]:
        m = matching_checksums[c]
        # find all sides that have a matching checksum but not the same as our current tile
        matches = [x for x in sides_per_checksum[m] if tile != x[0]]
        for x in matches:
            matching_sides[(tile, side)].add(x)

for t, s in sorted(matching_sides):
    print(f'({t}, {s}): {matching_sides[(t, s)]}')

# find number of unique tiles each tile is matching
unique_tile_matches = defaultdict(set)
for tile, side in matching_sides:
    tiles = matching_sides[(tile, side)]
    for t, _ in tiles:
        unique_tile_matches[tile].add(t)

for t in unique_tile_matches:
    print(f'({t}): {unique_tile_matches[t]}')

# print all tiles that have 2 matches (potential corners):
part1 = 1
for x in [t for t in unique_tile_matches if len(unique_tile_matches[t]) == 2]:
    print(x)
    part1 *= x

print(f'Part 1: {part1}')

# Part 1: 13224049461431
