import pygame
import subprocess

def switch_to_terminal():
    subprocess.Popen('code --goto %d:%d', shell=True)

pygame.init()
window = pygame.display.set_mode((200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                switch_to_terminal()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
