import pygame
import random
import os
from config import LARGURA, ALTURA, PASTA_IMAGENS

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(PASTA_IMAGENS, "jogador.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA // 2, ALTURA - 80)
        self.velocidade = 7

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(PASTA_IMAGENS, "inimigo.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = random.randint(-100, -32)
        self.velocidade = random.randint(4, 8)

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.rect.x = random.randint(0, LARGURA - self.rect.width)
            self.rect.y = random.randint(-100, -32)
            self.velocidade = random.randint(4, 8)
