#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_CYAN, MENU_OPTION, C_GREEN, C_YELLOW, C_WHITE, C_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Winter", C_CYAN, ((WIN_WIDTH / 2), 70), border_color=C_WHITE)
            self.menu_text(50, "Shooter", C_CYAN, ((WIN_WIDTH / 2), 120), border_color=C_WHITE)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i), border_color=C_ORANGE)
                else:
                    self.menu_text(20, MENU_OPTION[i], C_GREEN, ((WIN_WIDTH / 2), 200 + 25 * i), border_color=C_WHITE)
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    elif event.key == pygame.K_RETURN:  # ENTER
                        return menu_option

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, border_color=None):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        if border_color:
            # Draws the border in 8 directions
            for dx in [-2, 0, 2]:
                for dy in [-2, 0, 2]:
                    if dx != 0 or dy != 0:
                        border_surf: Surface = text_font.render(text, True, border_color).convert_alpha()
                        border_rect: Rect = border_surf.get_rect(
                            center=(text_center_pos[0] + dx, text_center_pos[1] + dy))
                        self.window.blit(border_surf, border_rect)

        # Main text in the center
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
