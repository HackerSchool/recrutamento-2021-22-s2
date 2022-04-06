from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def check_syntax(line, operator, i):
    if i == 0 and not(operator == "("):
        return False
    elif i == (len(line)-1) and not(operator == ")"):
        return False

    if operator == "+" or operator == "/" or operator == "-" or operator == "%":
        if (line[i-1].isnumeric() and line[i+1].isnumeric())\
                or (line[i-1] == ")" and line[i+1].isnumeric())\
                or (line[i-1].isnumeric() and line[i+1] == "("):
            return True
        else:
            return False
    elif operator == "*":
        if (line[i - 1].isnumeric() and line[i + 1].isnumeric())\
                or (line[i - 1] == ")" and line[i + 1].isnumeric())\
                or (line[i - 1].isnumeric() and line[i + 1] == "("):
            return True
        else:
            if (i >= 1) and i <= (len(line)-2):
                if line[i-1] == "*" and (line[i+1].isnumeric() or line[i+1] == "("):
                    return True
                elif line[i + 1] == "*" and (line[i+2].isnumeric() or line[i+2] == "("):
                    return True
                elif line[i-1] == "*" and line[i+1] == "(":
                    return True
                elif line[i + 1] == "*" and line[i+2].isnumeric():
                    return True
                else:
                    return False
            else:
                return False
    elif operator == "(":
        if i == 0 and (line[i + 1].isnumeric() or line[i + 1] == "("):
            return True
        elif (line[i + 1].isnumeric() or line[i + 1] == "(") and (not(line[i - 1].isnumeric()) and line[i - 1] != ")"):
            return True
        else:
            return False
    elif operator == ")":
        if i == (len(line)-1) and (line[i - 1].isnumeric() or line[i - 1] == ")"):
            return True
        if not(line[i - 1].isnumeric()) or line[i + 1].isnumeric():
            if line[i - 1] == ")" and not(line[i + 1].isnumeric()):
                return True
            else:
                return False
        else:
            return True


def parenthesis_pair_check_1(line, i): #(
    for j in range(i, len(line)):
        if line[j] == ")":
            return True
    return False


def parenthesis_pair_check_2(line, i): #)
    for j in range(0, i):
        if line[j] == "(":
            return True
    return False


def number_parenthesis(line):
    count_open = 0
    count_close = 0
    for i in range(0, len(line)):
        if line[i] == ")":
            count_close += 1
        elif line[i] == "(":
            count_open += 1
    if count_close == count_open:
        return True
    return False


def check_parenthesis(line):
    if number_parenthesis(line):
        for i in range(0, len(line)):
            if line[i] == "(":
                if parenthesis_pair_check_1(line, i):
                    continue
                else:
                    return False
            elif line[i] == ")":
                if parenthesis_pair_check_2(line, i):
                    continue
                else:
                    return False
        return True
    else:
        return False


def valid_character(char):
    if char.isdigit() or (char == "+" or char == "-" or char == "*"\
            or char == "/" or char == "%" or char == "(" or char == ")"):
        return True
    else:
        return False


def valid_input(line):
    for i in range(0, len(line)):
        if valid_character(line[i]):
            continue
        else:
            return False
    if not check_parenthesis(line):
        return False
    for i in range(0, len(line)):
        if not line[i].isnumeric():
            if check_syntax(line, line[i], i):
                continue
            else:
                return False
        else:
            continue
    return True


def simple_calculator():
    while True:
        print('''Simple Calculator (eval) - Available Operations:\n
            "+" -> addition,\
            "-" -> subtraction,\
            "*" -> multiplication,\
            "/" -> division,\n
            \t\t"**" -> exponentiation,\
            \t\t"%" -> modulus/remainder\n
                ''')
        print("QUIT - 0\n")
        eq = input()
        if eq == "0":
            clear()
            return
        elif valid_input(eq):
            clear()
            result = eval(eq)
            print("Result:")
            print(result)
            print("-------")
        else:
            print("Expression could not be evaluated...")
        eq = input()
        clear()

if __name__ == "__main__":
    simple_calculator()