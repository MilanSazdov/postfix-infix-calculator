import re


# Autor: Milan Sazdov, SV21-2023, 24.03.2024
# Kalkulator postfix & infix notacija

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


class Stack(object):
    """
    Implementacija steka na osnovu liste.
    Koristimo Stek sa neogranicenom dubinom (veliki matematicki izrazi)
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
            raise StackError("Stek je prazan !!!")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise StackError("Stek je prazan !!!")
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
        float(string)  # Pokušavamo konverziju u float
        return True  # Ako je uspešno, string je broj
    except ValueError:
        return False  # Ako ne, string nije broj


def infix_to_postfix(expression):
    valid_characters = set('1234567890()+-*/^. ')

    # expression = ''.join(char for char in expression if char in valid_characters)

   # print(expression)

    operators_after_opening_bracket = {'*', '/', '^'}
    operators_before_closing_bracket = {'+', '-', '*', '/', '^'}

    tokens = re.findall(r'[+\-*/^()]|\d+\.\d+|\d+|\.\d+', expression)
    if ''.join(expression.split()) != ''.join(tokens):
        raise NotMathematicallyCorrect("Izraz nije matematicki korektan !!!")

    tokens = [token.strip() for token in tokens]

    #print(tokens)

    #if not all(character in valid_characters for character in expression):
       # raise IllegalCharacters("Izraz sadrzi nedozvoljene karaktere.")

    for i in range(len(tokens) - 1):
        if tokens[i] in '+-*/^' and tokens[i + 1] in '+-*/^':
            raise ConsecutiveOperations("Dve operacije su uzastopne.")

    for i in range(len(tokens) - 1):
        if is_number(tokens[i]) and is_number(tokens[i + 1]):
            raise ConsecutiveOperands("Dva operanda su uzastopna. ")

    if expression.startswith('*') or expression.startswith(
            '/') or expression.startswith('^') or expression.startswith(')'):
        raise NotMathematicallyCorrect("Izraz nije matematicki ispravan !!!")

    if expression.endswith('+') or expression.endswith('-') or expression.endswith('*') or expression.endswith(
            '/') or expression.endswith('^') or expression.endswith('('):
        raise NotMathematicallyCorrect("Izraz nije matematicki ispravan !!!")

    for i in range(len(tokens) - 1):
        if tokens[i] == '(' and tokens[i + 1] == ')':
            raise NotMathematicallyCorrect("Izraz nije matematicki ispravan !!!")

   # print(tokens)

    for i in range(len(tokens) - 1):
        if tokens[i] == '(' and tokens[i + 1] in operators_after_opening_bracket:
            raise NotMathematicallyCorrect(
                "Nakon otvorene zagrade sledi operator '* / ^'.")

        # Check for invalid sequences before closing bracket
    for i in range(len(tokens) - 1):
        if tokens[i] in operators_before_closing_bracket and tokens[i + 1] == ')':
            raise NotMathematicallyCorrect("Operator ne može slediti nakon zatvorene zagrade.")

    # tokens = re.split(r'([()+\-*/^])', expression)
    # tokens = [token for token in expression.split() if token]
    # tokens = re.findall(r'[+\-*/^()]|\d+', expression)
    # tokens = [token.strip() for token in tokens if token.strip()]  # Uklanjamo prazne stringove

    # print(tokens)

    postfix = []
    stack = Stack()
    previous_token = None

    for token in tokens:
        if is_number(token) or (token[0] == '-' and token[1:].isdigit()):
            postfix.append(float(token))  # Konvertujemo brojeve u float
        else:
            if token in '+-' and (previous_token is None or previous_token == '('):
                token = '_' + token  # Oznacavamo unarne operacije
            while not stack.is_empty() and input_priority(token) <= stack_priority(stack.top()):
                postfix.append(stack.top())
                stack.pop()
            if token != ')':
                stack.push(token)
            else:
                if stack.is_empty():
                    raise NotMathematicallyCorrect("Izraz nije matematicki ispravan !!!")
                stack.pop()
        previous_token = token

    while not stack.is_empty():
        postfix.append(stack.top())
        stack.pop()

    if '(' in postfix:
        raise NotMathematicallyCorrect("Izraz nije matematicki ispravan !!!")

    return postfix


def print_postfix(postfixx):
    formatted_postfix = []
    for item in postfixx:
        if isinstance(item, float) and item.is_integer():  # Provera da li je broj celobrojni float
            formatted_postfix.append(str(int(item)))  # Konverzija u int i pretvaranje u string
        else:
            formatted_postfix.append(str(item))  # Ostali elementi ostaju nepromenjeni
    print(' '.join(formatted_postfix))  # Spajanje elemenata u jedan string i ispisivanje


def calculate_postfix(token_list):

    stack = Stack()

    for i in token_list:
        if is_number(i):
            stack.push(i)  # na stek stavljamo operand
        elif i == '+':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()

            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_2 = stack.pop()

            stack.push(float(operand_1) + float(operand_2))
        elif i == '-':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_2 = stack.pop()
            stack.push(float(operand_2) - float(operand_1))
        elif i == '/':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_2 = stack.pop()
            if float(operand_1) == 0:
                raise DivisionByZero("Deljenje sa 0 nije dozvoljeno !!!")
            else:
                stack.push(float(operand_2) / float(operand_1))
        elif i == '*':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_2 = stack.pop()
            stack.push(float(operand_1) * float(operand_2))
        elif i == '^':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_2 = stack.pop()

            if float(operand_2) == 0 and float(operand_1) <= 0:
                raise ZeroNegativePower("Nula na negativan stepen ili nulu. Izraz nije definisan. ")

            if isinstance(float(operand_2) ** float(operand_1), complex):
                raise ComplexNumber("U izrazu se dobija kompleksan broj !!!")
            else:
                stack.push(float(operand_2) ** float(operand_1))
        elif i == '_-':
            if stack.is_empty():
                raise NotMathematicallyCorrect("Nema dovoljno operanada da se izvrsi operacija !!!")
            operand_1 = stack.pop()
            stack.push(float(operand_1) * (-1))
        else:
            raise NotMathematicallyCorrect("Izraz nije matematicki korektan (sadrzi neodgovarajuce karaktere) !!!")

    if stack.__len__() > 1:
        raise NotMathematicallyCorrect("Izraz nije matematicki korektan !!!")
    else:
        return float(stack.top())


def calculate_infix(expression):
    postfix = infix_to_postfix(expression)
    return calculate_postfix(postfix)


def menu():
    while True:
        print("Unesite 1. za prebacivanje iz INFIX -> POSTFIX ")
        print("Unesite 2. za izracunavanje INFIX izraza ")
        print("Unesite 0. za EXIT ")
        option = input("Unesite opciju iz menija: ")
        if option == '1':
            inf = input("Unesite matematicki INFIX izraz: ")
            postfix = infix_to_postfix(inf)
            print_postfix(postfix)

            print("Unesite 2. za racunanje POSTFIX izraza: (0. za exit) ")
            option_2 = input()

            if option_2 == '2':
                print("Resenje izraza je: ")
                print(calculate_postfix(postfix))
                continue
            elif option_2 == '0':
                continue
            else:
                print("Uneliste neogovarajucu opciju !!!")
                continue

        elif option == '2':
            inf = input("Unesite matematicki INFIX izraz: ")
            postfix = infix_to_postfix(inf)
            print("Resenje izraza je: ")
            print(calculate_postfix(postfix))
            continue
        elif option == '0':
            exit(0)
        else:
            print("Uneliste neogovarajucu opciju !!!")
            continue


# stack = Stack()
if __name__ == '__main__':
    exp = input("Unesite matematicki izraz: ")
    tokens = infix_to_postfix(exp)
    print(tokens)
    print(calculate_postfix(tokens))
    print(calculate_infix(exp))
