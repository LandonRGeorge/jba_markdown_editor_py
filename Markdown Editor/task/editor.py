def make_plain() -> str:
    return get_text()


def make_bold() -> str:
    return "**" + get_text() + "**"


def make_italic() -> str:
    return "*" + get_text() + "*"


def get_text() -> str:
    return input("Text: ")


def make_header() -> str:
    while True:
        n = input("Level: ")
        try:
            n = int(n)
            assert n >= 1 or n <= 6
        except (ValueError, AssertionError):
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


def get_list(ordered=False) -> str:
    while True:
        nbr_rows = input("Number of rows: ")
        try:
            nbr_rows = int(nbr_rows)
            assert nbr_rows > 0
        except (ValueError, AssertionError):
            print("The number of rows should be greater than zero")
            continue
        break
    rows = []
    for i in range(1, nbr_rows + 1):
        row = input(f"Row #{i}: ")
        if ordered:
            row = f"{i}. {row}"
        else:
            row = f"* {row}"
        rows.append(row)
    return "\n".join(rows) + "\n"


def make_ordered_list() -> str:
    return get_list(ordered=True)


def make_unordered_list() -> str:
    return get_list(ordered=False)


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
    "ordered-list": make_ordered_list,
    "unordered-list": make_unordered_list,
}

texts = ""
while True:
    f = input("Choose a formatter: ")
    if f == "!help":
        print_help()
        continue
    if f == "!done":
        with open("output.md", "w") as file:
            file.write(texts)
        exit()
    formatter = formatters.get(f)
    if formatter is None:
        print("Unknown formatting type or command")
        continue
    text = formatter()
    texts += text
    print(texts)
