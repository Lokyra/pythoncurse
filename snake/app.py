import curses


def main(stdscr):
    stdscr.clear()

    curses.curs_set(0)

    y, x = 0, 0

    char = "@"
    space = " "

    stdscr.addstr(y, x, char)

    stdscr.refresh()

    while True:
        key = stdscr.getkey()

        cur_y, cur_x = y, x

        if key == "KEY_UP":
            y = max(y - 1, 0)

        elif key == "KEY_DOWN":
            y = min(y + 1, stdscr.getmaxyx()[0] - 1)

        elif key == "KEY_LEFT":
            x = max(x - 1, 0)

        elif key == "KEY_RIGHT":
            x = min(x + 1, stdscr.getmaxyx()[1] - 1)

        elif key == "a":
            char = char + "@"
            space = space + " "

        elif key == "q":
            break

        stdscr.addstr(cur_y, cur_x, space)

        stdscr.move(y, x)

        stdscr.addstr(char)

        stdscr.refresh()


curses.wrapper(main)
