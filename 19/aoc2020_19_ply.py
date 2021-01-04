import re
from ply import lex, yacc

# --------- LEX definition ---------

# first definitions of the tokens for lex:
tokens = (
    'A',
    'B'
)

# Regular expression rules for simple tokens
t_A = r'a'
t_B = r'b'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# to ignore spaces or tabs
t_ignore = ' \t'


# error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# ------------ YACC configuration ------------


def p_r0(p):
    """0 : 4 1 5"""
    pass


def p_r1(p):
    """1 : 2 3
         | 3 2"""
    pass


def p_r2(p):
    """2 : 4 4
         | 5 5"""
    pass


def p_r3(p):
    """3 : 4 5
         | 5 4"""
    pass


def p_r4(p):
    """4 : A"""
    pass


def p_r5(p):
    """5 : B"""
    pass


def p_error(p):
    if p:
        raise ValueError("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


f_name = 'ex1.txt'
# f_name = 'input.txt'

with open(f_name, 'r') as f:
    raw_rules, raw_messages = f.read().split('\n\n')

# process the messages and store in a list
messages = [x.strip() for x in raw_messages.strip().split('\n')]

# build the lexer
lexer = lex.lex()
parser = yacc.yacc()
valid_count = 0
for m in messages:
    try:
        result = parser.parse(m)
        valid_count += 1
        print(f'Valid syntax: {m}')
    except ValueError:
        print(f'Incorrect syntax: {m}')


print(f'Valid messages: {valid_count}')
# Part 1: 168
