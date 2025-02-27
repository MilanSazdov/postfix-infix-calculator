import re

# Author: Milan Sazdov, 24.03.2024
# Calculator for postfix & infix notation

class StackError(Exception):
    pass


class DivisionByZero(Exception):
    pass


class NotMathematicallyCorrect(Exception):
    pass


class ConsecutiveOperands(Exception):
    pass


class ConsecutiveOperations(Exception):
    pass


class IllegalCharacters(Exception):
    pass


class ComplexNumber(Exception):
    pass


class ZeroNegativePower(Exception):
    pass


class Stack:
    """
    Stack implementation using a list.
    We use an unlimited depth stack (for large mathematical expressions).
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty!!!")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty!!!")
        return self._data.pop()


def input_priority(character):
    if character == "+" or character == "-":
        return 2
    elif character == "*" or character == "/":
        return 3
    elif character == "^":
        return 6
    elif character == "(":
        return 8
    elif character == ")":
        return 1
    elif character == "_-" or character == "_+":
        return 7


def stack_priority(character):
    if character == '+' or character == '-':
        return 2
    elif character == '*' or character == '/':
        return 3
    elif character == '^':
        return 4
    elif character == '(':
        return 0
    elif character == "_-" or character == "_+":
        return 5


def is_number(string):
    try:
        float(string)  # Attempting conversion to float
        return True  # If successful, the string is a number
    except ValueError:
        return False  # Otherwise, it's not a number


def infix_to_postfix(expression):
    valid_characters = set('1234567890()+-*/^. ')

    operators_after_opening_bracket = {'*', '/', '^'}
    operators_before_closing_bracket = {'+', '-', '*', '/', '^'}

    tokens = re.findall(r'[+\-*/^()]|\d+\.\d+|\d+|\.\d+', expression)
    if ''.join(expression.split()) != ''.join(tokens):
        raise NotMathematicallyCorrect("The expression is not mathematically correct!!!")

    tokens = [token.strip() for token in tokens]

    for i in range(len(tokens) - 1):
        if tokens[i] in '+-*/^' and tokens[i + 1] in '+-*/^':
            raise ConsecutiveOperations("Two consecutive operators.")

    for i in range(len(tokens) - 1):
        if is_number(tokens[i]) and is_number(tokens[i + 1]):
            raise ConsecutiveOperands("Two consecutive operands.")

    if expression.startswith('*') or expression.startswith(
            '/') or expression.startswith('^') or expression.startswith(')'):
        raise NotMathematicallyCorrect("The expression is not mathematically valid!!!")

    if expression.endswith('+') or expression.endswith('-') or expression.endswith('*') or expression.endswith(
            '/') or expression.endswith('^') or expression.endswith('('):
        raise NotMathematicallyCorrect("The expression is not mathematically valid!!!")

    for i in range(len(tokens) - 1):
        if tokens[i] == '(' and tokens[i + 1] == ')':
            raise NotMathematicallyCorrect("The expression is not mathematically valid!!!")

    for i in range(len(tokens) - 1):
        if tokens[i] == '(' and tokens[i + 1] in operators_after_opening_bracket:
            raise NotMathematicallyCorrect(
                "An operator '* / ^' follows an opening bracket.")

    for i in range(len(tokens) - 1):
        if tokens[i] in operators_before_closing_bracket and tokens[i + 1] == ')':
            raise NotMathematicallyCorrect("An operator cannot follow a closing bracket.")

    postfix = []
    stack = Stack()
    previous_token = None

    for token in tokens:
        if is_number(token) or (token[0] == '-' and token[1:].isdigit()):
            postfix.append(float(token))  # Convert numbers to float
        else:
            if token in '+-' and (previous_token is None or previous_token == '('):
                token = '_' + token  # Mark unary operations
            while not stack.is_empty() and input_priority(token) <= stack_priority(stack.top()):
                postfix.append(stack.top())
                stack.pop()
            if token != ')':
                stack.push(token)
            else:
                if stack.is_empty():
                    raise NotMathematicallyCorrect("The expression is not mathematically valid!!!")
                stack.pop()
        previous_token = token

    while not stack.is_empty():
        postfix.append(stack.top())
        stack.pop()

    if '(' in postfix:
        raise NotMathematicallyCorrect("The expression is not mathematically valid!!!")

    return postfix


def print_postfix(postfixx):
    formatted_postfix = []
    for item in postfixx:
        if isinstance(item, float) and item.is_integer():
            formatted_postfix.append(str(int(item)))
        else:
            formatted_postfix.append(str(item))
    print(' '.join(formatted_postfix))


def calculate_postfix(token_list):

    stack = Stack()

    for i in token_list:
        if is_number(i):
            stack.push(i)
        elif i == '+':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.push(float(operand_1) + float(operand_2))
        elif i == '-':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.push(float(operand_2) - float(operand_1))
        elif i == '/':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            if float(operand_1) == 0:
                raise DivisionByZero("Division by zero is not allowed!!!")
            else:
                stack.push(float(operand_2) / float(operand_1))
        elif i == '*':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.push(float(operand_1) * float(operand_2))
        elif i == '^':
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            if float(operand_2) == 0 and float(operand_1) <= 0:
                raise ZeroNegativePower("Zero to a negative power is undefined.")
            if isinstance(float(operand_2) ** float(operand_1), complex):
                raise ComplexNumber("The expression results in a complex number!!!")
            else:
                stack.push(float(operand_2) ** float(operand_1))
        elif i == '_-':
            operand_1 = stack.pop()
            stack.push(float(operand_1) * (-1))
        else:
            raise NotMathematicallyCorrect("The expression is not mathematically correct!!!")

    if stack.__len__() > 1:
        raise NotMathematicallyCorrect("The expression is not mathematically correct!!!")
    else:
        return float(stack.top())


def calculate_infix(expression):
    postfix = infix_to_postfix(expression)
    return calculate_postfix(postfix)


if __name__ == '__main__':
    exp = input("Enter a mathematical expression: ")
    tokens = infix_to_postfix(exp)
    print(tokens)
    print(calculate_postfix(tokens))
    print(calculate_infix(exp))
