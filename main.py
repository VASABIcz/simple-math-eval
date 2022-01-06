import string

NUMBERS = string.digits
BRACKETS = ('(', ')')
OPERATORS = ('+', '-', '/', '*')
LOW = ('+', '-')
HIGH = ('*', '/')

exp = "5*((2-3)*2)+10"

# TODO add support for negative values
# TODO add support for power of
# TODO rewrite it in rust


def parse_int(exp: str) -> int:
    buf = ""

    print("parsing", exp)
    for n, char in enumerate(exp):
        if char in string.digits:
            buf += char
        else:
            if buf != "":
                return int(buf)
            else:
                raise ValueError

    return int(buf)


def evaluate_exp(a: int or float, b: int or float, c: str) -> float or int:
    print(f"evaluating {a} {c} {b}")
    match c:
        case "*":
            return a * b
        case "/":
            return a / b
        case "+":
            return a + b
        case "-":
            return a - b


def better_bracket(exp: str) -> (int, int):
    openn = None
    ignore = 0

    for n, c in enumerate(exp):
        if c == '(':
            if openn is None:
                openn = n
            else:
                ignore += 1
        elif c == ')':
            if ignore == 0:
                closee = n
                return openn, closee
            else:
                ignore -= 1
    else:
        raise ValueError


def find_lowest_val(exp: str) -> None or int:
    copy = exp
    first_high = None

    while '(' in copy:
        op, clo = better_bracket(copy)
        for x in range(op, clo):
            copy = copy[:op] + "x" * ((clo + 1) - op) + copy[clo + 1:]

    for n, c in enumerate(copy):
        if c in LOW:
            return n
        elif c in HIGH:
            if first_high is None:
                first_high = n

    if first_high is not None:
        return first_high

    return None


def is_int(exp):
    for c in exp:
        if c not in NUMBERS:
            return False

    return True


def calculate(exp: str) -> int:
    left = None
    right = None
    operator = None

    print("context", exp)
    x = find_lowest_val(exp)
    if x is None and exp[0] == '(':
        bs, be = better_bracket(exp)
        left = calculate(exp[bs + 1:be])
    else:
        operator = exp[x]
        left_ = exp[:x]
        if is_int(left_):
            left = parse_int(left_)
        else:
            left = calculate(left_)
        right_ = exp[x + 1:]
        if is_int(right_):
            right = parse_int(right_)
        else:
            right = calculate(right_)

    if right is None:
        return left
    else:
        return evaluate_exp(left, right, operator)