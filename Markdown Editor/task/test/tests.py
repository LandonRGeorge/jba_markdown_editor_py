from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


class Test(StageTest):

    @dynamic_test
    def test1(self):
        pr = TestedProgram()
        pr.start()

        output = pr.execute('random').strip().lower()
        if 'unknown formatting type or command' not in output.strip().lower():
            return CheckResult.wrong('In case of an unknown formatter the program should return the corresponding message: "Unknown formatting type or command"')

        pr.execute('!done')
        if not pr.is_finished():
            return CheckResult.wrong('Your program should finish its execution whenever !done is an input')

        return CheckResult.correct()

    @dynamic_test
    def test2(self):
        pr = TestedProgram()
        pr.start()
        formatters = ['plain', 'bold', 'italic', 'header', 'ordered-list', 'unordered-list',
                      'link', 'inline-code', 'new-line']
        commands = ['!help', '!done']

        output = list(map(lambda item: item.lower(), pr.execute('!help').split('\n')))
        if len(output) != 3:
            return CheckResult.wrong('!help command should return the list of available formatting types, and the list of special commands, on separate rows, and the prompt a user for an input')

        for formatter in formatters:
            if formatter not in output[0].split():
                return CheckResult.wrong('One or more formatting types are not present in the output of !help command')

        for command in commands:
            if command not in output[1].split():
                return CheckResult.wrong('One or more special commands are not present in the output of !help command')

        if 'formatter' not in output[2].strip():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        pr.execute('!done')
        if not pr.is_finished():
            return CheckResult.wrong('Your program should finish its execution whenever !done is an input')

        return CheckResult.correct()

    @dynamic_test
    def test3(self):
        pr = TestedProgram()
        pr.start()

        output = pr.execute('header').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('ordered-list').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('unordered-list').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('link').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('inline-code').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('new-line').strip().lower()
        if len(output.split('\n')) != 1 and 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        pr.execute('!done')
        if not pr.is_finished():
            return CheckResult.wrong('Your program should finish its execution whenever !done is an input')

        return CheckResult.correct()

    @dynamic_test
    def test4(self):
        pr = TestedProgram()
        pr.start()

        output = pr.execute('plain').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('bold').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        output = pr.execute('italic').strip().lower()
        if len(output.split('\n')) != 1 or 'formatter' not in output.strip().lower():
            return CheckResult.wrong('A user should be prompted for input again, i.e  "- Choose a formatter: > "')

        pr.execute('!done')
        if not pr.is_finished():
            return CheckResult.wrong('Your program should finish its execution whenever !done is an input')

        return CheckResult.correct()


if __name__ == '__main__':
    Test().run_tests()
