import curses
import sys
import time
from World import *
from Characters import *
from Displays import *


def main():

    # initialize curses
    curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_GREEN)  # grass
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_GREEN)  # forest
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLUE)  # water
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)  # path
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)  # mountain
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_GREEN)  # valley
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED)  # city
    curses.init_pair(8, curses.COLOR_BLUE, curses.COLOR_WHITE)  # portal & wizard
    curses.init_pair(9, curses.COLOR_MAGENTA, curses.COLOR_WHITE)  # player
    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_BLACK)  # title
    curses.init_pair(11, curses.COLOR_CYAN, curses.COLOR_BLACK)  # staff topper

    # initialize game windows
    display = Display()

    # initialize world map and player
    world_map = Map()
    player = Player(world_map.map_grid[10][42])
    wizard = Wizard(world_map.map_grid[8][42])
    encounters = Encounters(display)

    # display title
    display.draw_title()
    display.title_scrn.refresh()

    # draw map in loop
    ch = ' '
    while ch != 'q':

        display.draw_map(world_map, player, wizard)
        display.draw_status(player)
        display.draw_characters(player, wizard)
        display.refresh_display()

        # if wizard, wizard encounter
        # if null, chance for enemy encounter
        # if player.location.is_wizard_occupied:
        #     encounters.wizard_encounter(player, wizard, text_scrn, character_scrn)
        # encounters.city_encounter(player, text_scrn, character_scrn)

        encounters.check(player, wizard, display)
        curses.flushinp()

        ch = display.map_scrn.getch()                                           # get user input.

        display.text_scrn.erase()
        display.refresh_display()

        if ch == ord('q') or ch == ord('Q'):
            # close curses window

            print("hello from quitting")

            curses.nocbreak()
            curses.echo()
            display.map_scrn.keypad(False)
            curses.endwin()
            ch = 'q'                                                    # needed to exit loop, close window properly

        else:
            # player.action(ch, world_map)

            if ch == curses.KEY_UP or ch == ord('w') or ch == ord('W'):
                player.travel(-1, 0, world_map)
            if ch == curses.KEY_DOWN or ch == ord('s') or ch == ord('S'):
                player.travel(1, 0, world_map)
            if ch == curses.KEY_RIGHT or ch == ord('d') or ch == ord('D'):
                player.travel(0, 1, world_map)
            if ch == curses.KEY_LEFT or ch == ord('a') or ch == ord('A'):
                player.travel(0, -1, world_map)


if __name__ == '__main__':
    main()
