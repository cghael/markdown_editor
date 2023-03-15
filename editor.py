class Editor:
    def __init__(self):
        self.formatters = {
            "plain": self._plain,
            "bold": self._bold,
            "italic": self._italic,
            "header": self._header,
            "link": self._link,
            "inline-code": self._inline_code,
            "new-line": self._new_line,
            "ordered-list": self._list,
            "unordered-list": self._list
        }
        self.commands = {
            "!help": self._help_cmd,
            "!done": self._done_cmd
        }

    def run(self):
        result = ""
        while True:
            choose = self._choose_formater()
            if choose in self.commands:
                if choose == "!done":
                    self.commands[choose](result)
                else:
                    self.commands[choose]()
                continue
            elif choose in self.formatters:
                if choose == "unordered-list":
                    formatted_text = self.formatters[choose](False)
                else:
                    formatted_text = self.formatters[choose]()

                if choose == "header" and not result:
                    formatted_text = formatted_text[1:]

                result += formatted_text
            print(result)

    def _choose_formater(self):
        while True:
            user_choose = input("Choose a formatter: ")
            if user_choose in self.commands or user_choose in self.formatters:
                return user_choose
            print("Unknown formatting type or command")

    # ---------- formatters ----------

    def _plain(self):
        return self._set_text()

    def _bold(self):
        text = self._set_text()
        return f"**{text}**"

    def _italic(self):
        text = self._set_text()
        return f"*{text}*"

    def _header(self):
        lvl = 0
        while True:
            try:
                lvl = int(input("Level: "))
                if lvl not in range(1, 7):
                    raise TypeError
                break
            except TypeError:
                print("The level should be within the range of 1 to 6")

        text = self._set_text()
        return f"\n{'#' * lvl} {text}\n"

    def _link(self):
        lable = input("Label: ")
        url = input("URL: ")  # TODO make check for url
        return f"[{lable}]({url})"

    def _inline_code(self):
        text = self._set_text()
        return f"`{text}`"

    def _new_line(self):
        return "\n"

    def _list(self, ordered=True):
        n_rows = 0
        while True:
            try:
                n_rows = int(input("Number of rows: "))
                if n_rows <= 0:
                    raise ValueError
                break
            except ValueError:
                print("The number of rows should be greater than zero")

        lines = []
        for i in range(1, n_rows + 1):
            line = input(f"Row #{i}: ")
            line = f"{i}. {line}\n" if ordered else f"* {line}\n"
            lines.append(line)
        return "".join(lines)

    # ---------- commands ----------

    def _help_cmd(self):
        print(f"Available formatters: {' '.join(self.formatters)}")
        print(f"Special commands: {' '.join(self.commands)}")

    def _done_cmd(self, result):
        with open("output.md", "w") as f:
            f.write(result)
        exit()

    # ---------- helpers ----------

    def _set_text(self):
        return input("Text: ")


def main():
    md_editor = Editor()
    md_editor.run()


if __name__ == "__main__":
    main()