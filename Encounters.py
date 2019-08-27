import curses
import time
from WriteText import *
from random import randint
from Characters import *


class Encounters:

    def __init__(self, display):
        self.wizard_meet_counter = 0
        self.scribe = Scribe(display)

    def check(self, player, wizard, display):
        if player.location == wizard.location:
            self.wizard_encounter(player, wizard, display)

        elif player.location.is_city:
            self.city_encounter(player)

        elif player.location.name == "Portal":
            self.portal_encounter(player)

        elif randint(0, player.location.odds_of_bandit) == 1:
            self.bandit_encounter(player, display)

    def wizard_encounter(self, player, wizard, display):
        display.draw_characters(player, wizard)
        if self.wizard_meet_counter == 0:
            self.wizard_meet_counter += 1

            time.sleep(1)

            self.scribe.notify("Hello, I am Paddington the Wizard! And you are?")
            player.name = self.scribe.listen()
            display.draw_status(player)
            display.refresh_display()
            self.scribe.write("Pleased to meet you " + player.name + ". I tend to chatter on pretty quickly. Press any key to let me know you're ready to keep listening!")
            self.scribe.write("What's that? You're lost, eh?")
            self.scribe.write("Well, if you need a way out... there's rumoured to be a hidden Portal somewhere in these lands.")
            self.scribe.write("To find the lost Portal would be a dangerous adventure indeed! You'll need to learn how to protect yourself.")
            self.scribe.write("Go to Shorepoint City and visit George the weapon smith. He'll help you out.")
            self.scribe.write("Oh and here, take these Rations. You don't want to starve to death on your journey! You'll need to eat whenever you travel. Au revoir!")
            player.add_rations(20)
            display.draw_status(player)
            display.refresh_display()
            wizard.location = None
            display.character_scrn.erase()
            display.draw_characters(player, wizard)
            display.refresh_display()
            self.scribe.notify("The wizard vanished without a trace...")

    def city_encounter(self, player):
        self.scribe.notify("Arrived at " + player.location.name + ".")

    def portal_encounter(self, player):
        if not player.location.discovered:
            self.scribe.notify("Discovered the Portal!")
            player.location.discover()

    # probably won't end up using this function
    def random_enemy(self, player, text_scrn, character_scrn, status_scrn):
        replace = True

    def bandit_encounter(self, player, display):
        from Characters import Bandit

        bandit = Bandit(player.experience)  # create new bandit
        display.draw_bandit(bandit, 0)

        display.refresh_display()

        time.sleep(0.5)

        self.scribe.notify("You were jumped by a bandit!")

        time.sleep(0.5)

        display.draw_opponent_status(bandit)  # obtain and display information about bandit
        display.draw_status(player)  # draw player status
        display.refresh_display()  # refresh display so visible to player

        max_bandit_health = bandit.health
        max_player_health = 100  # this needs to be changed to dynamic player health system

        turn = 0

        while player.health != 0 and bandit.health != 0:

            display.draw_bandit(bandit, 0)
            display.draw_player(player, 0)
            display.refresh_display()

            if turn % 2 == 0:
                curses.flushinp()

                display.text_scrn.erase()
                display.text_scrn.addstr("Your turn.")
                display.text_scrn.addstr(2, 0, "'F': Attack")
                display.text_scrn.addstr(3, 0, "'C': Heal")
                display.text_scrn.addstr(4, 0, "'R': Run away (uses 3 Rations)")
                display.refresh_display()

                ch = display.map_scrn.getch()

                if ch == ord('f') or ch == ord('F'):
                    damage = player.attack()

                    display.character_scrn.erase()
                    display.draw_bandit(bandit, 0)
                    display.draw_player(player, 1)
                    display.refresh_display()

                    time.sleep(0.25)

                    display.character_scrn.erase()
                    display.draw_bandit(bandit, 0)
                    display.draw_player(player, 0)
                    display.refresh_display()

                    bandit.receive_damage(damage)
                    self.scribe.notify("Dealt " + str(damage) + " damage!")

                    turn += 1

                elif ch == ord('r') or ch == ord('R'):
                    player.run_away()
                    print("RUN")

                    turn += 1

                elif ch == ord('c') or ch == ord('C'):
                    if player.health < 100 and player.bandages.quantity != 0:
                        player.heal()
                        if player.health > max_player_health:
                            player.health = max_player_health
                        self.scribe.notify("You healed yourself!")
                        turn += 1
                    elif player.health == 100:
                        self.scribe.notify("Already at full health!")
                    elif player.bandages.quantity == 0:
                        self.scribe.notify("You are out of bandages!")

                time.sleep(1)

            else:
                if bandit.health < max_bandit_health * .3 and bandit.bandages.quantity > 0:  # less than 30 percent
                    bandit.heal()
                    if bandit.health > max_bandit_health:
                        bandit.health = max_bandit_health
                    self.scribe.notify("The bandit healed themselves!")

                    turn += 1

                else:
                    damage = bandit.attack()

                    display.character_scrn.erase()
                    display.draw_player(player, 0)
                    display.draw_bandit(bandit, 1)
                    display.refresh_display()

                    time.sleep(0.25)

                    display.character_scrn.erase()
                    display.draw_player(player, 0)
                    display.draw_bandit(bandit, 0)
                    display.refresh_display()

                    player.receive_damage(damage)

                    self.scribe.notify("You took " + str(damage) + " damage!")

                    turn += 1

                time.sleep(1)

            display.status_scrn.erase()
            display.draw_opponent_status(bandit)  # obtain and display information about bandit
            display.draw_status(player)  # draw player status
            display.refresh_display()  # refresh display so visible to player

        if player.health == 0:
            self.scribe.write("You died!")

        elif bandit.health == 0:
            self.scribe.notify("Bandit defeated!")

        display.character_scrn.erase()
        display.status_scrn.erase()
        display.draw_player(player, 0)
        display.draw_status(player)
        display.refresh_display()
