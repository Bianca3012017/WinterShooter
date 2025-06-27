#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_index = menu.run()


            if menu_index in [0, 1, 2]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_index, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_index, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_index, player_score)

            elif menu_index == MENU_OPTION[3]:
                score.show()
            elif menu_index == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pygame.quit()
                sys.exit()
