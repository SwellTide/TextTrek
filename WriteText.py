import curses
import time


class Scribe:

    def __init__(self, display):
        self.seconds = .03
        self.display = display
        self.line_length = 0

    def check_line_fit(self, w):
        self.line_length += (len(w) + 1)  # plus 1 for the space
        if self.line_length > 38:
            self.display.text_scrn.addstr(str("\n"))
            self.line_length = 0

    def write(self, string):  # character must acknowledge message with a pressed key to continue
        self.display.text_scrn.erase()
        self.display.text_scrn.refresh()

        self.print_to_text_scrn(string)

        self.display.text_scrn.getch()
        self.display.text_scrn.erase()
        self.display.text_scrn.refresh()

    def notify(self, string):  # doesn't impede character actions
        self.display.text_scrn.erase()
        self.display.text_scrn.refresh()

        self.print_to_text_scrn(string)

    def print_to_text_scrn(self, string):
        words = string.split(' ')

        for w in words:  # each word
            self.check_line_fit(w)
            chars = list(w)
            for c in chars:
                self.display.text_scrn.addstr(c)
                if c == "," or c == "." or c == "!" or c == "?":
                    self.display.text_scrn.refresh()
                    time.sleep(.1)
                self.display.text_scrn.refresh()
                time.sleep(self.seconds)

            self.display.text_scrn.addstr(" ")

        self.line_length = 0

        curses.flushinp()

    def listen(self):
        curses.echo()
        string = self.display.input_scrn.getstr()
        curses.noecho()
        self.display.input_scrn.erase()
        self.display.input_scrn.addstr(">>")
        self.display.input_scrn.refresh()

        string = str(string)
        string = string[2:len(string) - 1]

        return string
