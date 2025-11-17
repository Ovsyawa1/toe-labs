import curses
from curses import wrapper
import time

from lab_3.task_2.chars_classes import Saber


def main(stdscr: curses.window):
    member_1 = Saber("Arhuria")
    stats_text = f"{member_1.name} Stats: \n\
{member_1.health} HP | \
{member_1.defence} DEF | \
{member_1.damage} DMG\n\
{member_1.strength} STR | \
{member_1.agility} AGL | \
{member_1.intelligence} INT | \
{member_1.faith} FTH"

    stats_window = curses.newwin(4, 80, 20, 0)

    for i in range(10):
        stdscr.clear()
        stdscr.addstr(f"Hello, World! {i}")
        stdscr.refresh()

        stats_window.clear()
        stats_window.addstr(stats_text)
        stats_window.refresh()

        time.sleep(0.5)

    stdscr.getch()


wrapper(main)
