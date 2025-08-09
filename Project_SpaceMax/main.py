import pygame
from config import *
from sprites import Jogador, Inimigo

#FUNÇÕES AUXILIARES
def desenhar_texto(surface, texto, tamanho, x, y, cor=BRANCO):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.midtop = (x, y)
    surface.blit(texto_surface, texto_rect)

#INICIALIZAÇÃO
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Max")
clock = pygame.time.Clock()

# Fundo
fundo = pygame.image.load(os.path.join(PASTA_IMAGENS, "fundo.png")).convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

#LOOP PRINCIPAL
jogando = True
while jogando:
    # Criar sprites
    todos_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()

    jogador = Jogador()
    todos_sprites.add(jogador)

    for _ in range(8):
        inimigo = Inimigo()
        todos_sprites.add(inimigo)
        inimigos.add(inimigo)

    # Variáveis do jogo
    pontuacao = 0
    rodando = True

    while rodando:
        clock.tick(FPS)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                jogando = False

        # Atualizações
        todos_sprites.update()
        pontuacao += 1

        # Colisão
        if pygame.sprite.spritecollide(jogador, inimigos, False):
            rodando = False

        # Desenho
        tela.blit(fundo, (0, 0))
        todos_sprites.draw(tela)
        desenhar_texto(tela, f"Pontuação: {pontuacao}", 36, LARGURA // 2, 10)
        pygame.display.flip()

    #Tela de Game Over
    tela.blit(fundo, (0, 0))
    desenhar_texto(tela, "GAME OVER", 64, LARGURA // 2, ALTURA // 3)
    desenhar_texto(tela, f"Sua pontuação: {pontuacao}", 48, LARGURA // 2, ALTURA // 2)
    desenhar_texto(tela, "Pressione ESPAÇO para jogar novamente", 36, LARGURA // 2, ALTURA // 1.5)
    pygame.display.flip()

    esperando = True
    while esperando and jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                esperando = False
                jogando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

pygame.quit()
