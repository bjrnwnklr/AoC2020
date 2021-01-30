from collections import deque

f_name = 'ex1.txt'
# f_name = 'input.txt'


with open(f_name, 'r') as f:
    cups_initial = [int(x) for x in list(f.read().strip())]

max_initial_cup = max(cups_initial) # should be 9
max_card_value = 1_000_000
cups = deque(cups_initial + list(range(max_initial_cup + 1, max_card_value + 1)))
print(max_initial_cup, len(cups))


n = 10_000_000
cycles = 1
while cycles <= n:
    if cycles % 1_000 == 0:
        print(f'Cycle {cycles}')
    # print(f'-- move {cycles} --')
    # print(f'cups: {cups}')
    # pick up the three cups clockwise by rotating to the left and then popping off 3 items
    # then rotating back to the current cup
    cups.rotate(-1)
    held_cups = [cups.popleft() for _ in range(3)]
    cups.rotate(1)

    # print(f'pick up: {held_cups}')

    # select the destination cup
    def get_dest_cup(n):
        return (n - 2) % max_card_value + 1

    dest_cup = get_dest_cup(cups[0])
    while dest_cup not in cups:
        dest_cup = get_dest_cup(dest_cup)

    # print(f'destination: {dest_cup}')

    # place the cup clockwise to the destination cup by rotating to the destination cup, inserting
    # and then rotating back the same amount as the destination cup index plus 3 (the length of the inserted cups)
    # On the first rotate, we need to rotate by one additional step to move the destination cup to
    # the right end of the deque
    # On the second rotate, we will end up with the new current cup as the first element of the deque
    dest_cup_index = cups.index(dest_cup)
    cups.rotate(-dest_cup_index - 1)
    cups.extend(held_cups)
    cups.rotate(dest_cup_index + len(held_cups))

    # increase cycles
    cycles += 1

print('-- final --')
# print(cups)

# get the part 1 solution string starting from cup labeled 1, but excluding the 1.
one_idx = cups.index(1)
cups.rotate(-one_idx)
n1 = cups[1]
n2 = cups[2]
part2 = n1 * n2
print(f'Part 2: {part2} = {n1} * {n2}')

# part 1: 34952786
