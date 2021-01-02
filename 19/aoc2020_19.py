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
        rule_contains[rule_num].append([letter])
        # final_rules[rule_num] = letter
    elif '|' not in subrules:
        int_rules = [int(x) for x in subrules.split()]
        rule_contains[rule_num].append(int_rules)
        for i in int_rules:
            rule_included_in[i].add(rule_num)
    elif '|' in subrules:
        or_rules = subrules.split(' | ')
        for or_rule in or_rules:
            int_rules = [int(x) for x in or_rule.split()]
            rule_contains[rule_num].append(int_rules)
            for i in int_rules:
                rule_included_in[i].add(rule_num)

print_state()

# process all finalized (atomic) rules across all rules they are contained in
while atomic_rules:
    # get the first atomic rule to process
    atomic_r = atomic_rules.pop(0)
    # add to the final rules
    rule_to_finalize = rule_contains[atomic_r]
    final_rule = ''
    for sr in rule_to_finalize:
        final_rule += ''.join(c for c in sr)
        final_rule += '|'
    # strip off the last |
    final_rule = final_rule.rstrip('|')
    # and finally add to the final completed rule
    final_rules[atomic_r] = final_rule

    # now find all rules the atomic rule is included in and replace it with the final rule
    for rules_to_modify in rule_included_in[atomic_r]:
        new_rules = []
        for rule_to_modify in rule_contains[rules_to_modify]:
            mod_rule = [final_rules[atomic_r] if x == atomic_r else x for x in rule_to_modify]
            new_rules.append(mod_rule)
        rule_contains[rules_to_modify] = new_rules


print_state()

