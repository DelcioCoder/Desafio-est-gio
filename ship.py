import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu retângulo
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()  # Pegamos o retângulo da imagem
        self.screen_rect = screen.get_rect()  # Pegamos o retângulo da tela

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza a posição do centro da espaçonave com base nas flags de movimento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect com o valor de self.center
        self.rect.centerx = self.center

    def blitme(self):
        # Desenha a espaçonave na posição atual
        self.screen.blit(self.image, self.rect)
