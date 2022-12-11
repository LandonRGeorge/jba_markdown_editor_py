formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line",
]
msg = f"""\
Available formatters: {" ".join(formatters)}
Special commands: !help !done\
"""
while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print(msg)
        continue
    if formatter == "!done":
        break
    if formatter not in formatters:
        print("Unknown formatting type or command")
        continue
