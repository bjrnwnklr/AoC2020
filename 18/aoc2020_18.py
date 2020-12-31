import re


def process_op(result, value, op):
    if op == '+':
        result += value
    elif op == '*':
        result *= value
    return result


def evaluate_expression(expression):
    stack = []
    op = '+'
    result = 0
    while expression:
        # pop off first element and decide what to do
        term = expression.pop(0)
        if term.isnumeric():
            # we found a number, so apply the last operator to the number and result
            term = int(term)
            result = process_op(result, term, op)
        elif term in ['+', '*']:
            # we found an operator. and just need to update our operator for the next number we find
            op = term
        elif term == '(':
            # we found an opening parenthesis. Push the result and last operator onto the stack and start with a new
            # term
            stack.append((result, op))
            result = 0
            op = '+'
        elif term == ')':
            # we found a closing parenthesis. Retrieve the result and operator from the stack and process the result
            value = result
            result, op = stack.pop()
            result = process_op(result, value, op)
    return result


# f_name = 'ex1.txt'
f_name = 'input.txt'


with open(f_name, 'r') as f:
    expressions = [list(re.sub(r'\s', '', l.strip('\n'))) for l in f.readlines()]

part1 = sum(evaluate_expression(e) for e in expressions)
print(f'Part 1: {part1}')

# Part 1: 86311597203806

