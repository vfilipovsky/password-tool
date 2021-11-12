import const as c
import string
import random
import re


def validate(password: str) -> str:
    length_error = len(password) < 8

    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

    return 'Password is strong' if password_ok else 'Password is weak'


def gen(rules: dict) -> str:
    try:
        length = int(rules[c.KEY_LENGTH])
    except ValueError:
        return 'Length can be only an integer'

    characters = list()

    if rules[c.KEY_ASCII]:
        characters += string.ascii_letters

    if rules[c.KEY_NUMBERS]:
        characters += string.digits

    if rules[c.KEY_SYMBOLS]:
        characters += string.punctuation

    password = []

    for _ in range(length):
        password.append(random.choice(characters))

    return ''.join(password)


if __name__ == '__main__':
    import sys

    try:
        passwd = sys.argv[1]
    except IndexError:
        passwd = None

    if passwd is None:
        print('Input password as argument: python password.py "h5RrGjfc*2"')
        exit(1)

    print(validate(passwd))
