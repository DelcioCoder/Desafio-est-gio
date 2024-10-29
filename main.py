import pygame
import sys

# My modules 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Corrigido o erro de digitação
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:

        ship.update()
        
        # Verifica eventos de teclado e mouse
        gf.check_event(ship)

        gf.update_screen(ai_settings, screen, ship)
        
        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()
