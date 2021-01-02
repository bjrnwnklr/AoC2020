import re
from collections import defaultdict


def print_state():
    print('Atomic rules:')
    print(atomic_rules)
    print('Final rules:')
    print(final_rules)
    print('Rule included in:')
    print(rule_included_in)
    print('Rule contains:')
    print(rule_contains)


f_name = 'ex1.txt'
# f_name = 'input.txt'


with open(f_name, 'r') as f:
    rules, messages = f.read().split('\n\n')

atomic_rules = []
rule_included_in = defaultdict(set)
rule_contains = defaultdict(list)
final_rules = defaultdict(str)

for rule in rules.split('\n'):
    rule_num, subrules = rule.split(':')
    rule_num = int(rule_num)
    subrules = subrules.strip()

    # process subrules
    # first find the starting rules
    if 'a' in subrules or 'b' in subrules:
        letter = subrules.strip('\"')
        atomic_rules.append(rule_num)
        final_rules[rule_num] = letter


print_state()

# process all finalized (atomic) rules across all rules they are contained in
while atomic_rules:
    # get the first atomic rule to process
    atomic_r = atomic_rules.pop(0)

    ### We need to consider:
    # - the expressions separated with | need to be nested e.g.
    # (aa | bb) (ab | ba) | (ab | ba) (aa | bb)