import pygame
import sys

# My modules 
from settings import Settings

def run_game():
    #inicializa o jogo e cria um objecto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.sreen_height))
    pygame.display.set_caption("Alien Invasion")

    #inicia o laço principal do jogo
    while True:
        screen.fill(ai_settings.bg_color)
        #verifica eventos de teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #deixa a tela mais recente visivel
        pygame.display.flip()


run_game()