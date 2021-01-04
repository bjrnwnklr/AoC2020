import re

header = """from ply import lex, yacc
import messagelex

tokens = messagelex.tokens

"""

error_def = """
def p_error(p):
    if p:
        raise ValueError("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
"""


# f_name = 'ex1.txt'
f_name = 'input.txt'

with open(f_name, 'r') as f:
    raw_rules, _ = f.read().split('\n\n')

# process the rules and save them in a dict. Since they need to be in the same
# order as in the original input file, we need to store their position in the dict
# and then later on retrieve them in the same order to write the grammar rules
rules = dict()
for i, rule in enumerate(raw_rules.split('\n')):
    rule_num, subrules = rule.split(':')
    rules[int(rule_num)] = (i, subrules.strip().strip('\"'))

with open('messageparser.py', 'w') as f:
    # write header
    f.write(header)

    # write rules
    for rule in sorted(rules, key=lambda x: rules[x][0]):
        _, subrules = rules[rule]
        f.write(f'\ndef p_r{rule}(p):\n')
        # handle a and b values
        if subrules in 'ab':
            subrules_text = subrules.upper()
        elif '|' in subrules:
            subrules_text = re.sub(r'\s\|\s', '\n        | ', subrules)
        else:
            subrules_text = subrules

        f.write('    ' + r'"""' + str(rule) + ' : ' + subrules_text + r'"""')
        f.write('\n    pass\n\n')

    f.write(error_def)
