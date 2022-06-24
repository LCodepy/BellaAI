from os.path import join

import pygame

from bela.game.utils.singleton import Singleton


class Assets(metaclass=Singleton):

    """
    Class for loading and accessing all assets in the project.
    """

    PATH_IMAGES = "Assets/Images/"

    def __init__(self) -> None:
        self.font18 = pygame.font.SysFont("consolas", 18)
        self.font24 = pygame.font.SysFont("consolas", 24)
        self.font32 = pygame.font.SysFont("consolas", 32)
        self.font48 = pygame.font.SysFont("consolas", 48)
        self.font64 = pygame.font.SysFont("consolas", 64)

        self.card_names = [
            list(map(lambda x: (x, "herc"), ["as", "7", "8", "9", "cener", "unter", "baba", "kraj"])),
            list(map(lambda x: (x, "pik"), ["as", "7", "8", "9", "cener", "unter", "baba", "kraj"])),
            list(map(lambda x: (x, "karo"), ["as", "7", "8", "9", "cener", "unter", "baba", "kraj"])),
            list(map(lambda x: (x, "tref"), ["as", "7", "8", "9", "cener", "unter", "baba", "kraj"]))
        ]
        self.cards = self.edit_sprite_sheet(self.load_sprite_sheet("karte.png", 4, 8), self.card_names)

    def load_sprite_sheet(self, filename: str, rows: int, cols: int) -> list[list[pygame.Surface]]:
        sheet = []

        img = pygame.image.load(self.PATH_IMAGES + filename).convert_alpha()

        for x, i in enumerate(range(0, img.get_height(), img.get_height() // rows)):
            sheet.append([])
            for j in range(0, img.get_width(), img.get_width() // cols):
                sheet[x].append(img.subsurface([j, i, img.get_width() // cols, img.get_height() // rows]))

        return sheet

    def edit_sprite_sheet(self, sheet: list[list[pygame.Surface]], names: list[list]) -> dict[str, pygame.Surface]:
        d = {}
        for i in range(len(sheet)):
            for j in range(len(sheet[0])):
                d[names[i][j]] = sheet[i][j]
        return d

