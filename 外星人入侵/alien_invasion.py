import sys
import pygame
from pygame.display import set_caption

class AlienInvasion:
    def __init__(self):
        """初始化游戏并创建游系资源"""
        pygame.init()

        self.screen = pygame.display.set.mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self)：