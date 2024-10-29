import pygame

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()  # Pegamos o retângulo da imagem
        self.screen_rect = screen.get_rect()  # Pegamos o retângulo da tela

        #flag de movimento
        self.moving_right = False
        self.moving_left = False

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        if self.moving_right:
          self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        # Desenha a espaçonave na posição atual
        self.screen.blit(self.image, self.rect)
