def division_by_twelve(num: int) -> bool:
    try:
        if int(num) % 12 == 0:
            return True
        else:
            return False
    except ValueError:
        return False


def make_capital_letters(inp: str) -> str:
    inp = inp.upper()
    return inp


def min_of_three_vars(a, b, c):
    if b > a < c:
        return a
    elif a > b < c:
        return b
    else:
        return c
