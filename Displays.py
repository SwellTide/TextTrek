import curses


class Display:
    def __init__(self):

        # initialize individual screens
        self.title_scrn = curses.newwin(10, 95, 0, 0)
        self.map_scrn = curses.newwin(32, 51, 10, 0)
        self.character_scrn = curses.newwin(15, 44, 18, 51)
        self.status_scrn = curses.newwin(8, 44, 10, 51)
        self.text_scrn = curses.newwin(8, 45, 33, 52)
        self.input_scrn = curses.newwin(1, 42, 41, 52)

        # prepare input screen
        self.input_scrn.addstr(">>")

        # allow map screen to accept arrow input
        self.map_scrn.keypad(True)

    def refresh_display(self):
        self.map_scrn.refresh()
        self.character_scrn.refresh()
        self.status_scrn.refresh()
        self.text_scrn.refresh()
        self.input_scrn.refresh()

    def draw_title(self):
        self.title_scrn.border('|', '|', '-', '-')
        self.title_scrn.attron(curses.color_pair(10))
        self.title_scrn.addstr(2, 15, "*******  ******  *   *  *******    *******  *****   ******  *  *")
        self.title_scrn.addstr(3, 15, "*  *  *  *        * *   *  *  *    *  *  *  *    *  *       * * ")
        self.title_scrn.addstr(4, 15, "   *     ***       *       *          *     *****   ***     **  ")
        self.title_scrn.addstr(5, 15, "   *     *        * *      *          *     *  *    *       * * ")
        self.title_scrn.addstr(6, 15, "   *     ******  *   *     *          *     *   *   ******  *  *")
        self.title_scrn.addstr(8, 15, "Created by: Owen Ripley")
        self.title_scrn.attroff(curses.color_pair(10))

    def draw_map(self, world_map, player, wizard):
        self.map_scrn.erase()
        for i in range(world_map.row):
            for j in range(world_map.column):
                if i == player.location.y and j == player.location.x:
                    self.map_scrn.attron(curses.color_pair(9))
                    self.map_scrn.addch('@')
                    self.map_scrn.attroff(curses.color_pair(9))
                else:
                    if wizard.location is not None:  # ensure the wizard actually exists on the map
                        if i == wizard.location.y and j == wizard.location.x:
                            self.map_scrn.attron(curses.color_pair(8))
                            self.map_scrn.addch('W')
                            self.map_scrn.attroff(curses.color_pair(8))
                        elif world_map.map_grid[i][j].name == "Grass":
                            self.map_scrn.attron(curses.color_pair(1))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(1))
                        elif world_map.map_grid[i][j].name == "Forest":
                            self.map_scrn.attron(curses.color_pair(2))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(2))
                        elif world_map.map_grid[i][j].name == "Water":
                            self.map_scrn.attron(curses.color_pair(3))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(3))
                        elif world_map.map_grid[i][j].name == "Path":
                            self.map_scrn.attron(curses.color_pair(4))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(4))
                        elif world_map.map_grid[i][j].name == "Mountain":
                            self.map_scrn.attron(curses.color_pair(5))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(5))
                        elif world_map.map_grid[i][j].name == "Valley":
                            self.map_scrn.attron(curses.color_pair(6))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(6))
                        elif world_map.map_grid[i][j].name == "Portal":
                            if world_map.map_grid[i][j].discovered:
                                self.map_scrn.attron(curses.color_pair(8))
                                self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                                self.map_scrn.attroff(curses.color_pair(8))
                            else:
                                self.map_scrn.attron(curses.color_pair(6))
                                self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                                self.map_scrn.attroff(curses.color_pair(6))
                        else:
                            self.map_scrn.attron(curses.color_pair(7))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(7))
                    else:
                        if world_map.map_grid[i][j].name == "Grass":
                            self.map_scrn.attron(curses.color_pair(1))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(1))
                        elif world_map.map_grid[i][j].name == "Forest":
                            self.map_scrn.attron(curses.color_pair(2))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(2))
                        elif world_map.map_grid[i][j].name == "Water":
                            self.map_scrn.attron(curses.color_pair(3))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(3))
                        elif world_map.map_grid[i][j].name == "Path":
                            self.map_scrn.attron(curses.color_pair(4))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(4))
                        elif world_map.map_grid[i][j].name == "Mountain":
                            self.map_scrn.attron(curses.color_pair(5))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(5))

                        elif world_map.map_grid[i][j].name == "Valley":
                            self.map_scrn.attron(curses.color_pair(6))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(6))

                        elif world_map.map_grid[i][j].name == "Portal":
                            if world_map.map_grid[i][j].discovered:
                                self.map_scrn.attron(curses.color_pair(8))
                                self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                                self.map_scrn.attroff(curses.color_pair(8))
                            else:
                                self.map_scrn.attron(curses.color_pair(6))
                                self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                                self.map_scrn.attroff(curses.color_pair(6))
                        else:
                            self.map_scrn.attron(curses.color_pair(7))
                            self.map_scrn.addch(world_map.map_grid[i][j].map_char)
                            self.map_scrn.attroff(curses.color_pair(7))

    def draw_status(self, player):
        self.status_scrn.border('|', '|', '-', '-')

        self.status_scrn.addstr(1, 1, str(player.name))
        self.status_scrn.addstr(3, 1, "Coins: " + str(player.coins))
        self.status_scrn.addstr(3, 14, str(player.experience))
        self.status_scrn.addstr(4, 1, "Rations: " + str(player.rations.quantity))
        self.status_scrn.addstr(5, 1, "Bandages: " + str(player.bandages.quantity))
        self.status_scrn.addstr(6, 1, "Health: " + str(player.health))

    def draw_opponent_status(self, opponent):
        self.status_scrn.addstr(1, 24, "Bandit")

        self.status_scrn.addstr(6, 24, "Health: " + str(opponent.health))

    def draw_characters(self, player, wizard):
        self.character_scrn.border('|', '|', '-', '-')

        self.character_scrn.addstr(12, 3, "--------------------------------------")

        self.draw_player(player, 0)

        if wizard.location is not None:
            if player.location == wizard.location:
                self.draw_wizard(wizard)

    def draw_player(self, player, player_attack):

        self.character_scrn.border('|', '|', '-', '-')

        self.character_scrn.addstr(12, 3, "--------------------------------------")

        if player.equipped_weapon.name == "Fist":
            self.character_scrn.addstr(3, 7 + player_attack, "___")
            self.character_scrn.addstr(4, 7 + player_attack, "| .|")
            self.character_scrn.addstr(5, 7 + player_attack, "\\ -/")
            self.character_scrn.addstr(6, 7 + player_attack, "/__\\")
            self.character_scrn.addstr(7, 6 + player_attack, "/|__|\\_")
            self.character_scrn.addstr(8, 5 + player_attack, "(||  | \\)")
            self.character_scrn.addstr(9, 7 + player_attack, "/ /\\")
            self.character_scrn.addstr(10, 6 + player_attack, "/_/ _]")
            self.character_scrn.addstr(11, 6 + player_attack, "\\_) \\_)")

        if player.equipped_weapon.name == "Cudgel":
            self.character_scrn.addstr(3, 7 + player_attack, "___")
            self.character_scrn.addstr(4, 7, "| .| (-)")
            self.character_scrn.addstr(5, 7, "\\ -/ (-)")
            self.character_scrn.addstr(6, 7, "/__\\ (-)")
            self.character_scrn.addstr(7, 6, "/|__|\\(-)")
            self.character_scrn.addstr(8, 5, "(||  | \\I)")
            self.character_scrn.addstr(9, 7, "/ / \\")
            self.character_scrn.addstr(10, 6, "/_/ _]")
            self.character_scrn.addstr(11, 6, "\\_) \\_)")

        if player.equipped_weapon.name == "Spear":
            self.character_scrn.addstr(3, 7 + player_attack, "___")
            self.character_scrn.addstr(4, 7 + player_attack, "| .|  ^")
            self.character_scrn.addstr(5, 7 + player_attack, "\\ -/  |")
            self.character_scrn.addstr(6, 7 + player_attack, "/__\\  |")
            self.character_scrn.addstr(7, 6 + player_attack, "/|__|\\ |")
            self.character_scrn.addstr(8, 5 + player_attack, "(||  | \\O")
            self.character_scrn.addstr(9, 7 + player_attack, "/ / \\ |")
            self.character_scrn.addstr(10, 6 + player_attack, "/_/ _] |")
            self.character_scrn.addstr(11, 6 + player_attack, "\\_) \\_)|")

        if player.equipped_weapon.name == "Sword":
            self.character_scrn.addstr(3, 7 + player_attack, "___       .")
            self.character_scrn.addstr(4, 7 + player_attack, "| .|     /|")
            self.character_scrn.addstr(5, 7 + player_attack, "\\ -/    //")
            self.character_scrn.addstr(6, 7 + player_attack, "/__\\   //")
            self.character_scrn.addstr(7, 6 + player_attack, "/|__|\\_\\/")
            self.character_scrn.addstr(8, 5 + player_attack, "(||  |  O")
            self.character_scrn.addstr(9, 7 + player_attack, "/ / \\")
            self.character_scrn.addstr(10, 6 + player_attack, "/_/ _]")
            self.character_scrn.addstr(11, 6 + player_attack, "\\_) \\_)")

        if player.equipped_weapon.name == "Wizard's Staff":
            self.character_scrn.addstr(3, 7, "___")
            self.character_scrn.addstr(4, 7, "| .|  ")
            self.character_scrn.attron(curses.color_pair(11))
            self.character_scrn.addstr(3, 13, "_")
            self.character_scrn.addstr(4, 12, "/_\\")
            self.character_scrn.addstr(5, 12, "\\_/")
            self.character_scrn.attroff(curses.color_pair(11))
            self.character_scrn.addstr(5, 7, "\\ -/")
            self.character_scrn.addstr(6, 7, "/__\\  |")
            self.character_scrn.addstr(7, 6, "/|__|\\_|")
            self.character_scrn.addstr(8, 5, "(||  | \\)")
            self.character_scrn.addstr(9, 7, "/ / \\ |")
            self.character_scrn.addstr(10, 6, "/_/ _] |")
            self.character_scrn.addstr(11, 6, "\\_) \\_)|")

    def draw_bandit(self, bandit, bandit_attack):

        # bandit attack should be 1 or 0
        # 1 will move character one unit to the left

        if bandit.equipped_weapon.name == "Fist":
            self.character_scrn.addstr(3, 32 - bandit_attack, "__")
            self.character_scrn.addstr(4, 31 - bandit_attack, "|. |")
            self.character_scrn.addstr(5, 28 - bandit_attack, "() \\- / ()")
            self.character_scrn.addstr(6, 29 - bandit_attack, "\\\\/__\\//")
            self.character_scrn.addstr(7, 30 - bandit_attack, "\\|__|/ ")
            self.character_scrn.addstr(8, 31 - bandit_attack, "|  |")
            self.character_scrn.addstr(9, 31 - bandit_attack, "/\\ \\  ")
            self.character_scrn.addstr(10, 30 - bandit_attack, "[_ \\_\\ ")
            self.character_scrn.addstr(11, 29 - bandit_attack, "(_/ (_/")

    def draw_wizard(self, wizard):
        self.character_scrn.attron(curses.color_pair(11))
        self.character_scrn.addstr(3, 28, " _")
        self.character_scrn.addstr(4, 28, "/_\\")
        self.character_scrn.addstr(5, 28, "\\_/")
        self.character_scrn.attroff(curses.color_pair(11))
        self.character_scrn.addstr(3, 30, "   __")
        self.character_scrn.addstr(4, 31, " |. \\")
        self.character_scrn.addstr(5, 31, " \\-_|\\")
        self.character_scrn.addstr(6, 28, " |  /| \\")
        self.character_scrn.addstr(7, 28, " |_/|  |\\")
        self.character_scrn.addstr(8, 28, " (/ |__||)")
        self.character_scrn.addstr(9, 28, " |  /  \\")
        self.character_scrn.addstr(10, 28, " | /    \\")
        self.character_scrn.addstr(11, 28, " | |____|")

    # def draw_bandit(self):