import pygame

pygame.init()

W, H = 1280, 700
FPS = 20

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dino Platformer")

clock = pygame.time.Clock()