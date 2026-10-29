# stack
#


stack = list

# def Reverse_Stack(stack1: stack) -> stack:
#     res = stack()

#     def _reverse():
#         if not stack1: return
#         top = stack1.pop()
#         res.append(top)

#         _reverse()

#     _reverse()
#     return res


def Reverse_Stack(s1: stack):
    # reverse the stack using another stack
    tmp = stack()

    while s1:
        top = s1.pop()
        while tmp and tmp[-1] < top: s1.append(tmp.pop())
        tmp.append(top)

    while tmp: s1.append(tmp.pop())


def Valid_Expression(string: str) -> bool:
    string_, s1, mapping = list(string), stack(), {'}':'{', ')':'(', ']':'['}
    for char in string_:
        if char in mapping.values(): s1.append(char)
        else:
            if s1[-1] != mapping[char]: return False
            s1.pop()
    return True


def Eval_Postfix_Expression(expr: list[str]) -> int:
    s1 = stack()

    for atom in expr:
        if atom.isnumeric(): s1.append(int(atom))
        else:
            right, left = s1.pop(), s1.pop()
            match atom:
                case "*" | "+" | "-": s1.append(eval(f"{left} {atom} {right}"))
                case "/": s1.append(left // right)
                case "^": s1.append(left ** right)

    return int(s1.pop())


def Evaluate_Infix(expr: list[str]) -> int:
    numbers, ops, precedence = stack(), stack(), { "+": 0, "-": 0, "*": 1, "/": 1, "^": 2 }

    for atom in expr:
        if atom.isnumeric(): numbers.append(int(atom))
        else:
            while ops and ( (precedence[ops[-1]] > precedence[atom]) or (precedence[ops[-1]] == precedence[atom] and atom != "^") ):
                right, op, left = numbers.pop(), ops.pop(), numbers.pop()
                match op:
                    case "*" | "+" | "-": numbers.append(eval(f"{left} {op} {right}"))
                    case "/": numbers.append(left // right)
                    case "^": numbers.append(left ** right)
            ops.append(atom)

    while ops:
        right, op, left = numbers.pop(), ops.pop(), numbers.pop()
        match op:
            case "*" | "+" | "-": numbers.append(eval(f"{left} {op} {right}"))
            case "/": numbers.append(left // right)
            case "^": numbers.append(left ** right)

    return numbers[-1]


def Check_Redundant_Brackets(string: str) -> bool:
    s1 = stack()

    for char in string:
        if char == ')':
            top = s1.pop()

            redun = True
            while top != '(':
                if top in "+-*/^": redun = False
                top = s1.pop()

            if redun: return True
        else: s1.append(char)

    return False

def Longest_Valid_Paren_Substring(string: str) -> int:
    s1, max_len = stack([-1]), 0

    for i in range(len(string)):
        if string[i] == '(': s1.append(i)
        else:
            s1.pop()
            if not s1: s1.append(i)
            else: max_len = max(max_len, i - s1[-1])

    return max_len
