def make_plain() -> str:
    return get_text()


def make_bold() -> str:
    return "**" + get_text() + "**"


def make_italic() -> str:
    return "*" + get_text() + "*"


def get_text() -> str:
    return input("Text: ")


class InvalidHeaderRange(Exception):
    pass


def make_header() -> str:
    while True:
        n = input("Level: ")
        try:
            n = int(n)
            if n < 1 or n > 6:
                raise InvalidHeaderRange
        except (ValueError, InvalidHeaderRange):
            print("The level should be within the range of 1 to 6")
            continue
        break
    return f'{"#" * n} {get_text()}\n'


def make_link() -> str:
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def make_inline_code() -> str:
    return "`" + get_text() + "`"


def make_new_line() -> str:
    return "\n"


def print_help() -> None:
    msg = (
        f'Available formatters: {" ".join(list(formatters))}'
        f'Special commands: !help !done'
    )
    print(msg)


formatters = {
    "plain": make_plain,
    "bold": make_bold,
    "italic": make_italic,
    "header": make_header,
    "link": make_link,
    "inline-code": make_inline_code,
    "new-line": make_new_line,
}

texts = ""
while True:
    f = input("Choose a formatter: ")
    if f == "!help":
        print_help()
        continue
    if f == "!done":
        exit()
    formatter = formatters.get(f)
    if formatter is None:
        print("Unknown formatting type or command")
        continue
    text = formatter()
    texts += text
    print(texts)
